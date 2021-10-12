from typing import Any

import google.auth
from google.auth import jwt as jwt

def encode(signer, payload, header: Any | None = ..., key_id: Any | None = ...): ...
def decode(
    token, certs: Any | None = ..., verify: bool = ..., audience: Any | None = ...
): ...

class Credentials(
    jwt.Credentials,
    google.auth._credentials_async.Signing,
    google.auth._credentials_async.Credentials,
): ...
class OnDemandCredentials(
    jwt.OnDemandCredentials,
    google.auth._credentials_async.Signing,
    google.auth._credentials_async.Credentials,
): ...
