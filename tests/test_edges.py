import pytest
from graphtool.graph import *
from utils import *

def test_vertex_eq():
    vertex1 = Vertex(0)
    assert vertex1 == 0


def test_vertex_lt():
    vertex1 = Vertex(0)
    assert vertex1 < 3


def test_vertex_init():
    vertex1 = Vertex(0, data={})
    assert vertex1["name"] == "0"


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


def test_edge_other():
    edge = Edge(2, 3)
    assert edge.other(2) == 3
    assert edge.other(3) == 2
    try:
        edge.other(0)
        assert False
    except Exception as e:
        assert str(e) == "Vertex 0 is not incident"

def test_edge_fail():
    try:
        edge = Edge(start=None, end=None)
        assert False
    except Exception as e:
        assert str(e) == "Invalid argument"

    try:
        edge = Edge(1, 2, 3)
        assert False
    except Exception as e:
        assert str(e) == "Too many arguments : only 2 were expected"

def test_edge_revert():
    edge = Edge(2, 3)
    assert Edge.revert(edge) == Edge(3, 2)
