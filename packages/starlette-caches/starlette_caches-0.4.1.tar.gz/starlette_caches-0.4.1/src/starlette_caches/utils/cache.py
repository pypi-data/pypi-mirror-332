"""Utilities that add HTTP-specific to aiocache.

The `store_in_cache()` and `get_from_cache()` helpers are the main pieces of API
defined in this module:

* `store_in_cache()` learns a cache key from a `(request, response)` pair.
* `get_from_cache()` retrieves and uses this cache key for a new `request`.
"""

from __future__ import annotations

import hashlib
import time
import typing
from urllib.request import parse_http_list

from starlette.responses import Response

from ..exceptions import RequestNotCachable, ResponseNotCachable
from ..rules import Rule, get_rule_matching_request, get_rule_matching_response
from .logging import get_logger
from .misc import bytes_to_json_string, http_date, json_string_to_bytes

if typing.TYPE_CHECKING:
    from collections.abc import Sequence

    from aiocache import BaseCache
    from starlette.datastructures import URL, Headers, MutableHeaders
    from starlette.requests import Request

logger = get_logger(__name__)


# https://developer.mozilla.org/en-US/docs/Glossary/Cacheable
CACHABLE_METHODS = frozenset(("GET", "HEAD"))
CACHABLE_STATUS_CODES = frozenset(
    (200, 203, 204, 206, 300, 301, 404, 405, 410, 414, 501)
)
ONE_YEAR = 60 * 60 * 24 * 365

INVALIDATING_METHODS = frozenset(("POST", "PUT", "PATCH", "DELETE"))


class CacheDirectives(typing.TypedDict, total=False):
    max_age: int
    s_maxage: int
    no_cache: bool
    no_store: bool
    no_transform: bool
    must_revalidate: bool
    proxy_revalidate: bool
    must_understand: bool
    private: bool
    public: bool
    immutable: bool
    stale_while_revalidate: int
    stale_if_error: int


async def store_in_cache(
    response: Response,
    *,
    request: Request,
    cache: BaseCache,
    rules: Sequence[Rule],
) -> None:
    """Given a response and a request, store the response in the cache for reuse.

    To do so, a cache key is built from:

    * The absolute URL (including query parameters)
    * Varying headers [^1], as specified specified in the "Vary" header of the response.
      These headers are stored at a key that depends only on the request URL, so that
      they can be retrieved (and checked against) for future requests (without having
      to build and read an uncached response first).

    [^1]: The "Vary" header lists which headers should be taken into account in cache
    systems, because they may result in the server sending in a different response.
    For example, gzip compression requires to add "Accept-Encoding" to "Vary" because
    sending "Accept-Encoding: gzip", and "Accept-Encoding: identity" will result in
    different responses.
    """
    if response.status_code not in CACHABLE_STATUS_CODES:
        logger.trace("response_not_cachable reason=status_code")
        raise ResponseNotCachable(response)

    if not request.cookies and "Set-Cookie" in response.headers:
        logger.trace("response_not_cachable reason=cookies_for_cookieless_request")
        raise ResponseNotCachable(response)

    rule = get_rule_matching_response(rules, request=request, response=response)
    if not rule:
        logger.trace("response_not_cachable reason=rule")
        raise ResponseNotCachable(response)

    ttl = rule.ttl if rule.ttl is not None else cache.ttl

    if ttl == 0:
        logger.trace("response_not_cachable reason=zero_ttl")
        raise ResponseNotCachable(response)

    if ttl is None:
        # From section 14.12 of RFC2616:
        # "HTTP/1.1 servers SHOULD NOT send Expires dates more than
        # one year in the future."
        max_age = ONE_YEAR
        logger.trace(f"max_out_ttl value={max_age!r}")
    else:
        max_age = int(ttl)

    logger.debug(f"store_in_cache max_age={max_age!r}")

    # Store the cached response as a hit. The current request will have it
    # set to miss before returning the response to the client. Future requests
    # will load from the cache, and have it set to hit.
    response.headers["X-Cache"] = "hit"

    cache_headers = get_cache_response_headers(response, max_age=max_age)
    logger.trace(f"patch_response_headers headers={cache_headers!r}")
    response.headers.update(cache_headers)

    cache_key = await learn_cache_key(request, response, cache=cache)
    logger.trace(f"learnt_cache_key cache_key={cache_key!r}")
    serialized_response = serialize_response(response)
    logger.trace(
        f"store_response_in_cache key={cache_key!r} value={serialized_response!r}"
    )
    kwargs = {}
    if ttl is not None:
        kwargs["ttl"] = ttl

    await cache.set(key=cache_key, value=serialized_response, **kwargs)

    # Set X-Cache header to miss for the current request. The next request will
    # load from the cache and have the X-Cache header set to hit.
    response.headers["X-Cache"] = "miss"


