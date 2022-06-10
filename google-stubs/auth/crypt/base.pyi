import abc

from _typeshed import Incomplete

class Verifier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def verify(self, message, signature): ...

class Signer(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def key_id(self): ...
    @abc.abstractmethod
    def sign(self, message): ...

class FromServiceAccountMixin(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def from_string(cls, key, key_id: Incomplete | None = ...): ...
    @classmethod
    def from_service_account_info(cls, info): ...
    @classmethod
    def from_service_account_file(cls, filename): ...
