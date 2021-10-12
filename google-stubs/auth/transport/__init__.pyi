import abc
from typing import Any

DEFAULT_REFRESH_STATUS_CODES: Any
DEFAULT_MAX_REFRESH_ATTEMPTS: int

class Response(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def status(self): ...
    @property
    @abc.abstractmethod
    def headers(self): ...
    @property
    @abc.abstractmethod
    def data(self): ...

class Request(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(
        self,
        url,
        method: str = ...,
        body: Any | None = ...,
        headers: Any | None = ...,
        timeout: Any | None = ...,
        **kwargs
    ): ...
