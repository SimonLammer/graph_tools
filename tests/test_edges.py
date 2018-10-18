import pytest
from graphtool.graph import *
from utils import *


def test_edge():
    edge1 = Edge(0, 1)
    edge2 = Edge(Vertex(0), Vertex(1))
    edge3 = Edge(edge1)
    assert edge1 == edge2
    assert edge2 == edge3
    assert edge1 == edge3


def test_edge_revert():
    edge = Edge(0, 1, oriented=True, data={"name": "toto"})
    edge2 = Edge.revert(edge)
    assert edge2.start == Vertex(1)
    assert edge2.end == Vertex(0)
    assert edge2["name"] == "toto"


def test_edge_get_set():
    edge = Edge(0, 1)
    edge["name"] = "toto"
    edge["color"] = 42
    assert edge["name"] == "toto"
    assert edge["color"] == 42


def test_comp():
    edge1 = Edge(0, 1)
    edge2 = Edge(4, 5)
    edge3 = Edge(0, 2)
    edge4 = Edge(0, 1, data={"weight": 42})
    assert edge1 <= edge1
    assert edge1 >= edge1
    assert edge1 < edge2
    assert edge1 < edge3
    assert edge4 > edge1
