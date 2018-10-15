import pytest
from graphtool.graph import *
from graphtool.algorithms.mst import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


def test_kruskal(triangle):
    assert len(MST(triangle, algo=='Kruskal'))==2
    assert len(MST(GraphGenerator.clique(100), algo='Kruskal'))==99

def test_prim(triangle):
    assert len(MST(triangle, algo=='Prim'))==2
    assert len(MST(GraphGenerator.clique(100), algo='Prim'))==99

def test_MST(triangle):
    test_kruskal(triangle)
    test_prim(triangle)
