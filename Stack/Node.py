from abc import ABC, abstractmethod


class NodeBase(ABC):
    @abstractmethod
    def __init__(self, e, next) -> None:
        self.element = e
        self.next = next
