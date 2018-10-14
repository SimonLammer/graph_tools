import pytest
from graphtool.graph import *
from graphtool.algorithms.search import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


def test_connected_components(triangle):
    g = Graph.empty(3)
    g.add_edge(0, 1)
    assert len(get_connected_components(g)) == 2
    assert len(get_connected_components(triangle)) == 1
