from _typeshed import Incomplete

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
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        timeout: Incomplete | None = ...,
        **kwargs
    ): ...
