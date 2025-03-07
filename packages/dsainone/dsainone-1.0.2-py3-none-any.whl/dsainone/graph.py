import heapq
import numpy as np
from numba import njit

class Graph:
    __slots__ = ("V", "graph")

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]  # Faster than dictionary

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  

    @staticmethod
    @njit
    def dijkstra(vertices, edges, src):
        dist = np.full(vertices, np.inf, dtype=np.float32)
        dist[src] = 0
        pq = [(0, src)]
        
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, weight in edges[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return dist.tolist()

    def compute_dijkstra(self, src):
        return self.dijkstra(self.V, self.graph, src)
