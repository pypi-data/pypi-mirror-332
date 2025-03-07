class HashTable:
    __slots__ = ("capacity", "table", "size")

    def __init__(self, capacity=101):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.capacity
        self.table[index] = (key, value)
        self.size += 1

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
        return None
