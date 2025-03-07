class LinkedListNode:
    __slots__ = ("data", "next")

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    __slots__ = ("head", "cache")

    def __init__(self):
        self.head = None
        self.cache = {}

    def insert(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node
        self.cache[data] = new_node

    def search(self, key):
        return self.cache.get(key)
