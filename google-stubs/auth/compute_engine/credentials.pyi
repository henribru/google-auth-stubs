from typing import Any

from google.auth import (
    credentials as credentials,
    exceptions as exceptions,
    iam as iam,
    jwt as jwt,
)

class Credentials(credentials.Scoped, credentials.CredentialsWithQuotaProject):
    def __init__(
        self,
        service_account_email: str = ...,
        quota_project_id: Any | None = ...,
        scopes: Any | None = ...,
        default_scopes: Any | None = ...,
    ) -> None: ...
    def refresh(self, request) -> None: ...
    @property
    def service_account_email(self): ...
    @property
    def requires_scopes(self): ...
    def with_quota_project(self, quota_project_id): ...
    def with_scopes(self, scopes, default_scopes: Any | None = ...): ...

class IDTokenCredentials(credentials.CredentialsWithQuotaProject, credentials.Signing):
    def __init__(
        self,
        request,
        target_audience,
        token_uri: Any | None = ...,
        additional_claims: Any | None = ...,
        service_account_email: Any | None = ...,
        signer: Any | None = ...,
        use_metadata_identity_endpoint: bool = ...,
        quota_project_id: Any | None = ...,
    ) -> None: ...
    def with_target_audience(self, target_audience): ...
    def with_quota_project(self, quota_project_id): ...
    token: Any
    expiry: Any
    def refresh(self, request) -> None: ...
    @property
    def signer(self): ...
    def sign_bytes(self, message): ...
    @property
    def service_account_email(self): ...
    @property
    def signer_email(self): ...