async def get_from_cache(
    request: Request, *, cache: BaseCache, rules: Sequence[Rule]
) -> Response | None:
    """Retrieve a cached response based on the cache key associated to the request.

    If no cache key is present yet, or if there is no cached response at
    that key, return `None`.

    A `None` return value indicates that the response for this
    request can (and should) be added to the cache once computed.
    """
    logger.trace(
        f"get_from_cache "
        f"request.url={str(request.url)!r} "
        f"request.method={request.method!r}"
    )
    if request.method not in CACHABLE_METHODS:
        logger.trace("request_not_cachable reason=method")
        raise RequestNotCachable(request)

    rule = get_rule_matching_request(rules, request=request)
    if rule is None:
        logger.trace("request_not_cachable reason=rule")
        raise RequestNotCachable(request)

    logger.trace("lookup_cached_response method='GET'")
    # Try to retrieve the cached GET response (even if this is a HEAD request).
    cache_key = await get_cache_key(request, method="GET", cache=cache)
    if cache_key is None:
        logger.trace("cache_key found=False")
        return None
    logger.trace(f"cache_key found=True cache_key={cache_key!r}")
    serialized_response: dict | None = await cache.get(cache_key)

    # If not present, fallback to look for a cached HEAD response.
    if serialized_response is None:
        logger.trace("lookup_cached_response method='HEAD'")
        cache_key = await get_cache_key(request, method="HEAD", cache=cache)
        assert cache_key is not None
        logger.trace(f"cache_key found=True cache_key={cache_key!r}")
        serialized_response = await cache.get(cache_key)

    if serialized_response is None:
        logger.trace("cached_response found=False")
        return None

    logger.trace(
        f"cached_response found=True key={cache_key!r} value={serialized_response!r}"
    )
    return deserialize_response(serialized_response)


async def delete_from_cache(url: URL, *, vary: Headers, cache: BaseCache) -> None:
    """Clear the cache for the given request."""
    varying_headers_cache_key = generate_varying_headers_cache_key(url, cache=cache)
    varying_headers = await cache.get(varying_headers_cache_key)
    if varying_headers is None:
        # Nothing to do, as there's no cache key associated to this URL.
        return

    for method in "GET", "HEAD":
        cache_key = generate_cache_key(
            url,
            method=method,
            headers=vary,
            varying_headers=varying_headers,
            cache=cache,
        )

        logger.trace(f"clear_cache key={cache_key!r}")
        await cache.delete(cache_key)

    await cache.delete(varying_headers_cache_key)


def serialize_response(response: Response) -> dict:
    """Convert a response to JSON format.

    (This is required as `aiocache` dumps values to JSON before storing them
    in the cache system by default.)
    """
    return {
        "content": bytes_to_json_string(response.body),
        "status_code": response.status_code,
        "headers": dict(response.headers),
    }


def deserialize_response(serialized_response: dict) -> Response:
    """Re-build the original response object from a json-serialized object."""
    return Response(
        content=json_string_to_bytes(serialized_response["content"]),
        status_code=serialized_response["status_code"],
        headers=serialized_response["headers"],
    )


async def learn_cache_key(
    request: Request, response: Response, *, cache: BaseCache
) -> str:
    """Generate a cache key from the requested absolute URL.

    Varying response headers are stored at another key based from the
    requested absolute URL.
    """
    logger.trace(
        "learn_cache_key "
        f"request.method={request.method!r} "
        f"response.headers.Vary={response.headers.get('Vary')!r}"
    )
    url = request.url
    varying_headers_cache_key = generate_varying_headers_cache_key(url, cache=cache)

    cached_vary_headers = set(await cache.get(key=varying_headers_cache_key) or ())
    response_vary_headers = {
        header.lower() for header in parse_http_list(response.headers.get("Vary", ""))
    }

    # workaround for when a route doesn't always add a Vary header
    # Caveat: only effective when a varied requested is sent first
    varying_headers = sorted(response_vary_headers | cached_vary_headers)
    if varying_headers:
        response.headers["Vary"] = ", ".join(varying_headers)

    logger.trace(
        "store_varying_headers "
        f"cache_key={varying_headers_cache_key!r} headers={varying_headers!r}"
    )
    await cache.set(key=varying_headers_cache_key, value=varying_headers)

    return generate_cache_key(
        url,
        method=request.method,
        headers=request.headers,
        varying_headers=varying_headers,
        cache=cache,
    )


