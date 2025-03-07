from dsainone.graph import Graph

def test_dijkstra():
    g = Graph(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 5)
    assert g.compute_dijkstra(0) == [0, 10, 5, float('inf'), float('inf')]

test_dijkstra()
