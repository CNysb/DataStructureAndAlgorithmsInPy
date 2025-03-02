from Stack.DoubleLinkedBase import DoubleLinkedBase


class PositionalList(DoubleLinkedBase):
    class Position:
        def __init__(self, container, node) -> None:
            self.container = container
            self.node = node

        @property
        def element(self):
            return self.node.element

        def __eq__(self, other) -> bool:
            return type(other) is type(self) and other.node.element is self.node.element

        def __ne__(self, other) -> bool:
            return not (self == other)

    def validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("type error")

        if p.container is not self:
            raise ValueError("p dont belong to this container")
        if p.node.next is None:
            raise ValueError("p is no longer valid")
        return p.node

    def make_position(self, node):
        if node is self.head or node is self.tail:
            return None
        return self.Position(self, node)

    @property
    def first(self):
        return self.make_position(self.head.next)

    @property
    def last(self):
        return self.make_position(self.tail.prev)

    def before(self, p):
        node = self.validate(p)
        return self.make_position(node.prev)

    def after(self, p):
        node = self.validate(p)
        return self.make_position(node.next)

    def __iter__(self):
        cursor = self.first
        while cursor is not None:
            yield cursor.element
            cursor = self.after(cursor)

    def insert_between(self, e, predecessor, successor):
        node = super().insert_between(e, predecessor, successor)
        return self.make_position(node)

    def add_first(self, e):
        return self.insert_between(e, self.head.prev, self.head.next)

    def add_last(self, e):
        return self.insert_between(e, self.tail.prev, self.tail)

    def add_before(self, p, e):
        original = self.validate(p)
        return self.insert_between(e, original.prev, original)

    def add_after(self, p, e):
        original = self.validate(p)
        return self.insert_between(e, original, original.next)

    def delete(self, p):
        original = self.validate(p)
        return self.delete_node(original)

    def replace(self, p, e):
        original = self.validate(p)
        old_value = original.element
        original.element = e
        return old_value