async def get_cache_key(request: Request, method: str, cache: BaseCache) -> str | None:
    """Return the cache key where a cached response should be looked up.

    If this request hasn't been served before, return `None` as there definitely
    won't be any matching cached response.
    """
    url = request.url
    logger.trace(f"get_cache_key request.url={str(url)!r} method={method!r}")
    varying_headers_cache_key = generate_varying_headers_cache_key(url, cache=cache)
    varying_headers = await cache.get(varying_headers_cache_key)

    if varying_headers is None:
        logger.trace("varying_headers found=False")
        return None
    logger.trace(f"varying_headers found=True headers={varying_headers!r}")

    return generate_cache_key(
        request.url,
        method=method,
        headers=request.headers,
        varying_headers=varying_headers,
        cache=cache,
    )


def generate_cache_key(
    url: URL,
    method: str,
    headers: Headers,
    varying_headers: list[str],
    cache: BaseCache,
) -> str:
    """Generate a cache key from the request full URL and varying response headers.

    Note that the given `method` may be different from that of the request, e.g.
    because we're trying to find a response cached from a previous GET request
    while this one is a HEAD request. (This is OK because web servers will strip content
    from responses to a HEAD request before sending them on the wire.)
    """
    assert method in CACHABLE_METHODS

    ctx = hashlib.md5(usedforsecurity=False)
    for header in varying_headers:
        value = headers.get(header)
        if value is not None:
            ctx.update(value.encode())
    vary_hash = ctx.hexdigest()

    url_hash = hashlib.md5(str(url).encode("ascii"), usedforsecurity=False).hexdigest()

    return f"cache_page.{method}.{url_hash}.{vary_hash}"


def generate_varying_headers_cache_key(url: URL, cache: BaseCache) -> str:
    """Generate a cache key from the requested absolute URL.

    Suitable for associating varying headers to a requested URL.
    """
    url_hash = hashlib.md5(str(url.path).encode("ascii"), usedforsecurity=False)
    return f"varying_headers.{url_hash.hexdigest()}"


def get_cache_response_headers(response: Response, *, max_age: int) -> dict[str, str]:
    """Return caching-related headers to add to a response."""
    assert max_age >= 0, "Can't have a negative cache max-age"
    headers = {}

    if "Expires" not in response.headers:
        headers["Expires"] = http_date(time.time() + max_age)

    patch_cache_control(response.headers, max_age=max_age)

    return headers


def patch_cache_control(
    headers: MutableHeaders, **kwargs: typing.Unpack[CacheDirectives]
) -> None:
    """Patch headers with an extended version of the initial Cache-Control header.

    Appends all keyword arguments to the Cache-Control header.

    True values are added as flags, while false values are omitted.
    """
    cache_control: dict[str, typing.Any] = {}
    value: typing.Any
    for field in parse_http_list(headers.get("Cache-Control", "")):
        try:
            key, value = field.split("=")
        except ValueError:  # noqa: PERF203
            cache_control[field] = True
        else:
            cache_control[key] = value

    if "max-age" in cache_control and "max_age" in kwargs:
        kwargs["max_age"] = min(int(cache_control["max-age"]), kwargs["max_age"])

    if "public" in kwargs:
        raise NotImplementedError(
            "The 'public' cache control directive isn't supported yet."
        )

    if "private" in kwargs:
        raise NotImplementedError(
            "The 'private' cache control directive isn't supported yet."
        )

    for key, value in kwargs.items():
        key = key.replace("_", "-")
        cache_control[key] = value

    directives: list[str] = []
    for key, value in cache_control.items():
        if value is False:
            continue
        if value is True:
            directives.append(key)
        else:
            directives.append(f"{key}={value}")

    patched_cache_control = ", ".join(directives)

    if patched_cache_control:
        headers["Cache-Control"] = patched_cache_control
    else:
        del headers["Cache-Control"]
