import pytest
from utils import *
from graphtool.graph import *
from graphtool.algorithms import *


def test_edge():
    edge1 = Edge(0, 1)
    edge2 = Edge(Vertex(0), Vertex(1))
    edge3 = Edge(edge1)
    assert edge1 == edge2
    assert edge2 == edge3
    assert edge1 == edge3


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


def test_edge_lt():
    edge1 = Edge(0, 1, data={'weight': 2})
    edge2 = Edge(0, 1, data={'weight': 3})
    assert edge1 < edge2
    edge3 = Edge(0, 1)
    edge4 = Edge(0, 2)
    assert not(edge3 < edge4)


def test_edge_gt():
    edge1 = Edge(0, 1, data={'weight': 2})
    edge2 = Edge(0, 1, data={'weight': 3})
    assert edge2 > edge1
    edge3 = Edge(0, 1)
    edge4 = Edge(0, 2)
    assert not(edge3 > edge4)


def test_edge_other():
    edge = Edge(2, 3)
    assert edge.other(2) == 3
    assert edge.other(3) == 2
    try:
        edge.other(0)
        assert False
    except Exception as e:
        assert str(e) == "Vertex 0 is not incident"


def test_edge_revert():
    edge = Edge(2, 3)
    assert Edge.revert(edge) == Edge(3, 2)


def test_vertex_eq():
    vertex1 = Vertex(0)
    assert vertex1 == 0


def test_vertex_lt():
    vertex1 = Vertex(0)
    assert vertex1 < 3


def test_vertex_init():
    vertex1 = Vertex(0, data={})
    assert vertex1["name"] == "0"


def test_add_vertex_edges(triangle):
    graph1 = GraphGenerator.empty(1)
    graph1.add_vertex(1)
    graph1.add_vertex(2)
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 2)
    graph1.add_edge(1, 2)
    assert graph1 == triangle


def test_add_vertex_to_non_existing():
    g = GraphGenerator.empty(4)
    g.add_edge(1, 2)
    assert g.vertex_degree() == [0, 1, 1, 0]
    g.add_edge(0, 5)
    assert g.vertex_degree() == [1, 1, 1, 0, 1]
    g.edges()
    g.add_edge(1, 5)
    assert g.vertex_degree() == [1, 2, 1, 0, 2]


def test_add_vertex_edges_oriented(oriented_triangle):
    graph1 = GraphGenerator.empty(1, oriented=True)
    graph1.add_vertex(1)
    graph1.add_vertex(2)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(2, 0)
    assert graph1 == oriented_triangle


def test_add_only_edges(triangle):
    graph1 = GraphGenerator.empty(1)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(0, 2)
    assert graph1 == triangle


def test_add_only_edges_oriented(oriented_triangle):
    graph1 = GraphGenerator.empty(1, oriented=True)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(2, 0)
    assert graph1 == oriented_triangle


def test_remove_vertex_edges(triangle):
    graph1 = triangle
    graph1.remove_edge(0, 1)
    graph1.remove_edge(0, 2)
    graph1.remove_vertex(2)
    assert graph1 == GraphGenerator.empty(2)


def test_getters(triangle, oriented_triangle):
    assert triangle.vertices() == set([Vertex(0), Vertex(1), Vertex(2)])
    assert triangle.edges() == set([Edge(2, 0), Edge(1, 2), Edge(0, 1)])
    assert oriented_triangle.vertices() == set([Vertex(0),
                                                Vertex(1),
                                                Vertex(2)])
    assert oriented_triangle.edges() == set([Edge(0, 1, oriented=True),
                                             Edge(1, 2, oriented=True),
                                             Edge(2, 0, oriented=True)])
