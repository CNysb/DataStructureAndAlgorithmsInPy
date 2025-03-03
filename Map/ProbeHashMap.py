from Map.HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
    _AVAIL = object()

    def is_available(self, j) -> bool:
        return self.table[j] is None or self.table[j] is ProbeHashMap._AVAIL

    def find_slot(self, j, k):
        firstAvail = None
        while True:
            if self.is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self.table[j] is None:
                    return (False, firstAvail)

            elif k == self.table[j].key:
                return (True, j)
            j = (j + 1) % (len(self.table))

    def bucket_getitem(self, j, k):
        found, s = self.find_slot(j, k)
        if not found:
            raise KeyError("key error ")
        return self.table[s].value

    def bucket_setitem(self, j, k, v):
        found, s = self.find_slot(j, k)
        if not found:
            self.table[s] = self.Item(k, v)
            self.n += 1
        else:
            self.table[s].value = v

    def bucket_delitem(self, j, k):
        found, s = self.find_slot(j, k)
        if not found:
            raise KeyError("key error ")
        self.table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self.table)):
            if not self.is_available(j):
                yield self.table[j].key
