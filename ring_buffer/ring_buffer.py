class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.length = 0

    def append(self, item):
        if len(self.storage) <= self.capacity:
            self.storage[self.length] = item
            self.length += 1
        else:
            self.length = 0
            self.storage[self.length] = item
            self.length += 1    

    def get(self):
        for item in self.storage:
            print(item)