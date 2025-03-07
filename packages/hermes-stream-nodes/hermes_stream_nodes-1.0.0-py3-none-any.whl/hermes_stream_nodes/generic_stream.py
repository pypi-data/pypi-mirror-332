from abc import ABC, abstractmethod

from node_hermes_core.nodes import GenericNode, AsyncGenericNode


class GenericStreamTransport(GenericNode, ABC):
    @abstractmethod
    def read(self) -> bytes: ...

    @abstractmethod
    def write(self, data: bytes): ...


class AsyncGenericStreamTransport(AsyncGenericNode, ABC):
    @abstractmethod
    async def read(self) -> bytes: ...

    @abstractmethod
    async def write(self, data: bytes): ...
