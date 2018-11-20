import pytest
from graphtool.graph import *
from graphtool.graph.generator import *
from utils import *


def test_empty():
    g1 = GraphGenerator.empty(10, type="simple")
    g2 = GraphGenerator.empty(10, type="simple")
    g3 = GraphGenerator.empty(10, type="simple")
    assert len(g1) == 10
    assert len(g2) == 10
    assert len(g3) == 10
    assert len(g1.edges()) == 0
    assert len(g2.edges()) == 0
    assert len(g3.edges()) == 0


def test_cycle(triangle, oriented_triangle):
    assert GraphGenerator.cycle(3) == triangle
    assert GraphGenerator.cycle(3, type="oriented") == oriented_triangle


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


def test_configuration_model():
    seq = [1, 1, 2, 2, 4]
    assert len(GraphGenerator.configuration_model(seq)) == 5
    seq = [1, 2]
    try:
        GraphGenerator.configuration_model(seq)
        assert False
    except Exception as e:
        assert str(e) == "The sum of degrees should be even!"

   
def test_barabasi_albert():
    graph = GraphGenerator.barabasi_albert(100, 0.1)
    assert len(graph.vertices()) == 100
    graph = GraphGenerator.barabasi_albert(100, 0.1)
    assert len(graph.vertices()) == 100
    graph = GraphGenerator.barabasi_albert(100, 0.1)
    assert len(graph.vertices()) == 100
    
    
def test_watts_strogatz():
    N = 20
    k = 8
    beta = 0.25
    G = GraphGenerator.watts_strogatz(N, k, beta)
    assert sum(G.degree_sequence()) == N*k
    k = 3
    try:
        G = GraphGenerator.watts_strogatz(N, k, beta)
        assert False
    except Exception as e:
        assert str(e) == "The mean degree must be even"
