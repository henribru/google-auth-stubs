from typing import Any

import grpc

from google.auth import environment_vars as environment_vars, exceptions as exceptions
from google.oauth2 import service_account as service_account

new_exc: Any

class AuthMetadataPlugin(grpc.AuthMetadataPlugin):
    def __init__(
        self, credentials, request, default_host: Any | None = ...
    ) -> None: ...
    def __call__(self, context, callback) -> None: ...

def secure_authorized_channel(
    credentials,
    request,
    target,
    ssl_credentials: Any | None = ...,
    client_cert_callback: Any | None = ...,
    **kwargs
): ...

class SslCredentials:
    def __init__(self) -> None: ...
    @property
    def ssl_credentials(self): ...
    @property
    def is_mtls(self): ...
