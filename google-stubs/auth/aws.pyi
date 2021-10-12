from typing import Any

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
        credential_source: Any | None = ...,
        service_account_impersonation_url: Any | None = ...,
        client_id: Any | None = ...,
        client_secret: Any | None = ...,
        quota_project_id: Any | None = ...,
        scopes: Any | None = ...,
        default_scopes: Any | None = ...,
    ) -> None: ...
    def retrieve_subject_token(self, request): ...
    @classmethod
    def from_info(cls, info, **kwargs): ...
    @classmethod
    def from_file(cls, filename, **kwargs): ...
