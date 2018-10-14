import pytest
from graphtool.graph import *
from graphtool.algorithms.clustering import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


def test_ergos_gallai():
    assert is_erdos_gallai([2]) == False
    assert is_erdos_gallai([1, 1]) == True
    assert is_erdos_gallai([2, 2, 2]) == True
    assert is_erdos_gallai([1, 2]) == False
    assert is_erdos_gallai([2, 3, 3]) == False
    assert is_erdos_gallai([3, 3, 4]) == False


def test_clustering_coeff(triangle):
    assert global_clustering_coeff(triangle) == 0


def test_local_clust_coeff(triangle):
    assert local_clustering_coeff(triangle, Vertex(0)) == 1


def test_avg_local_clust_coeff(triangle):
    assert average_local_clustering_coeff(triangle) == 1
