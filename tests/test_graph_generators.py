import pytest
from graphtool.graph import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


def test_cycle(triangle):
    assert Graph.cycle(3) == triangle


def test_clique(triangle):
    assert Graph.clique(3) == triangle


def test_random_graph_generator():
    assert Graph.erdos_renyi_proba(10, 0) == Graph.empty(10)
    assert Graph.erdos_renyi_proba(10, 1) == Graph.clique(10)
    graph1 = Graph.erdos_renyi_edge(100, 250)
    graph2 = Graph.erdos_renyi_proba(100, 0.5)
    assert len(graph1.edges()) == 250
    assert len(graph1.vertices()) == 100
    assert len(graph2.vertices()) == 100
