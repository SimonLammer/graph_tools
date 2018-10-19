import pytest
from graphtool.graph import *


def test_vertex_eq():
    vertex1 = Vertex(0)
    vertex2 = Vertex(0)
    assert vertex1 == 0
    assert vertex1 == vertex2


def test_vertex_comp():
    vertex1 = Vertex(0)
    vertex2 = Vertex(1)
    assert vertex1 < 3
    assert vertex1 <= 3
    assert vertex1 <= 0
    assert vertex1 < vertex2
    assert vertex1 <= vertex2
    assert vertex1 <= vertex1
    assert vertex2 > 0
    assert vertex2 >= 0
    assert vertex2 >= 1
    assert vertex2 > vertex1
    assert vertex2 >= vertex1
    assert vertex2 >= vertex2


def test_vertex_init():
    vertex1 = Vertex(0, data={})
    assert vertex1["name"] == "0"
