class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.cache = {}  # Caching to improve search speed

    def insert(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node
        self.cache[data] = new_node  # Store in cache

    def search(self, key):
        return self.cache.get(key, None)  # Optimized lookup
