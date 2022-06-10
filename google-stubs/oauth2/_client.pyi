from _typeshed import Incomplete

from google.auth import exceptions as exceptions, jwt as jwt

def jwt_grant(request, token_uri, assertion): ...
def id_token_jwt_grant(request, token_uri, assertion): ...
def refresh_grant(
    request,
    token_uri,
    refresh_token,
    client_id,
    client_secret,
    scopes: Incomplete | None = ...,
    rapt_token: Incomplete | None = ...,
): ...
