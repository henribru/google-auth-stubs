from typing import Any

from google.oauth2 import utils as utils

class Client(utils.OAuthClientAuthHandler):
    def __init__(
        self, token_exchange_endpoint, client_authentication: Any | None = ...
    ) -> None: ...
    def exchange_token(
        self,
        request,
        grant_type,
        subject_token,
        subject_token_type,
        resource: Any | None = ...,
        audience: Any | None = ...,
        scopes: Any | None = ...,
        requested_token_type: Any | None = ...,
        actor_token: Any | None = ...,
        actor_token_type: Any | None = ...,
        additional_options: Any | None = ...,
        additional_headers: Any | None = ...,
    ): ...
