from random import randrange
from typing import List

from Map.MapBase import MapBase


class HashMapBase(MapBase):
    def __init__(self, cap=11, p=109345121):
        self.table: List = [None] * cap
        self.n = 0
        self.prime = p
        self.scale = 1 + randrange(p - 1)
        self.shift = randrange(p)

    def hash_function(self, k):
        return (hash(k) * self.scale + self.shift) % self.prime % len(self.table)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        j = self.hash_function(k)
        return self.bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self.hash_function(k)
        self.bucket_setitem(j, k, v)
        if self.n > len(self.table) // 2:
            self.resize(2 * len(self.table) - 1)

    def __delitem__(self, k):
        j = self.hash_function(k)
        self.bucket_delitem(j, k)
        self.n -= 1

    def resize(self, c):
        old = list(self.items())
        self.table = c * [None]
        self.n = 0
        for k, v in old:
            self[k] = v

    def bucket_delitem(self, j, k):
        pass

    def bucket_setitem(self, j, k, v):
        pass

    def bucket_getitem(self, j, k):
        pass
