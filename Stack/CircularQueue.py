


class CircularQueue:
    class _node:
        def __init__(self) -> None:
            self._tail = None
            self._size = 0

        def __len__(self):
            return self._size

        def is_empty(self):
            return self._size == 0

        def first(self):
            if self.is_empty():
                rasie Exception("empty")
            head = self._tail._next



