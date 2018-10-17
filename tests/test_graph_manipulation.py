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


def test_add_vertex_edges(triangle):
    graph1 = GraphGenerator.empty(1)
    graph1.add_vertex(1)
    graph1.add_vertex(2)
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 2)
    graph1.add_edge(1, 2)
    assert graph1 == triangle


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
