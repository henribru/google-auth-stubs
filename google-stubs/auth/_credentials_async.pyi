import abc

from google.auth import credentials as credentials

class Credentials(credentials.Credentials, metaclass=abc.ABCMeta):
    async def before_request(self, request, method, url, headers) -> None: ...  # type: ignore[override]

class CredentialsWithQuotaProject(
    credentials.CredentialsWithQuotaProject, metaclass=abc.ABCMeta
): ...
class AnonymousCredentials(credentials.AnonymousCredentials, Credentials): ...  # type: ignore[misc]
class ReadOnlyScoped(credentials.ReadOnlyScoped, metaclass=abc.ABCMeta): ...
class Scoped(credentials.Scoped, metaclass=abc.ABCMeta): ...

def with_scopes_if_required(credentials, scopes): ...

class Signing(credentials.Signing, metaclass=abc.ABCMeta): ...
