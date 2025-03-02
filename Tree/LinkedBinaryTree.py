from BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    class Node:
        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

    def validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("P must be proper Position type")
        if p.container is not self:
            raise ValueError("P does not belong to this container")
        if p.node.parent is p.node:
            raise ValueError("p is no longer valid")
        return p.node

    def make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def root(self):
        return self.make_position(self.root)

    def parent(self, p):
        node = self.validate(p)
        return self.make_position(node.parent)

    def left(self, p):
        node = self.validate(p)
        return self.make_position(node.left)

    def right(self, p):
        node = self.validate(p)
        return self.make_position(node.right)

    def num_children(self, p):
        node = self.validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def add_root(self, e):
        if self.root is not None:
            raise ValueError("root exists")
        self.size += 1
        self.root = self.Node(e)
        return self.make_position(self.root)

    def add_left(self, p, e):
        node = self.validate(p)
        if node.left is not None:
            raise ValueError("left exists")
        self.size += 1
        node.left = self.Node(e, node)
        return self.make_position(node.left)

    def add_right(self, p, e):
        node = self.validate(p)
        if node.right is not None:
            raise ValueError("right exists")
        self.size += 1
        node.right = self.Node(e, node)
        return self.make_position(node.right)

    def replace(self, p, e):
        node = self.validate(p)
        old = node.element
        node.element = e
        return old

    def delete(self, p):
        node = self.validate(p)
        if self.num_children(p) == 2:
            raise ValueError("P has 2 children")
        child = node.left if node.left is not None else node.right
        if child is not None:
            child.parent = node.parent
        if node is self.root:
            self.root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        node.parent = node
        return node.element

    def attach(self, p, t1, t2):
        node = self.validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("tree type must match")
        self.size += len(t1) + len(t2)
        if not t1.is_empty():
            t1.root.parent = node
            node.left = t1.root
            t1.root = None
            t1.size = 0
        if not t2.is_empty():
            t2.root.parent = node
            node.left = t2.root
            t2.root = None
            t2.size = 0
