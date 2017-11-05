import Graph

def test_scc():
    graph = Graph.Graph(5)
    graph.add_edge(1, 0)
    graph.add_edge(0, 2)
    graph.add_edge(2, 1)
    graph.add_edge(0, 3)
    graph.add_edge(3, 4)
    graph.make_scc()
    assert 0 in graph.scc[0]
    