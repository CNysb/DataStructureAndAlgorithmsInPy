from PriorityQueueBase import PriorityQueueBase



class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self) -> None:
        pass


    def find_main(self):
        if self.is_empty():
            rasie ValueError("priority queue is empty")
