import enum

from _typeshed import Incomplete

from google.auth import exceptions as exceptions

class ClientAuthType(enum.Enum):
    basic: int
    request_body: int

class ClientAuthentication:
    client_auth_type: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    def __init__(
        self, client_auth_type, client_id, client_secret: Incomplete | None = ...
    ) -> None: ...

class OAuthClientAuthHandler:
    def __init__(self, client_authentication: Incomplete | None = ...) -> None: ...
    def apply_client_authentication_options(
        self,
        headers,
        request_body: Incomplete | None = ...,
        bearer_token: Incomplete | None = ...,
    ) -> None: ...

def handle_error_response(response_body) -> None: ...
