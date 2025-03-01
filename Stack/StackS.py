class StackS:
    # push , pop, top , is_empty, len
    def __init__(self) -> None:
        self._data = list()

    def push(self, value):
        return self._data.append(value)

    def pop(self):
        if len(self._data) == 0:
            raise IndexError("invalid index ...")
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def top(self):
        if len(self._data) == 0:
            raise IndexError("invalid index ...")
        return self._data[0]
