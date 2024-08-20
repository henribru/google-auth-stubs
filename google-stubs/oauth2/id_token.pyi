from _typeshed import Incomplete

from google.auth import (
    environment_vars as environment_vars,
    exceptions as exceptions,
    jwt as jwt,
)

from typing import Union

def verify_token(
    id_token: Union[str, bytes],
    request: transport.Request,
    audience: str | list[str] | None = None,
    certs_url: str = _GOOGLE_OAUTH2_CERTS_URL,
    clock_skew_in_seconds: int = 0,
): ...
def verify_oauth2_token(
    id_token,
    request,
    audience: Incomplete | None = ...,
    clock_skew_in_seconds: int = ...,
): ...
def verify_firebase_token(
    id_token,
    request,
    audience: Incomplete | None = ...,
    clock_skew_in_seconds: int = ...,
): ...
def fetch_id_token_credentials(audience, request: Incomplete | None = ...): ...
def fetch_id_token(request, audience): ...
