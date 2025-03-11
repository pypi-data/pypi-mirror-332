# Introduction

`starlette-caches` provides middleware and utilities for adding server-side HTTP caching to ASGI applications. It is powered by [`aiocache`](https://aiocache.aio-libs.org/en/latest/), and inspired by Django's cache framework.

!!! warning
    This project is in an "alpha" status. Several features still need to be implemented, and you should expect breaking API changes across minor versions.

## Features

- Compatibility with any ASGI application (e.g. Starlette, FastAPI, Quart, etc.).
- Support for application-wide or per-endpoint caching.
- Ability to fine-tune the cache behavior (TTL, cache control) down to the endpoint level.
- Clean and explicit API enabled by a loose coupling with `aiocache`.
- Fully type annotated.
- 100% test coverage.

## Installation

```bash
pip install "starlette-caches==0.*"
```

## Quickstart

```python
from aiocache import Cache
from starlette_caches.middleware import CacheMiddleware

cache = Cache()

async def app(scope, receive, send):
    assert scope["type"] == "http"
    headers = [(b"content-type", "text/plain")]
    await send({"type": "http.response.start", "status": 200, "headers": headers})
    await send({"type": "http.response.body", "body": b"Hello, world!"})

app = CacheMiddleware(app, cache=cache)
```

This example:

- Sets up an in-memory cache (see the [aiocache docs](https://aiocache.aio-libs.org/en/latest/) for specifics).
- Sets up an application (in this case, a raw-ASGI 'Hello, world!' app).
- Applies caching on the entire application.

To learn more, head to the [User Guide](usage/index.md).

## Credits

Due credit goes to the Django developers and maintainers, as a lot of the API and implementation was directly inspired by the [Django cache framework](https://docs.djangoproject.com/en/2.2/topics/cache/).
