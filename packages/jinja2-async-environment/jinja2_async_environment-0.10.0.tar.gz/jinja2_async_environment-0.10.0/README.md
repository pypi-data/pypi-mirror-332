# Jinja2 Async Environment

A Python library that provides asynchronous support for Jinja2 templates, making it easy to use Jinja2 in asynchronous applications without blocking the event loop.

## Features

- **Asynchronous Template Loading**: Load templates asynchronously from filesystem, packages, dictionaries, and more
- **Asynchronous Bytecode Caching**: Cache compiled templates in Redis for improved performance
- **Multiple Async Loaders**: Choose from various async template loader implementations
- **Compatible with Standard Jinja2**: Uses the same template syntax and follows Jinja2 conventions

## Installation

```bash
pip install jinja2-async-environment
```

## Requirements

- Python 3.13+
- Jinja2
- aiopath
- redis-py (for Redis bytecode caching)

## Usage

### Basic Example

```python
import asyncio
from jinja2_async_environment import AsyncEnvironment, AsyncFileSystemLoader

async def render_template():
    # Create an async environment with filesystem loader
    env = AsyncEnvironment(
        loader=AsyncFileSystemLoader("templates")
    )

    # Load template asynchronously
    template = await env.get_template_async("index.html")

    # Render the template
    content = await template.render_async(name="World")
    return content

# Run the async function
content = asyncio.run(render_template())
print(content)
```

### Using Redis Bytecode Cache

```python
from redis.asyncio import Redis
from jinja2_async_environment import AsyncEnvironment, AsyncFileSystemLoader, AsyncRedisBytecodeCache

async def create_environment():
    # Initialize Redis cache
    redis_client = Redis(host="localhost", port=6379)
    cache = AsyncRedisBytecodeCache(
        prefix="jinja2_templates",
        client=redis_client
    )

    # Create environment with Redis cache
    env = AsyncEnvironment(
        loader=AsyncFileSystemLoader("templates"),
        bytecode_cache=cache
    )

    return env
```

### Multiple Template Loaders

```python
from jinja2_async_environment import (
    AsyncEnvironment,
    AsyncChoiceLoader,
    AsyncFileSystemLoader,
    AsyncPackageLoader
)

# Try multiple loaders in sequence
loader = AsyncChoiceLoader([
    AsyncFileSystemLoader("templates"),
    AsyncPackageLoader("my_package", "templates")
], searchpath="templates")

env = AsyncEnvironment(loader=loader)
```

## API Reference

### AsyncEnvironment

```python
class AsyncEnvironment(Environment):
    """Async environment for Jinja2 templates."""

    async def get_template_async(name, parent=None, globals=None):
        """Get a template by name asynchronously."""

    async def select_template_async(names, parent=None, globals=None):
        """Select a template from a list of names asynchronously."""

    async def get_or_select_template_async(template_name_or_list, parent=None, globals=None):
        """Get a template by name or select from a list asynchronously."""
```

### Loaders

```python
class AsyncBaseLoader:
    """Base class for async template loaders."""

    async def get_source(template):
        """Get the source code of a template."""

    async def list_templates():
        """List all available templates."""
```

#### Available Loaders

- `AsyncFileSystemLoader`: Load templates from the filesystem
- `AsyncPackageLoader`: Load templates from a Python package
- `AsyncDictLoader`: Load templates from a dictionary
- `AsyncFunctionLoader`: Load templates using a custom async function
- `AsyncChoiceLoader`: Try multiple loaders in sequence

### Bytecode Cache

```python
class AsyncBytecodeCache:
    """Base class for async bytecode caches."""

    async def load_bytecode(bucket):
        """Load bytecode from the cache."""

    async def dump_bytecode(bucket):
        """Dump bytecode to the cache."""

class AsyncRedisBytecodeCache(AsyncBytecodeCache):
    """A bytecode cache that stores bytecode in Redis."""
```

## License

This project is licensed under the BSD 3-Clause License.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
