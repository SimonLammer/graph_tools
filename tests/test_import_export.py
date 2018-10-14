import pytest
from graphtool.algorithms import *
from graphtool.graph import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


def test_edge():
    edge1 = Edge(0, 1)
    edge2 = Edge(Vertex(0), Vertex(1))
    edge3 = Edge(edge1)
    assert edge1 == edge2
    assert edge2 == edge3
    assert edge1 == edge3


def test_graph_from_edge_list(triangle):
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert (graph1 == triangle)


def test_export_as_edge_list():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    graph1.export_as_edge_list("graph_examples/triangle_edge_list.txt")
    graph2 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1 == graph2


def test_export_as_adjacency_list():
    graph1 = Graph.from_adjacency_dict("graph_examples/triangle_adjacency.txt")
    graph1.export_as_adjacency_dict("graph_examples/triangle_adjacency.txt")
    graph2 = Graph.from_adjacency_dict(
        "graph_examples/triangle_adjacency.txt")
    assert graph1 == graph2


def test_export_as_adjacency_matrix():
    graph1 = Graph.from_adjacency_matrix("graph_examples/triangle_matrix.txt")
    graph1.export_as_adjacency_matrix("graph_examples/triangle_matrix.txt")
    graph2 = Graph.from_adjacency_matrix(
        "graph_examples/triangle_matrix.txt")
    assert graph1 == graph2


def test_graph_from_adjacency_dict(triangle):
    graph1 = Graph.from_adjacency_dict("graph_examples/triangle_adjacency.txt")
    assert (graph1 == triangle)


def test_graph_from_adjacency_matrix(triangle):
    graph1 = Graph.from_adjacency_matrix("graph_examples/triangle_matrix.txt")
    assert (graph1 == triangle)


def test_all_import():
    graph_edge = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    graph_adj = Graph.from_adjacency_dict(
        "graph_examples/triangle_adjacency.txt")
    graph_mat = Graph.from_adjacency_matrix(
        "graph_examples/triangle_matrix.txt")
    assert graph_edge == graph_adj
    assert graph_adj == graph_mat
    assert graph_mat == graph_edge


def test_all_import_with_data():
    graph_edge = Graph.from_edge_list(
        "graph_examples/triangle_edge_list.txt",
        vertex_data="graph_examples/triangle_vertex_data.csv",
        edge_data="graph_examples/triangle_edge_data.csv")
    graph_adj = Graph.from_adjacency_dict(
        "graph_examples/triangle_adjacency.txt",
        vertex_data="graph_examples/triangle_vertex_data.csv",
        edge_data="graph_examples/triangle_edge_data.csv")
    graph_mat = Graph.from_adjacency_matrix(
        "graph_examples/triangle_matrix.txt",
        vertex_data="graph_examples/triangle_vertex_data.csv",
        edge_data="graph_examples/triangle_edge_data.csv")
    assert graph_edge == graph_adj
    assert graph_adj == graph_mat
    assert graph_mat == graph_edge
