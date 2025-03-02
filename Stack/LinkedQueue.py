# 队列


from Stack.Node import NodeBase


class LinkedQueue:
    class Node(NodeBase):
        def __init__(self, e, next: NodeBase) -> None:
            self.element = e
            self.next = next

    def __init__(self, head, tail) -> None:
        self.head = head
        self.tail = tail
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("queue is empty")

        return self.head.element

    def dequeue(self):
        if self.is_empty():
            raise ValueError("queue is empty")
        res = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return res

    def enqueue(self, e):
        nd = self.Node(e, None)
        if self.is_empty():
            self.head = nd
        else:
            self.tail.next = nd
        self.tail = nd
        self.size += 1
