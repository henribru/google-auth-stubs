from _typeshed import Incomplete

from google.auth import (
    environment_vars as environment_vars,
    exceptions as exceptions,
    external_account as external_account,
)

class RequestSigner:
    def __init__(self, region_name) -> None: ...
    def get_request_options(
        self,
        aws_security_credentials,
        url,
        method,
        request_payload: str = ...,
        additional_headers=...,
    ): ...

class Credentials(external_account.Credentials):
    def __init__(
        self,
        audience,
        subject_token_type,
        token_url,
        credential_source: Incomplete | None = ...,
        service_account_impersonation_url: Incomplete | None = ...,
        client_id: Incomplete | None = ...,
        client_secret: Incomplete | None = ...,
        quota_project_id: Incomplete | None = ...,
        scopes: Incomplete | None = ...,
        default_scopes: Incomplete | None = ...,
    ) -> None: ...
    def retrieve_subject_token(self, request): ...
    @classmethod
    def from_info(cls, info, **kwargs): ...
    @classmethod
    def from_file(cls, filename, **kwargs): ...
