import pytest
from graphtool.graph import *
from graphtool.algorithms.mst import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


def test_mst(triangle):
    assert len(MST(triangle))==2
    assert len(MST(GraphGenerator.clique(100)))==99
