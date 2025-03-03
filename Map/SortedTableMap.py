from typing import List

from Map.MapBase import MapBase


class SortedTableMap(MapBase):
    def __init__(self):
        self.table: List[MapBase.Item] = list()

    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self.table[mid].key:
                return mid
            elif k < self.table[mid].key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def __len__(self):
        return len(self.table)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j == len(self.table) or self.table[j].key != k:
            raise KeyError("key error")
        return self.table[j].value

    def __setitem__(self, k, v) -> None:
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table) and self.table[j].key == k:
            self.table[j].value = v
        else:
            self.table.insert(j, self.Item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j == len(self.table) or self.table[j].key != k:
            raise KeyError("key error")
        self.table.pop(j)

    def __iter__(self):
        for item in self.table:
            yield item.key

    def __reverse__(self):
        for item in reversed(self.table):
            yield item.key

    def find_min(self):
        if len(self.table) > 0:
            return (self.table[0].key, self.table[0].value)
        return None

    def find_max(self):
        if len(self.table) > 0:
            item = self.table[-1]
            return (item.key, item.value)

    def find_ge(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table):
            item = self.table[j]
            return (item.key, item.value)
        else:
            return None

    def find_le(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table):
            item = self.table[j]
            return (item.key, item.value)
        else:
            return None

    def find_lt(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j >= len(self.table):
            return None
        if j > 0:
            j -= 1
            item = self.table[j]
            return (item.key, item.value)
        else:
            return None

    def find_gt(self, k):
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table) and self.table[j].key == k:
            j += 1
        if j < len(self.table):
            item = self.table[j]
            return (item.key, item.value)
        else:
            return None

    def find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self.table) - 1)
        while j < len(self.table) and (stop is None or self.table[j].key < stop):
            item = self.table[j]
            yield (item.key, item.value)
            j += 1
