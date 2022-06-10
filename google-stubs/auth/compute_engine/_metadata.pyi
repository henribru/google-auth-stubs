from _typeshed import Incomplete

from google.auth import environment_vars as environment_vars, exceptions as exceptions

def ping(request, timeout=..., retry_count: int = ...): ...
def get(
    request,
    path,
    root=...,
    params: Incomplete | None = ...,
    recursive: bool = ...,
    retry_count: int = ...,
): ...
def get_project_id(request): ...
def get_service_account_info(request, service_account: str = ...): ...
def get_service_account_token(
    request, service_account: str = ..., scopes: Incomplete | None = ...
): ...
