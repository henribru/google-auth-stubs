import abc

from _typeshed import Incomplete

from google.auth import (
    credentials as credentials,
    exceptions as exceptions,
    impersonated_credentials as impersonated_credentials,
)
from google.oauth2 import sts as sts, utils as utils

class Credentials(
    credentials.Scoped, credentials.CredentialsWithQuotaProject, metaclass=abc.ABCMeta
):
    def __init__(
        self,
        audience,
        subject_token_type,
        token_url,
        credential_source,
        service_account_impersonation_url: Incomplete | None = ...,
        client_id: Incomplete | None = ...,
        client_secret: Incomplete | None = ...,
        quota_project_id: Incomplete | None = ...,
        scopes: Incomplete | None = ...,
        default_scopes: Incomplete | None = ...,
        workforce_pool_user_project: Incomplete | None = ...,
    ) -> None: ...
    @property
    def info(self): ...
    @property
    def service_account_email(self): ...
    @property
    def is_user(self): ...
    @property
    def is_workforce_pool(self): ...
    @property
    def requires_scopes(self): ...
    @property
    def project_number(self): ...
    def with_scopes(self, scopes, default_scopes: Incomplete | None = ...): ...
    @abc.abstractmethod
    def retrieve_subject_token(self, request): ...
    def get_project_id(self, request): ...
    token: Incomplete
    expiry: Incomplete
    def refresh(self, request) -> None: ...
    def with_quota_project(self, quota_project_id): ...
    @staticmethod
    def validate_token_url(token_url) -> None: ...
    @staticmethod
    def validate_service_account_impersonation_url(url) -> None: ...
    @staticmethod
    def is_valid_url(patterns, url): ...
