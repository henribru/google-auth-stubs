from typing import Mapping

from _typeshed import Incomplete

from google.auth import credentials as credentials, jwt as jwt

class Credentials(
    credentials.Signing, credentials.Scoped, credentials.CredentialsWithQuotaProject
):
    def __init__(
        self,
        signer,
        service_account_email,
        token_uri,
        scopes: Incomplete | None = ...,
        default_scopes: Incomplete | None = ...,
        subject: Incomplete | None = ...,
        project_id: Incomplete | None = ...,
        quota_project_id: Incomplete | None = ...,
        additional_claims: Incomplete | None = ...,
        always_use_jwt_access: bool = ...,
    ) -> None: ...
    @classmethod
    def from_service_account_info(
        cls,
        info: Mapping[str, str],
        *,
        scopes: Incomplete | None = ...,
        default_scopes: Incomplete | None = ...,
        subject: Incomplete | None = ...,
        quota_project_id: Incomplete | None = ...,
        additional_claims: Incomplete | None = ...,
        always_use_jwt_access: bool = ...,
    ) -> Credentials: ...
    @classmethod
    def from_service_account_file(
        cls,
        filename: str,
        *,
        scopes: Incomplete | None = ...,
        default_scopes: Incomplete | None = ...,
        subject: Incomplete | None = ...,
        quota_project_id: Incomplete | None = ...,
        additional_claims: Incomplete | None = ...,
        always_use_jwt_access: bool = ...,
    ) -> Credentials: ...
    @property
    def service_account_email(self): ...
    @property
    def project_id(self): ...
    @property
    def requires_scopes(self): ...
    def with_scopes(self, scopes, default_scopes: Incomplete | None = ...): ...
    def with_always_use_jwt_access(self, always_use_jwt_access): ...
    def with_subject(self, subject): ...
    def with_claims(self, additional_claims): ...
    def with_quota_project(self, quota_project_id): ...
    token: Incomplete
    expiry: Incomplete
    def refresh(self, request) -> None: ...
    def sign_bytes(self, message): ...
    @property
    def signer(self): ...
    @property
    def signer_email(self): ...

class IDTokenCredentials(credentials.Signing, credentials.CredentialsWithQuotaProject):
    def __init__(
        self,
        signer,
        service_account_email,
        token_uri,
        target_audience,
        additional_claims: Incomplete | None = ...,
        quota_project_id: Incomplete | None = ...,
    ) -> None: ...
    @classmethod
    def from_service_account_info(
        cls,
        info: Mapping[str, str],
        *,
        service_account_email=...,
        token_uri=...,
        target_audience,
        additional_claims: Incomplete | None = ...,
        quota_project_id: Incomplete | None = ...,
    ) -> IDTokenCredentials: ...
    @classmethod
    def from_service_account_file(
        cls,
        filename: str,
        *,
        service_account_email=...,
        token_uri=...,
        target_audience,
        additional_claims: Incomplete | None = ...,
        quota_project_id: Incomplete | None = ...,
    ) -> IDTokenCredentials: ...
    def with_target_audience(self, target_audience): ...
    def with_quota_project(self, quota_project_id): ...
    token: Incomplete
    expiry: Incomplete
    def refresh(self, request) -> None: ...
    @property
    def service_account_email(self): ...
    def sign_bytes(self, message): ...
    @property
    def signer(self): ...
    @property
    def signer_email(self): ...
