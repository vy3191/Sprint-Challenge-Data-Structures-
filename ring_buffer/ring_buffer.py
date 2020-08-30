class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.capacity = capacity
        self.length = 0

    def append(self, item):
        if self.length < self.capacity:
            self.storage[self.length] = item
            self.length += 1
        else:
            self.length = 0
            self.storage[self.length] = item
            self.length += 1    

    def get(self):
        item_list = []
        for item in self.storage:
            item_list.append(item)
        return item_list    