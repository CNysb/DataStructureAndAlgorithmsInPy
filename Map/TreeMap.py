


from Map.MapBase import MapBase
from Tree.LinkedBinaryTree import LinkedBinaryTree


class TreeMap(LinkedBinaryTree, MapBase):
    def _subtree_search(self, p, k):
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_postion(self, p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_postion(self, p):
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        return self._subtree_first_postion(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_postion(self.root()) if len(self) > 0 else None

    def before(self, p):
        if self.left(p):
            return self._subtree_last_postion(self.left(p))
        above = self.parent(p)
        while p is not None and p == self.left(above):
            p = above
            above = self.parent(p)
        return above

    def after(self, p):
        if self.right(p):
            return self._subtree_last_postion(self.right(p))
        above = self.parent(p)
        while p is not None and p == self.right(above):
            p = above
            above = self.parent(p)
        return above

    def find_postion(self, k):
        if self.is_empty():
            return
        p = self._subtree_search(self.root(), k)
        self._rebalance_access(p)
        return p

    def find_min(self):
        if self.is_empty():
            return
        p = self.first()
        return (p.key, p.value)

    def find_ge(self, k):
        if self.is_empty():
            return
        p = self.find_postion(k)
        if p.key < k:
            p = self.after(p)
        return (p.key, p.value)

    def find_range(self, start, stop):
        if self.is_empty():
            return

        if start is None:
            p = self.first()
        else:
            p = self.find_postion(start)
            if p.key < start:
                p = self.after(p)
        while p is not None and (stop is None or p.key < stop):
            yield (p.key, p.value)
            p = self.after(p)

    def __getitem__(self, key):
        if self.is_empty():
            raise KeyError("key error")
        p = self._subtree_search(key)
        self._rebalance_access(p)
        if key != p.key:
            raise KeyError("key error")
        return p.value


    def __setitem__(self,k, v):
        if self.is_empty():
            leaf = self.add_root(self.Item(k, v))
        else:
            p = self._subtree_search(k)
            if p.key == k:
                p.element.value = v
                self._rebalance_access(p)
                return
            else:
                item = self.Item(k, v)
                if p.key < k:
                    leaf = self.add_right(p, item)
                else:
                    leaf = self.add_left(p, item)
        self._rebalance_access(leaf)

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key
            p = self.after(p)

    def delete(self, p):
        self.validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_postion(self.left(p))
            self.replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self.delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k) -> None:
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key:
                self.delete(p)
                return
            self._rebalance_access(p)
        raie KeyError("keyerror")

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_access(self, p):
        pass

    def _relink(self, parent, child, make_left_child):
        if make_left_child:
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent

    def _rotate(self, p):
        x = p.node
        y = p.parent
        z = p.parent
        
        if z is None:
            self.root = x
            x.parent = None
        else:
            self._relink(z, x, y==z.left)

        if x == y.left:
            self._relink(y, x.right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x.left, False)
            self._relink(x, y, True)

    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)

        if (x == self.right(y)) is (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            return x

    class Position(LinkedBinaryTree.Position):
        @property
        def key(self):
            return self.element().key

        @property
        def value(self):
            return self.element().value

    
