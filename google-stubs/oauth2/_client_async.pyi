from _typeshed import Incomplete

from google.auth import exceptions as exceptions, jwt as jwt

async def jwt_grant(request, token_uri, assertion): ...
async def id_token_jwt_grant(request, token_uri, assertion): ...
async def refresh_grant(
    request,
    token_uri,
    refresh_token,
    client_id,
    client_secret,
    scopes: Incomplete | None = ...,
    rapt_token: Incomplete | None = ...,
): ...
