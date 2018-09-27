import pytest
from graphtool.graph import *

# ----- utility ------


def triangle():
    a, b, c = Vertex("0"), Vertex("1"), Vertex("2")
    return Graph.from_edge_list([Edge(a, b), Edge(a, c), Edge(b, c)])

# ------ tests ------


def test_test():
    assert True


def test_edge():
    edge1 = Edge("a", "b")
    edge2 = Edge(Vertex("a"), Vertex("b"))
    edge3 = Edge(edge1)
    assert edge1 == edge2
    assert edge2 == edge3
    assert edge1 == edge3


def test_graph_from_edge_list():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    graph2 = triangle()
    assert (graph1._dict == graph2._dict)


def test_add_vertex_edges():
    graph1 = Graph.empty(1)
    graph1.add_vertex("1")
    graph1.add_vertex("2")
    graph1.add_edge("0", "1")
    graph1.add_edge("0", "2")
    graph1.add_edge("1", "2")
    assert graph1 == triangle()


def test_add_only_edges():
    graph1 = Graph.empty(1)
    graph1.add_edge("0", "1")
    graph1.add_edge("1", "2")
    graph1.add_edge("0", "2")


def test_remove_vertex_edges():
    graph1 = triangle()
    graph1.remove_edge("0", "1")
    graph1.remove_edge("0", "2")
    graph1.remove_vertex("2")
    assert graph1 == Graph.empty(2)


def test_find_isolated_vertices():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.find_isolated_vertices() == []
    graph2 = Graph.empty(2)
    assert graph2.find_isolated_vertices() == ["0", "1"]


def test_density():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.density() == 1
    graph2 = Graph.empty(2)
    assert graph2.density() == 0
