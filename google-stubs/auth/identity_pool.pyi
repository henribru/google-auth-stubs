from typing import Any

from google.auth import exceptions as exceptions, external_account as external_account

class Credentials(external_account.Credentials):
    def __init__(
        self,
        audience,
        subject_token_type,
        token_url,
        credential_source,
        service_account_impersonation_url: Any | None = ...,
        client_id: Any | None = ...,
        client_secret: Any | None = ...,
        quota_project_id: Any | None = ...,
        scopes: Any | None = ...,
        default_scopes: Any | None = ...,
        workforce_pool_user_project: Any | None = ...,
    ) -> None: ...
    def retrieve_subject_token(self, request): ...
    @classmethod
    def from_info(cls, info, **kwargs): ...
    @classmethod
    def from_file(cls, filename, **kwargs): ...
