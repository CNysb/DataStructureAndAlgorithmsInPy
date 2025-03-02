# 队列


class LinkedQueue:
    class Node:
        def __init__(self, e, next) -> None:
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
