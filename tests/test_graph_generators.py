import pytest
from graphtool.graph import *
from graphtool.search import *
from graphtool.path import *


def test_random_graph_generator():
    assert Graph.erdos_renyi_proba(10, 0) == Graph.empty(10)
    assert Graph.erdos_renyi_proba(10, 1) == Graph.clique(10)
    graph1 = Graph.erdos_renyi_edge(100, 250)
    graph2 = Graph.erdos_renyi_proba(100, 0.5)
    assert len(graph1.edges()) == 250
    assert len(graph1.vertices()) == 100
    assert len(graph2.vertices()) == 100
