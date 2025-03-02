from Stack.DoubleLinkedBase import DoubleLinkedBase


class LinkedDeque(DoubleLinkedBase):
    def first(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        return self.head.next.element

    def last(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        return self.tail.prev.element

    def insert_first(self, e):
        self.insert_between(e, self.head, self.head.next)

    def insert_last(self, e):
        self.insert_between(e, self.tail.prev, self.tail)

    def delete_first(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        return self.delete_node(self.head.next)

    def delete_last(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        return self.delete_node(self.tail.prev)
