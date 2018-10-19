import pytest
from graphtool.graph import *


def test_vertex_eq():
    vertex1 = Vertex(0)
    assert vertex1 == 0


def test_vertex_lt():
    vertex1 = Vertex(0)
    assert vertex1 < 3


def test_vertex_init():
    vertex1 = Vertex(0, data={})
    assert vertex1["name"] == "0"
