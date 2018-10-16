import pytest
from graphtool.graph import *
from graphtool.algorithms.mst import *
from utils import *


def test_kruskal(triangle):
    assert len(MST(triangle, algo='Kruskal')) == 2
    assert len(MST(GraphGenerator.clique(100), algo='Kruskal')) == 99


def test_prim(triangle):
    assert len(MST(triangle, algo='Prim')) == 2
    assert len(MST(GraphGenerator.clique(100), algo='Prim')) == 99
