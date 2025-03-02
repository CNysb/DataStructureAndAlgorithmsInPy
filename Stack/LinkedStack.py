# 栈


class LinkedStack:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    class Node:
        def __init__(self, element, next) -> None:
            self.element = element
            self.next = next

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        return self.head.element

    def pop(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        res = self.head.element
        self.head = self.head.next
        self.size -= 1
        return res
