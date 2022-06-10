import urllib3.exceptions  # type: ignore[import]
from _typeshed import Incomplete

from google.auth import (
    environment_vars as environment_vars,
    exceptions as exceptions,
    transport as transport,
)
from google.oauth2 import service_account as service_account

class _Response(transport.Response):
    def __init__(self, response) -> None: ...
    @property
    def status(self): ...
    @property
    def headers(self): ...
    @property
    def data(self): ...

class Request(transport.Request):
    http: Incomplete
    def __init__(self, http) -> None: ...
    def __call__(
        self,
        url,
        method: str = ...,
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        timeout: Incomplete | None = ...,
        **kwargs
    ): ...

class AuthorizedHttp(urllib3.request.RequestMethods):
    http: Incomplete
    credentials: Incomplete
    def __init__(
        self,
        credentials,
        http: Incomplete | None = ...,
        refresh_status_codes=...,
        max_refresh_attempts=...,
        default_host: Incomplete | None = ...,
    ) -> None: ...
    def configure_mtls_channel(self, client_cert_callback: Incomplete | None = ...): ...
    def urlopen(  # type: ignore[override]
        self,
        method,
        url,
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        **kwargs
    ): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...
    def __del__(self) -> None: ...
    @property
    def headers(self): ...
    @headers.setter
    def headers(self, value) -> None: ...
