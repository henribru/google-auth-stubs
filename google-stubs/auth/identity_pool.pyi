from _typeshed import Incomplete

from google.auth import exceptions as exceptions, external_account as external_account

class Credentials(external_account.Credentials):
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
    def retrieve_subject_token(self, request): ...
    @classmethod
    def from_info(cls, info, **kwargs): ...
    @classmethod
    def from_file(cls, filename, **kwargs): ...
