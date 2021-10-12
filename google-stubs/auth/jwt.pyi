from typing import Any

import google.auth.credentials
from google.auth import crypt as crypt, exceptions as exceptions
from google.auth.crypt import es256 as es256

def encode(signer, payload, header: Any | None = ..., key_id: Any | None = ...): ...
def decode_header(token): ...
def decode(
    token,
    certs: Any | None = ...,
    verify: bool = ...,
    audience: Any | None = ...,
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
        additional_claims: Any | None = ...,
        token_lifetime=...,
        quota_project_id: Any | None = ...,
    ) -> None: ...
    @classmethod
    def from_service_account_info(cls, info, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename, **kwargs): ...
    @classmethod
    def from_signing_credentials(cls, credentials, audience, **kwargs): ...
    def with_claims(
        self,
        issuer: Any | None = ...,
        subject: Any | None = ...,
        audience: Any | None = ...,
        additional_claims: Any | None = ...,
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
        additional_claims: Any | None = ...,
        token_lifetime=...,
        max_cache_size=...,
        quota_project_id: Any | None = ...,
    ) -> None: ...
    @classmethod
    def from_service_account_info(cls, info, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename, **kwargs): ...
    @classmethod
    def from_signing_credentials(cls, credentials, **kwargs): ...
    def with_claims(
        self,
        issuer: Any | None = ...,
        subject: Any | None = ...,
        additional_claims: Any | None = ...,
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
