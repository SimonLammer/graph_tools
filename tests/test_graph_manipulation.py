import pytest
from graphtool.graph import *
from graphtool.algorithms import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


def test_edge():
    edge1 = Edge(0, 1)
    edge2 = Edge(Vertex(0), Vertex(1))
    edge3 = Edge(edge1)
    assert edge1 == edge2
    assert edge2 == edge3
    assert edge1 == edge3


def test_add_vertex_edges(triangle):
    graph1 = GraphGenerator.empty(1)
    graph1.add_vertex(1)
    graph1.add_vertex(2)
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 2)
    graph1.add_edge(1, 2)
    assert graph1 == triangle


def test_add_only_edges(triangle):
    graph1 = GraphGenerator.empty(1)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(0, 2)
    assert graph1 == triangle


def test_remove_vertex_edges(triangle):
    graph1 = triangle
    graph1.remove_edge(0, 1)
    graph1.remove_edge(0, 2)
    graph1.remove_vertex(2)
    assert graph1 == GraphGenerator.empty(2)
