import requests.exceptions
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

class TimeoutGuard:
    remaining_timeout: Incomplete
    def __init__(self, timeout, timeout_error_type=...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

class Request(transport.Request):
    session: Incomplete
    def __init__(self, session: requests.Session | None = ...) -> None: ...
    def __del__(self) -> None: ...
    def __call__(
        self,
        url,
        method: str = ...,
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        timeout=...,
        **kwargs
    ): ...

class _MutualTlsAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, cert, key) -> None: ...
    def init_poolmanager(self, *args, **kwargs) -> None: ...
    def proxy_manager_for(self, *args, **kwargs): ...

class _MutualTlsOffloadAdapter(requests.adapters.HTTPAdapter):
    signer: Incomplete
    def __init__(self, enterprise_cert_file_path) -> None: ...
    def init_poolmanager(self, *args, **kwargs) -> None: ...
    def proxy_manager_for(self, *args, **kwargs): ...

class AuthorizedSession(requests.Session):
    credentials: Incomplete
    def __init__(
        self,
        credentials,
        refresh_status_codes=...,
        max_refresh_attempts=...,
        refresh_timeout: Incomplete | None = ...,
        auth_request: Incomplete | None = ...,
        default_host: Incomplete | None = ...,
    ) -> None: ...
    def configure_mtls_channel(
        self, client_cert_callback: Incomplete | None = ...
    ) -> None: ...
    def request(  # type: ignore[override]
        self,
        method,
        url,
        data: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        max_allowed_time: Incomplete | None = ...,
        timeout=...,
        **kwargs
    ): ...
    @property
    def is_mtls(self): ...
    def close(self) -> None: ...
