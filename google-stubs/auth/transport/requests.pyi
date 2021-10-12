from typing import Any

import requests.exceptions

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

class TimeoutGuard:
    remaining_timeout: Any
    def __init__(self, timeout, timeout_error_type=...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

class Request(transport.Request):
    session: Any
    def __init__(self, session: Any | None = ...) -> None: ...
    def __call__(
        self,
        url,
        method: str = ...,
        body: Any | None = ...,
        headers: Any | None = ...,
        timeout=...,
        **kwargs
    ): ...

class _MutualTlsAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, cert, key) -> None: ...
    def init_poolmanager(self, *args, **kwargs) -> None: ...
    def proxy_manager_for(self, *args, **kwargs): ...

class AuthorizedSession(requests.Session):
    credentials: Any
    def __init__(
        self,
        credentials,
        refresh_status_codes=...,
        max_refresh_attempts=...,
        refresh_timeout: Any | None = ...,
        auth_request: Any | None = ...,
        default_host: Any | None = ...,
    ) -> None: ...
    def configure_mtls_channel(
        self, client_cert_callback: Any | None = ...
    ) -> None: ...
    def request(  # type: ignore[override]
        self,
        method,
        url,
        data: Any | None = ...,
        headers: Any | None = ...,
        max_allowed_time: Any | None = ...,
        timeout=...,
        **kwargs
    ): ...
    @property
    def is_mtls(self): ...
    def close(self) -> None: ...
