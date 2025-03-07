from abc import ABC, abstractmethod


class Handler(ABC):

    @property
    @abstractmethod
    def path(self) -> str:
        pass
