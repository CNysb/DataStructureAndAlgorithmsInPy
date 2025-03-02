from abc import ABC, abstractmethod
from typing import Optional


class NodeBase(ABC):
    @abstractmethod
    def __init__(self, e, next) -> None:
        self.element = e
        self.next = next
