class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = []
        self.capacity = k
        self.k = self.capacity

    def enQueue(self, value: int) -> bool:
        if self.k > 0:
            self.queue.append(value)
            self.k -= 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            self.k += 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.k == 0:
            return True
        else:
            return False