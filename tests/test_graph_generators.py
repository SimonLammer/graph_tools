import pytest
from graphtool.graph import *
from graphtool.graph.generator import *
from utils import *


def test_empty():
    g = GraphGenerator.empty(10)
    assert len(g) == 10
    assert len(g.edges()) == 0


def test_cycle(triangle, oriented_triangle):
    assert GraphGenerator.cycle(3) == triangle
    assert GraphGenerator.cycle(3, oriented=True) == oriented_triangle


def test_clique(triangle):
    assert GraphGenerator.clique(3) == triangle


def test_random_graph_generator():
    assert GraphGenerator.erdos_renyi_proba(10, 0) == GraphGenerator.empty(10)
    assert GraphGenerator.erdos_renyi_proba(10, 1) == GraphGenerator.clique(10)
    graph1 = GraphGenerator.erdos_renyi_edge(100, 250)
    graph2 = GraphGenerator.erdos_renyi_proba(100, 0.5)
    assert len(graph1.edges()) == 250
    assert len(graph1.vertices()) == 100
    assert len(graph2.vertices()) == 100


def test_chung_lu():
    seq = [1, 1]
    assert len(GraphGenerator.chung_lu(seq)) == 2
    seq = [2, 2, 2]
    assert len(GraphGenerator.chung_lu(seq)) == 3


def test_molloy_reed():
    seq = [1, 1, 2, 2, 4]
    assert len(GraphGenerator.molloy_reed(seq)) == 5
