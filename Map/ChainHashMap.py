from Map.HashMapBase import HashMapBase
from Map.UnsortedTableMap import UnsortedTableMap


class ChainHashMap(HashMapBase):
    def bucket_setitem(self, j, k, v):
        if self.table[j] is None:
            self.table[j] = UnsortedTableMap()
        oldsize = len(self.table[j])
        self.table[j][k] = v
        if len(self.table[j]) > oldsize:
            self.n += 1

    def bucket_getitem(self, j, k):
        bucket = self.table[j]
        if bucket is None:
            raise Exception("key error ")
        return bucket[k]

    def bucket_delitem(self, j, k):
        bucket = self.table[j]
        if bucket is None:
            raise Exception("key error ")
        del bucket[k]

    def __iter__(self):
        for bucket in self.table:
            if bucket is not None:
                for key in bucket:
                    yield key
