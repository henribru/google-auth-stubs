from typing import Any

from google.auth import exceptions as exceptions, transport as transport

class Response(transport.Response):
    def __init__(self, response) -> None: ...
    @property
    def status(self): ...
    @property
    def headers(self): ...
    @property
    def data(self): ...

class Request(transport.Request):
    def __call__(
        self,
        url,
        method: str = ...,
        body: Any | None = ...,
        headers: Any | None = ...,
        timeout: Any | None = ...,
        **kwargs
    ): ...
