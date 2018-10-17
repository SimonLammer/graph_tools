import pytest
from graphtool.graph import *
from graphtool.algorithms import *
from utils import *


def test_adjacency(triangle):
    expected = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    assert triangle.adjacency_matrix() == expected


def test_find_isolated_vertices():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.find_isolated_vertices() == []
    graph2 = GraphGenerator.empty(2)
    assert set(graph2.find_isolated_vertices()) == {Vertex(0), Vertex(1)}


def test_sources_sink(oriented_triangle):
    g = GraphGenerator.empty(3, oriented=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    assert g.get_sinks() == [Vertex(2)]
    assert g.get_sources() == [Vertex(0)]
    assert oriented_triangle.get_sinks() == []
    assert oriented_triangle.get_sources() == []


def test_neighbours():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    graph2 = OrientedGraph.from_edge_list(
        "graph_examples/triangle_edge_list.txt")
    assert {v for v in graph1.get_neighbours(0)} == {Vertex(1), Vertex(2)}
    assert {v for v in graph2.get_neighbours(0)} == {Vertex(1)}


def test_neighbours_edge():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    graph2 = OrientedGraph.from_edge_list(
        "graph_examples/triangle_edge_list.txt")
    assert graph1.get_neighbours_edge(0) == {Edge(0, 1), Edge(0, 2)}
    assert graph2.get_neighbours_edge(0) == {Edge(0, 1, oriented=True)}


def test_edges():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    graph2 = OrientedGraph.from_edge_list(
        "graph_examples/triangle_edge_list.txt")
    assert graph1.edges() == {Edge(0, 1), Edge(1, 2), Edge(2, 0)}
    assert graph2.edges() == {Edge(0, 1, oriented=True), Edge(
        1, 2, oriented=True), Edge(2, 0, oriented=True)}


def test_density():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.density() == 1
    graph2 = GraphGenerator.empty(2)
    assert graph2.density() == 0
    graph3 = GraphGenerator.clique(10)
    assert graph3.density() == 1


def test_diameter(triangle):
    assert diameter(triangle) == 1
    assert diameter(GraphGenerator.empty(2)) == float("inf")


"""
def test_diameter2(triangle):
    assert diameter(triangle)==biggest_component_diameter(triangle)
"""
