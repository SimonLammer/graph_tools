import pytest
from graphtool.graph import *

# ----- utility ------


def triangle():
    a, b, c = Vertex("0"), Vertex("1"), Vertex("2")
    return Graph.from_edge_list([Edge(a, b), Edge(a, c), Edge(b, c)])

# ------ tests ------


def test_test():
    assert True


def test_graph_from_edge_list():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    graph2 = triangle()
    assert (graph1._dict == graph2._dict)
