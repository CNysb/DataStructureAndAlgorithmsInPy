class PriorityQueueBase:
    class Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __lt__(self, other):
            return self.key < other.key

    def is_empty(self):
        return len(self) == 0
