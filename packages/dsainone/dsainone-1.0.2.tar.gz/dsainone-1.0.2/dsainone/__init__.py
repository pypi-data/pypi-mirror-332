from .graph import Graph
from .tree import AVLTree
from .hash_table import HashTable
from .linked_list import LinkedList

class DSALibrary:
    __slots__ = ("graph", "avl_tree", "hash_table", "linked_list")

    def __init__(self):
        self.graph = None
        self.avl_tree = AVLTree()
        self.hash_table = HashTable()
        self.linked_list = LinkedList()
    
    def create_graph(self, vertices):
        self.graph = Graph(vertices)
    
    def add_graph_edge(self, u, v, weight):
        if self.graph:
            self.graph.add_edge(u, v, weight)
    
    def run_dijkstra(self, src):
        return self.graph.compute_dijkstra(src) if self.graph else None

    def insert_avl(self, root, key):
        return self.avl_tree.insert(root, key)

    def insert_hash(self, key, value):
        self.hash_table.insert(key, value)

    def search_hash(self, key):
        return self.hash_table.search(key)

    def insert_linked_list(self, data):
        self.linked_list.insert(data)

    def search_linked_list(self, key):
        return self.linked_list.search(key)
