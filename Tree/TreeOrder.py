from collections import deque
from queue import Queue

from LinkedBinaryTree import LinkedBinaryTree


class TreeOrder(LinkedBinaryTree):
    # 左遍历
    def pre_order(self):
        if not self.is_empty():
            for p in self._subtree_pre_order(self.root):
                yield p

    def _subtree_pre_order(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_pre_order(c):
                yield other

    # 右遍历
    def post_order(self):
        if not self.is_empty():
            for p in self._subtree_post_order(self.root):
                yield p

    def _subtree_post_order(self, p):
        for c in self.children(p):
            for other in self._subtree_post_order(c):
                yield other
        yield p

    # 广度遍历
    def bread_order_with_deque(self):
        if not self.is_empty():
            fringe = deque()
            fringe.append(self.root)
        else:
            raise ValueError("tree is empty")
        while not len(fringe) == 0:
            p = fringe.popleft()
            yield p
            for c in self.children(p):
                fringe.append(c)

    def bread_order_with_queue(self):
        if not self.is_empty():
            node_q = Queue()
            node_q.put(self.root)
        else:
            raise ValueError("tree is empty")
        while not node_q.empty():
            p = node_q.get()
            yield p
            for c in self.children(p):
                node_q.put(c)

    # 中序遍历
    def in_order(self):
        pass
