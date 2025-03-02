from Stack.PositionalList import PositionalList
from Stack.PriorityQueueBase import PriorityQueueBase


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self) -> None:
        self.data = PositionalList()

    def __len__(self):
        return len(self.data)

    def add(self, key, value):
        newest = self.Item(key, value)
        walk = self.data.last

        while walk is not None and newest < walk.element:
            walk = self.data.before(walk)
        if walk is None:
            self.data.add_first(newest)
        else:
            self.data.add_after(walk, newest)

    def min(self):
        if self.is_empty():
            raise ValueError("empty")
        p = self.data.first
        item = p.element
        return (item.key, item.value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError("empty")
        item = self.data.delete(self.data.first)
        return (item.key, item.value)
