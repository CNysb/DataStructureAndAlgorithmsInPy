class DoubleLinkedBase:
    def __init__(self) -> None:
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, e, predecessor, successor):
        nd = self.Node(e, predecessor, successor)
        predecessor.next = nd
        successor.prev = nd
        self.size += 1
        return nd

    def delete_node(self, node):
        pre_nd = node.prev
        next_nd = node.next
        pre_nd.next = next_nd
        next_nd.prev = pre_nd
        self.size -= 1
        res = node.element
        node.prev = node.next = node.element = None
        return res

    class Node:
        def __init__(self, element, prev, next) -> None:
            self.element = element
            self.prev = prev
            self.next = next
