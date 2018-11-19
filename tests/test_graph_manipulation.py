import pytest
from utils import *
from graphtool.graph import *
from graphtool.algorithms import *


def test_add_vertex_edges(triangle):
    graph1 = GraphGenerator.empty(1)
    graph1.add_vertex(1)
    graph1.add_vertex(2)
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 2)
    graph1.add_edge(1, 2)
    assert graph1 == triangle


def test_add_loop():
    graph = GraphGenerator.empty(1)
    graph_or = GraphGenerator.empty(1, type="oriented")
    graph_mul = GraphGenerator.empty(1, type="multiple")
    try:
        graph.add_edge(0, 0)
        assert False
    except Exception as e:
        assert True
    try:
        graph_or.add_edge(0, 0)
        assert False
    except Exception as e:
        assert True
    graph_mul.add_edge(0, 0)
    assert len(graph.edges()) == 0
    assert len(graph_or.edges()) == 0
    assert len(graph_mul.edges()) == 1


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
    graph1 = GraphGenerator.empty(1, type="oriented")
    graph1.add_vertex(1)
    graph1.add_vertex(2)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(2, 0)
    assert graph1 == oriented_triangle


def test_add_vertex_edges_multiple(multi_triangle):
    graph1 = GraphGenerator.empty(1, type="multiple")
    graph1.add_vertex(1)
    graph1.add_vertex(2)
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(2, 0)
    assert graph1 == multi_triangle


def test_add_only_edges(triangle):
    graph1 = GraphGenerator.empty(1)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(0, 2)
    assert graph1 == triangle


def test_add_only_edges_oriented(oriented_triangle):
    graph1 = GraphGenerator.empty(1, type="oriented")
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(2, 0)
    assert graph1 == oriented_triangle


def test_add_only_edges_multiple(multi_triangle):
    graph1 = GraphGenerator.empty(1, type="multiple")
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(2, 0)
    assert graph1 == multi_triangle


def test_remove_vertex_edges(triangle):
    graph1 = triangle
    graph1.remove_edge(0, 1)
    graph1.remove_edge(0, 2)
    graph1.remove_vertex(2)
    assert graph1 == GraphGenerator.empty(2)


def test_remove_vertex_edges_oriented(oriented_triangle):
    graph1 = oriented_triangle
    graph1.remove_edge(0, 1)
    graph1.remove_edge(2, 0)
    graph1.remove_vertex(2)
    assert graph1 == GraphGenerator.empty(2, type="oriented")


def test_remove_vertex_edges_multi(multi_triangle):
    graph1 = multi_triangle
    graph1.remove_edge(0, 1)
    graph1.remove_edge(0, 1)
    graph1.remove_edge(2, 0)
    graph1.remove_vertex(2)
    assert graph1 == GraphGenerator.empty(2, type="multiple")


def test_getters(triangle, oriented_triangle, multi_triangle):
    assert triangle.vertices() == set([Vertex(0), Vertex(1), Vertex(2)])
    assert triangle.edges() == set([Edge(2, 0), Edge(1, 2), Edge(0, 1)])
    assert oriented_triangle.vertices() == set([Vertex(0),
                                                Vertex(1),
                                                Vertex(2)])
    assert oriented_triangle.edges() == set([Edge(0, 1, oriented=True),
                                             Edge(1, 2, oriented=True),
                                             Edge(2, 0, oriented=True)])
    assert multi_triangle.vertices() == set([Vertex(0),
                                             Vertex(1),
                                             Vertex(2)])
    edge_list = multi_triangle.edges()
    for e in [Edge(2, 0), Edge(1, 2), Edge(0, 1), Edge(0, 1)]:
        assert e in edge_list
        edge_list.remove(e)


def test_renumber(triangle, oriented_triangle, multi_triangle):
    g = GraphGenerator.empty(0, type="simple")
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    assert g.renumber() == triangle


def test_renumber_oriented(oriented_triangle):
    g = GraphGenerator.empty(0, type="oriented")
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    assert g.renumber() == oriented_triangle


def test_renumber_multi(multi_triangle):
    g = GraphGenerator.empty(0, type="multiple")
    g.add_edge(4, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    assert g.renumber() == multi_triangle
