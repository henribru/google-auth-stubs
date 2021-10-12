from typing import Any

from google.auth import exceptions as exceptions
from google.oauth2 import credentials as oauth2_credentials

class Credentials(oauth2_credentials.Credentials):
    token: Any
    expiry: Any
    async def refresh(self, request) -> None: ...  # type: ignore[override]

class UserAccessTokenCredentials(oauth2_credentials.UserAccessTokenCredentials): ...
