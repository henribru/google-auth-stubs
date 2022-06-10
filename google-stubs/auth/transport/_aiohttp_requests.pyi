import aiohttp  # type: ignore[import]
from _typeshed import Incomplete

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
    session: Incomplete
    def __init__(self, session: Incomplete | None = ...) -> None: ...
    async def __call__(
        self,
        url,
        method: str = ...,
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        timeout=...,
        **kwargs
    ): ...

class AuthorizedSession(aiohttp.ClientSession):
    credentials: Incomplete
    def __init__(
        self,
        credentials,
        refresh_status_codes=...,
        max_refresh_attempts=...,
        refresh_timeout: Incomplete | None = ...,
        auth_request: Incomplete | None = ...,
        auto_decompress: bool = ...,
    ) -> None: ...
    async def request(
        self,
        method,
        url,
        data: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        max_allowed_time: Incomplete | None = ...,
        timeout=...,
        auto_decompress: bool = ...,
        **kwargs
    ): ...
