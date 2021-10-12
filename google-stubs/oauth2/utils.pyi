import abc
import enum
from typing import Any

from google.auth import exceptions as exceptions

class ClientAuthType(enum.Enum):
    basic: int
    request_body: int

class ClientAuthentication:
    client_auth_type: Any
    client_id: Any
    client_secret: Any
    def __init__(
        self, client_auth_type, client_id, client_secret: Any | None = ...
    ) -> None: ...

class OAuthClientAuthHandler(metaclass=abc.ABCMeta):
    def __init__(self, client_authentication: Any | None = ...) -> None: ...
    def apply_client_authentication_options(
        self, headers, request_body: Any | None = ..., bearer_token: Any | None = ...
    ) -> None: ...

def handle_error_response(response_body) -> None: ...
