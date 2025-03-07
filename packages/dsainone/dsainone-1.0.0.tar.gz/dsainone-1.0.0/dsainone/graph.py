import numpy as np
import heapq
from numba import njit, prange

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Undirected Graph

    @staticmethod
    @njit(parallel=True)
    def dijkstra_parallel(vertices, edges, src):
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
        return self.dijkstra_parallel(self.V, self.graph, src)
