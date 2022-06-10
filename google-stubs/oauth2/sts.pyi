from _typeshed import Incomplete

from google.oauth2 import utils as utils

class Client(utils.OAuthClientAuthHandler):
    def __init__(
        self, token_exchange_endpoint, client_authentication: Incomplete | None = ...
    ) -> None: ...
    def exchange_token(
        self,
        request,
        grant_type,
        subject_token,
        subject_token_type,
        resource: Incomplete | None = ...,
        audience: Incomplete | None = ...,
        scopes: Incomplete | None = ...,
        requested_token_type: Incomplete | None = ...,
        actor_token: Incomplete | None = ...,
        actor_token_type: Incomplete | None = ...,
        additional_options: Incomplete | None = ...,
        additional_headers: Incomplete | None = ...,
    ): ...
