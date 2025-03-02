from Map.MapBase import MapBase


class UnsortedTableMap(MapBase):
    def __init__(self):
        self.table = list()

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError("key error ")

    def __setitem__(self, k, v):
        for item in self.table:
            if k == item.key:
                item.value = v
            return
        self.table.append(self.Item(k, v))

    def __delitem__(self, k):
        for j in range(len(self.table)):
            if k == self.table[j].key:
                self.table.pop(j)
                return
        raise Exception("key error")

    def __len__(self):
        return len(self.table)

    def __iter__(self):
        for item in self.table:
            yield item.key
