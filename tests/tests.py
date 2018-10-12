import pytest
from graphtool.graph import *
from graphtool.search import *
from graphtool.path import *


# ----- utility ------


def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])

# ------ tests ------


def test_test():
    assert True


def test_edge():
    edge1 = Edge(0, 1)
    edge2 = Edge(Vertex(0), Vertex(1))
    edge3 = Edge(edge1)
    assert edge1 == edge2
    assert edge2 == edge3
    assert edge1 == edge3


def test_graph_from_edge_list():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert (graph1 == triangle())


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


def test_graph_from_adjacency_dict():
    graph1 = Graph.from_adjacency_dict("graph_examples/triangle_adjacency.txt")
    print(graph1._dict)
    print(triangle()._dict)
    assert (graph1 == triangle())


def test_graph_from_adjacency_matrix():
    graph1 = Graph.from_adjacency_matrix("graph_examples/triangle_matrix.txt")
    print(graph1._dict)
    print(triangle()._dict)
    assert (graph1 == triangle())


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


def test_cycle():
    assert Graph.cycle(3) == triangle()


def test_clique():
    assert Graph.clique(3) == triangle()


def test_add_vertex_edges():
    graph1 = Graph.empty(1)
    graph1.add_vertex(1)
    graph1.add_vertex(2)
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 2)
    graph1.add_edge(1, 2)
    assert graph1 == triangle()


def test_add_only_edges():
    graph1 = Graph.empty(1)
    graph1.add_edge(0, 1)
    graph1.add_edge(1, 2)
    graph1.add_edge(0, 2)


def test_remove_vertex_edges():
    graph1 = triangle()
    graph1.remove_edge(0, 1)
    graph1.remove_edge(0, 2)
    graph1.remove_vertex(2)
    assert graph1 == Graph.empty(2)


def test_find_isolated_vertices():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.find_isolated_vertices() == []
    graph2 = Graph.empty(2)
    assert set(graph2.find_isolated_vertices()) == set(["0", "1"])


def test_density():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.density() == 1
    graph2 = Graph.empty(2)
    assert graph2.density() == 0


def test_diameter():
    assert diameter(triangle()) == 1
    assert diameter(Graph.empty(2)) == float("inf")


def test_random_graph_generator():
    assert Graph.erdos_renyi_proba(10, 0) == Graph.empty(10)
    assert Graph.erdos_renyi_proba(10, 1) == Graph.clique(10)
    graph1 = Graph.erdos_renyi_edge(100, 250)
    graph2 = Graph.erdos_renyi_proba(100, 0.5)
    assert len(graph1.edges()) == 250
    assert len(graph1.vertices()) == 100
    assert len(graph2.vertices()) == 100
