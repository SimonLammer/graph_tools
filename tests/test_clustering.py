import pytest
from graphtool.graph import *
from graphtool.algorithms.clustering import *
from utils import *


def test_ergos_gallai():
    assert is_erdos_gallai([2]) is False
    assert is_erdos_gallai([1, 1]) is True
    assert is_erdos_gallai([2, 2, 2]) is True
    assert is_erdos_gallai([1, 2]) is False
    assert is_erdos_gallai([2, 3, 3]) is False
    assert is_erdos_gallai([3, 3, 4]) is False


def test_clustering_coeff(triangle):
    assert global_clustering_coeff(GraphGenerator.empty(10)) == 0
    assert global_clustering_coeff(triangle) == 1
    assert global_clustering_coeff(GraphGenerator.clique(10)) == 1


def test_local_clust_coeff(triangle):
    assert local_clustering_coeff(triangle, Vertex(0)) == 1
    assert local_clustering_coeff(triangle, 0) == 1
    assert local_clustering_coeff(GraphGenerator.empty(5), 0) == 0


def test_avg_local_clust_coeff(triangle):
    assert average_local_clustering_coeff(triangle) == 1
