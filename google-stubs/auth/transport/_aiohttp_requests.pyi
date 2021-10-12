from typing import Any

import aiohttp  # type: ignore[import]

from google.auth import exceptions as exceptions, transport as transport
from google.auth.transport import requests as requests

class _CombinedResponse(transport.Response):
    def __init__(self, response) -> None: ...
    @property
    def status(self): ...
    @property
    def headers(self): ...
    @property
    def data(self): ...
    async def raw_content(self): ...
    async def content(self): ...

class _Response(transport.Response):
    def __init__(self, response) -> None: ...
    @property
    def status(self): ...
    @property
    def headers(self): ...
    @property
    def data(self): ...

class Request(transport.Request):
    session: Any
    def __init__(self, session: Any | None = ...) -> None: ...
    async def __call__(
        self,
        url,
        method: str = ...,
        body: Any | None = ...,
        headers: Any | None = ...,
        timeout=...,
        **kwargs
    ): ...

class AuthorizedSession(aiohttp.ClientSession):
    credentials: Any
    def __init__(
        self,
        credentials,
        refresh_status_codes=...,
        max_refresh_attempts=...,
        refresh_timeout: Any | None = ...,
        auth_request: Any | None = ...,
        auto_decompress: bool = ...,
    ) -> None: ...
    async def request(
        self,
        method,
        url,
        data: Any | None = ...,
        headers: Any | None = ...,
        max_allowed_time: Any | None = ...,
        timeout=...,
        auto_decompress: bool = ...,
        **kwargs
    ): ...
