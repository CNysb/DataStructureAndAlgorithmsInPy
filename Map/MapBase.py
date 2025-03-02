from collections.abc import MutableMapping


class MapBase(MutableMapping):
    class Item:
        def __init__(self, k, v) -> None:
            self.key = k
            self.value = v

        def __eq__(self, other) -> bool:
            return self.key == other.key

        def __ne__(self, other) -> bool:
            return not (self == other)

        def __lt__(self, other):
            return self.key < other.key
