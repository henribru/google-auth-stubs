from _typeshed import Incomplete

from google.auth import _credentials_async, jwt as jwt

def encode(
    signer, payload, header: Incomplete | None = ..., key_id: Incomplete | None = ...
): ...
def decode(
    token,
    certs: Incomplete | None = ...,
    verify: bool = ...,
    audience: Incomplete | None = ...,
): ...

class Credentials(
    jwt.Credentials, _credentials_async.Signing, _credentials_async.Credentials
): ...
class OnDemandCredentials(  # type: ignore
    jwt.OnDemandCredentials, _credentials_async.Signing, _credentials_async.Credentials
): ...
