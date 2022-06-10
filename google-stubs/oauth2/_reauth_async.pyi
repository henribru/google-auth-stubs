from _typeshed import Incomplete

from google.auth import exceptions as exceptions
from google.oauth2 import challenges as challenges, reauth as reauth

async def get_rapt_token(
    request,
    client_id,
    client_secret,
    refresh_token,
    token_uri,
    scopes: Incomplete | None = ...,
): ...
async def refresh_grant(
    request,
    token_uri,
    refresh_token,
    client_id,
    client_secret,
    scopes: Incomplete | None = ...,
    rapt_token: Incomplete | None = ...,
    enable_reauth_refresh: bool = ...,
): ...
