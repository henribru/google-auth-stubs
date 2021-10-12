from typing import Any

import urllib3.exceptions  # type: ignore[import]

from google.auth import (
    environment_vars as environment_vars,
    exceptions as exceptions,
    transport as transport,
)
from google.oauth2 import service_account as service_account

new_exc: Any

class _Response(transport.Response):
    def __init__(self, response) -> None: ...
    @property
    def status(self): ...
    @property
    def headers(self): ...
    @property
    def data(self): ...

class Request(transport.Request):
    http: Any
    def __init__(self, http) -> None: ...
    def __call__(
        self,
        url,
        method: str = ...,
        body: Any | None = ...,
        headers: Any | None = ...,
        timeout: Any | None = ...,
        **kwargs
    ): ...

class AuthorizedHttp(urllib3.request.RequestMethods):
    http: Any
    credentials: Any
    def __init__(
        self,
        credentials,
        http: Any | None = ...,
        refresh_status_codes=...,
        max_refresh_attempts=...,
        default_host: Any | None = ...,
    ) -> None: ...
    def configure_mtls_channel(self, client_cert_callback: Any | None = ...): ...
    def urlopen(
        self, method, url, body: Any | None = ..., headers: Any | None = ..., **kwargs
    ): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...
    @property
    def headers(self): ...
    @headers.setter
    def headers(self, value) -> None: ...
