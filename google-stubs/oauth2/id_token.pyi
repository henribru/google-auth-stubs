from _typeshed import Incomplete

from google.auth import (
    environment_vars as environment_vars,
    exceptions as exceptions,
    jwt as jwt,
    transport
)

from typing import Any, Mapping, Union

def verify_token(
    id_token: str | bytes,
    request: transport.Request,
    audience: str | list[str] | None = ...,
    certs_url: str = ...,
    clock_skew_in_seconds: int = ...,
) -> Mapping[str, Any]: ...
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
