from _typeshed import Incomplete

import google.auth.credentials
from google.auth import crypt as crypt, exceptions as exceptions
from google.auth.crypt import es256 as es256

def encode(
    signer, payload, header: Incomplete | None = ..., key_id: Incomplete | None = ...
): ...
def decode_header(token): ...
def decode(
    token,
    certs: Incomplete | None = ...,
    verify: bool = ...,
    audience: Incomplete | None = ...,
    clock_skew_in_seconds: int = ...,
): ...

class Credentials(
    google.auth.credentials.Signing, google.auth.credentials.CredentialsWithQuotaProject
):
    def __init__(
        self,
        signer,
        issuer,
        subject,
        audience,
        additional_claims: Incomplete | None = ...,
        token_lifetime=...,
        quota_project_id: Incomplete | None = ...,
    ) -> None: ...
    @classmethod
    def from_service_account_info(cls, info, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename, **kwargs): ...
    @classmethod
    def from_signing_credentials(cls, credentials, audience, **kwargs): ...
    def with_claims(
        self,
        issuer: Incomplete | None = ...,
        subject: Incomplete | None = ...,
        audience: Incomplete | None = ...,
        additional_claims: Incomplete | None = ...,
    ): ...
    def with_quota_project(self, quota_project_id): ...
    def refresh(self, request) -> None: ...
    def sign_bytes(self, message): ...
    @property
    def signer_email(self): ...
    @property
    def signer(self): ...

class OnDemandCredentials(
    google.auth.credentials.Signing, google.auth.credentials.CredentialsWithQuotaProject
):
    def __init__(
        self,
        signer,
        issuer,
        subject,
        additional_claims: Incomplete | None = ...,
        token_lifetime=...,
        max_cache_size=...,
        quota_project_id: Incomplete | None = ...,
    ) -> None: ...
    @classmethod
    def from_service_account_info(cls, info, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename, **kwargs): ...
    @classmethod
    def from_signing_credentials(cls, credentials, **kwargs): ...
    def with_claims(
        self,
        issuer: Incomplete | None = ...,
        subject: Incomplete | None = ...,
        additional_claims: Incomplete | None = ...,
    ): ...
    def with_quota_project(self, quota_project_id): ...
    @property
    def valid(self): ...
    def refresh(self, request) -> None: ...
    def before_request(self, request, method, url, headers) -> None: ...
    def sign_bytes(self, message): ...
    @property
    def signer_email(self): ...
    @property
    def signer(self): ...
