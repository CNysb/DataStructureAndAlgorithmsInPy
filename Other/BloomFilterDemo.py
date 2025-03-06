from bitarray import bitarray
import mmh3


class BloomFilter:
    def __init__(self, size, hash_count) -> None:
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size * 5)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    def check(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True


bl = BloomFilter(500000, 7)
bl.add("apple")
bl.add("mango")
bl.add("banana")

print(bl.check("apple"))
