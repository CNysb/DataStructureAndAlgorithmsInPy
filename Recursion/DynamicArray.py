import ctypes


class DynamicArray:
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.__data = self.__make_array(self.capacity)

    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __getitem__(self, k):
        if k >= self.capacity:
            raise IndexError("invalid index...")
        return self.__data[k]

    def append(self, obj):
        if self.length == self.capacity:
            self.__resize(self.capacity * 2)
        self.__data[self.length] = obj
        self.length += 1

    def __resize(self, cur_length):
        new_data = self.__make_array(cur_length)
        for i in range(self.length):
            new_data[i] = self.__data[i]
        self.__data = new_data
        self.capacity = cur_length
