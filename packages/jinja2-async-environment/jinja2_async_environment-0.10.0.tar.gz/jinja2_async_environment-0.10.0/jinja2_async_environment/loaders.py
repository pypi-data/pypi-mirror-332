import typing as t
from contextlib import suppress
from importlib import import_module

from aiopath import AsyncPath
from jinja2.environment import Template
from jinja2.exceptions import TemplateNotFound
from jinja2.utils import internalcode
from .environment import AsyncEnvironment

# Type aliases
SourceType: t.TypeAlias = tuple[str | bytes, str | None, t.Callable[[], bool] | None]
LoaderFunc: t.TypeAlias = t.Callable[[AsyncPath], t.Awaitable[str | bytes | None]]
UpToDateCallable: t.TypeAlias = t.Callable[[], t.Awaitable[bool]]
WalkType: t.TypeAlias = t.Any  # Actual return type from AsyncPath.walk()


class PackageSpecNotFound(TemplateNotFound):
    """Raised if a package spec not found."""


class LoaderNotFound(TemplateNotFound):
    """Raised if a loader is not found."""


class AsyncBaseLoader:
    """Base class for async template loaders."""

    has_source_access: bool = True
    searchpath: t.Sequence[AsyncPath]

    def __init__(self, searchpath: AsyncPath | t.Sequence[AsyncPath]) -> None:
        """Initialize the loader with a search path."""
        self.searchpath = (
            [searchpath] if not isinstance(searchpath, t.Sequence) else searchpath
        )

    async def get_source(self, template: AsyncPath) -> SourceType:
        """Get the source code of a template."""
        raise NotImplementedError()

    async def list_templates(self) -> list[str]:
        """List all available templates."""
        raise NotImplementedError()

    @internalcode
    async def load(
        self,
        environment: AsyncEnvironment,
        name: str,
        globals: t.MutableMapping[str, t.Any] | None = None,
    ) -> Template:
        """Load a template from the loader."""
        source, _, _ = await self.get_source(AsyncPath(name))
        globals = environment.make_globals(globals)
        if isinstance(source, bytes):
            source = source.decode("utf-8")  # Use UTF-8 as default encoding
        return environment.from_string(source, template_class=None, globals=globals)


class AsyncFileSystemLoader(AsyncBaseLoader):
    """Load templates from the file system."""

    encoding: str
    followlinks: bool

    def __init__(
        self,
        searchpath: AsyncPath | t.Sequence[AsyncPath],
        encoding: str = "utf-8",
        followlinks: bool = False,
    ) -> None:
        """Initialize the loader with a search path."""
        super().__init__(searchpath)
        self.encoding = encoding
        self.followlinks = followlinks

    async def get_source(self, template: AsyncPath) -> SourceType:
        """Get the source code of a template."""
        pieces = template.parts
        for searchpath in self.searchpath:
            filename = searchpath.joinpath(*pieces)
            if not await filename.is_file():
                continue

            async def uptodate() -> bool:
                return await filename.exists()

            async with filename.open("r", encoding=self.encoding) as f:
                contents = await f.read()
            return contents, str(filename), t.cast(t.Callable[[], bool], uptodate)

        raise TemplateNotFound(str(template))

    async def list_templates(self) -> list[str]:
        """List all available templates."""
        found = set()
        for searchpath in self.searchpath:
            walk: WalkType = searchpath.walk(follow_symlinks=self.followlinks)
            async for dirpath, _, filenames in walk:
                for filename in filenames:
                    template = str(
                        AsyncPath(dirpath).relative_to(searchpath).joinpath(filename)
                    )
                    if template.startswith("./"):
                        template = template.removeprefix("./")
                    found.add(template)
        return sorted(found)


class AsyncPackageLoader(AsyncBaseLoader):
    """Load templates from a Python package."""

    package_path: AsyncPath
    package_name: str
    encoding: str
    _template_root: AsyncPath

    def __init__(
        self,
        package_name: str,
        searchpath: AsyncPath | t.Sequence[AsyncPath],
        package_path: AsyncPath = AsyncPath("templates"),
        encoding: str = "utf-8",
    ) -> None:
        """Initialize the loader with a package name."""
        super().__init__(searchpath)
        self.package_name = package_name
        self.package_path = package_path
        self.encoding = encoding

        spec = import_module(package_name).__spec__
        if spec is None or spec.origin is None:
            raise ValueError(f"Could not find package {package_name}")

        self._template_root = AsyncPath(spec.origin).parent / package_path

    async def get_source(self, template: AsyncPath) -> SourceType:
        """Get the source code of a template."""
        path = self._template_root / template
        if not await path.is_file():
            raise TemplateNotFound(str(template))

        async def uptodate() -> bool:
            return await path.exists()

        async with path.open("r", encoding=self.encoding) as f:
            source = await f.read()
        return source, str(path), t.cast(t.Callable[[], bool], uptodate)

    async def list_templates(self) -> list[str]:
        """List all available templates."""
        results: list[str] = []
        walk: WalkType = self._template_root.walk()
        async for dirpath, _, filenames in walk:
            for filename in filenames:
                template = str(
                    AsyncPath(dirpath)
                    .relative_to(self._template_root)
                    .joinpath(filename)
                )
                if template.startswith("./"):
                    template = template.removeprefix("./")
                results.append(template)
        results.sort()
        return results


class AsyncDictLoader(AsyncBaseLoader):
    """Load templates from a dictionary."""

    mapping: t.Mapping[str, str]

    def __init__(
        self,
        mapping: t.Mapping[str, str],
        searchpath: AsyncPath | t.Sequence[AsyncPath],
    ) -> None:
        """Initialize the loader with a mapping."""
        super().__init__(searchpath)
        self.mapping = mapping

    async def get_source(self, template: AsyncPath) -> SourceType:
        """Get the source code of a template."""
        template_str = str(template)
        if template_str not in self.mapping:
            raise TemplateNotFound(template_str)
        source = self.mapping[template_str]
        return source, None, None

    async def list_templates(self) -> list[str]:
        """List all available templates."""
        return sorted(self.mapping)


class AsyncFunctionLoader(AsyncBaseLoader):
    """Load templates from a function."""

    load_func: LoaderFunc

    def __init__(
        self,
        load_func: LoaderFunc,
        searchpath: AsyncPath | t.Sequence[AsyncPath],
    ) -> None:
        """Initialize the loader with a function."""
        super().__init__(searchpath)
        self.load_func = load_func

    async def get_source(self, template: AsyncPath) -> SourceType:
        """Get the source code of a template."""
        source = await self.load_func(template)
        if source is None:
            raise TemplateNotFound(str(template))
        return source, None, None


class AsyncChoiceLoader(AsyncBaseLoader):
    """Load templates from multiple loaders."""

    loaders: list[AsyncBaseLoader]

    def __init__(
        self,
        loaders: list[AsyncBaseLoader],
        searchpath: AsyncPath | t.Sequence[AsyncPath],
    ) -> None:
        """Initialize the loader with a list of loaders."""
        super().__init__(searchpath)
        self.loaders = loaders

    async def get_source(self, template: AsyncPath) -> SourceType:
        """Get the source code of a template."""
        for loader in self.loaders:
            with suppress(TemplateNotFound):
                return await loader.get_source(template)
        raise TemplateNotFound(str(template))

    async def list_templates(self) -> list[str]:
        """List all available templates."""
        found = set()
        for loader in self.loaders:
            found.update(await loader.list_templates())
        return sorted(found)
