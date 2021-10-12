from typing import Any

from google.auth import environment_vars as environment_vars, exceptions as exceptions

def load_credentials_from_file(
    filename,
    scopes: Any | None = ...,
    default_scopes: Any | None = ...,
    quota_project_id: Any | None = ...,
    request: Any | None = ...,
): ...
def default(
    scopes: Any | None = ...,
    request: Any | None = ...,
    quota_project_id: Any | None = ...,
    default_scopes: Any | None = ...,
): ...
