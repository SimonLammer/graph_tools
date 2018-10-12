import pytest
from graphtool.graph import *
from graphtool.search import *
from graphtool.path import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


def test_find_isolated_vertices():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.find_isolated_vertices() == []
    graph2 = Graph.empty(2)
    assert set(graph2.find_isolated_vertices()) == {Vertex(0), Vertex(1)}


def test_neighbours():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert {v for v in graph1.get_neighbours(0)} == {Vertex(1), Vertex(2)}


def test_density():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.density() == 1
    graph2 = Graph.empty(2)
    assert graph2.density() == 0


def test_diameter(triangle):
    assert diameter(triangle) == 1
    assert diameter(Graph.empty(2)) == float("inf")
