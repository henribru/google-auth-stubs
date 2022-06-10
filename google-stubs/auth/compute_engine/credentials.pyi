from _typeshed import Incomplete

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
        quota_project_id: Incomplete | None = ...,
        scopes: Incomplete | None = ...,
        default_scopes: Incomplete | None = ...,
    ) -> None: ...
    def refresh(self, request) -> None: ...
    @property
    def service_account_email(self): ...
    @property
    def requires_scopes(self): ...
    def with_quota_project(self, quota_project_id): ...
    def with_scopes(self, scopes, default_scopes: Incomplete | None = ...): ...

class IDTokenCredentials(credentials.CredentialsWithQuotaProject, credentials.Signing):
    def __init__(
        self,
        request,
        target_audience,
        token_uri: Incomplete | None = ...,
        additional_claims: Incomplete | None = ...,
        service_account_email: Incomplete | None = ...,
        signer: Incomplete | None = ...,
        use_metadata_identity_endpoint: bool = ...,
        quota_project_id: Incomplete | None = ...,
    ) -> None: ...
    def with_target_audience(self, target_audience): ...
    def with_quota_project(self, quota_project_id): ...
    token: Incomplete
    expiry: Incomplete
    def refresh(self, request) -> None: ...
    @property
    def signer(self): ...
    def sign_bytes(self, message): ...
    @property
    def service_account_email(self): ...
    @property
    def signer_email(self): ...
