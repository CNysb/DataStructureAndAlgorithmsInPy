from typing import Optional


from Stack.Node import NodeBase


class CircularQueue:
    def __init__(self) -> None:
        self.tail: Optional[NodeBase] = None
        self.size = 0

    class Node(NodeBase):
        def __init__(self, element, next: NodeBase) -> None:
            self.element = element
            self.next = next

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        head = self.tail.next
        return head.element

    def dequeue(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        old_head = self.tail.next
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = old_head.next
        self.size -= 1
        return old_head.element

    def enqueue(self, e):
        nd = self.Node(e, None)
        if self.is_empty():
            nd.next = nd
        else:
            nd.next = self.tail.next
            self.tail.next = nd

        self.tail = nd
        self.size += 1

    def rotate(self):
        if self.size > 1:
            self.tail = self.tail.next
