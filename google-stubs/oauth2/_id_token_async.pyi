from _typeshed import Incomplete

from google.auth import (
    environment_vars as environment_vars,
    exceptions as exceptions,
    jwt as jwt,
)
from google.auth.transport import requests as requests

async def verify_token(
    id_token,
    request,
    audience: Incomplete | None = ...,
    certs_url=...,
    clock_skew_in_seconds: int = ...,
): ...
async def verify_oauth2_token(
    id_token,
    request,
    audience: Incomplete | None = ...,
    clock_skew_in_seconds: int = ...,
): ...
async def verify_firebase_token(
    id_token,
    request,
    audience: Incomplete | None = ...,
    clock_skew_in_seconds: int = ...,
): ...
async def fetch_id_token(request, audience): ...
