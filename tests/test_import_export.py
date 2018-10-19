import pytest
from graphtool.graph import *
from utils import *


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
    d = graph1._dict
    graph2 = Graph.from_adjacency_dict(d)
    assert graph2 == graph1


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


def test_str_conversion():
    g = GraphGenerator.clique(3)
    txt = '{V(0): {V(1), V(2)}, V(1): {V(0), V(2)}, V(2): {V(0), V(1)}}'
    assert str(g) == txt


# ---- Oriented tests ------


def test_oriented_graph_from_edge_list(oriented_triangle):
    graph1 = OrientedGraph.from_edge_list(
        "graph_examples/triangle_edge_list.txt")
    assert (graph1 == oriented_triangle)


def test_oriented_export_as_edge_list():
    graph1 = OrientedGraph.from_edge_list(
        "graph_examples/triangle_edge_list.txt")
    graph1.export_as_edge_list("graph_examples/triangle_edge_list.txt")
    graph2 = OrientedGraph.from_edge_list(
        "graph_examples/triangle_edge_list.txt")
    assert graph1 == graph2


def test_oriented_export_as_adjacency_list():
    graph1 = OrientedGraph.from_adjacency_dict(
        "graph_examples/triangle_adjacency.txt")
    graph1.export_as_adjacency_dict("graph_examples/triangle_adjacency.txt")
    graph2 = OrientedGraph.from_adjacency_dict(
        "graph_examples/triangle_adjacency.txt")
    assert graph1 == graph2


def test_oriented_export_as_adjacency_matrix():
    graph1 = OrientedGraph.from_adjacency_matrix(
        "graph_examples/triangle_matrix_oriented.txt")
    graph1.export_as_adjacency_matrix(
        "graph_examples/triangle_matrix_oriented.txt")
    graph2 = OrientedGraph.from_adjacency_matrix(
        "graph_examples/triangle_matrix_oriented.txt")
    assert graph1 == graph2


def test_oriented_graph_from_adjacency_dict(oriented_triangle):
    graph1 = OrientedGraph.from_adjacency_dict(
        "graph_examples/triangle_adjacency_oriented.txt")
    assert (graph1 == oriented_triangle)


def test_oriented_graph_from_adjacency_matrix(oriented_triangle):
    graph1 = OrientedGraph.from_adjacency_matrix(
        "graph_examples/triangle_matrix_oriented.txt")
    assert (graph1 == oriented_triangle)


def test_oriented_all_import():
    graph_edge = OrientedGraph.from_edge_list(
        "graph_examples/triangle_edge_list.txt")
    graph_adj = OrientedGraph.from_adjacency_dict(
        "graph_examples/triangle_adjacency_oriented.txt")
    graph_mat = OrientedGraph.from_adjacency_matrix(
        "graph_examples/triangle_matrix_oriented.txt")
    assert graph_edge == graph_adj
    assert graph_adj == graph_mat
    assert graph_mat == graph_edge


def test_oriented_all_import_with_data():
    graph_edge = OrientedGraph.from_edge_list(
        "graph_examples/triangle_edge_list.txt",
        vertex_data="graph_examples/triangle_vertex_data.csv",
        edge_data="graph_examples/triangle_edge_data.csv")
    graph_adj = OrientedGraph.from_adjacency_dict(
        "graph_examples/triangle_adjacency_oriented.txt",
        vertex_data="graph_examples/triangle_vertex_data.csv",
        edge_data="graph_examples/triangle_edge_data.csv")
    graph_mat = OrientedGraph.from_adjacency_matrix(
        "graph_examples/triangle_matrix_oriented.txt",
        vertex_data="graph_examples/triangle_vertex_data.csv",
        edge_data="graph_examples/triangle_edge_data.csv")
    assert graph_edge == graph_adj
    assert graph_adj == graph_mat
    assert graph_mat == graph_edge


def test_symetrization(triangle, oriented_triangle):
    assert oriented_triangle.symetrize() == triangle


def test_subgraph(triangle, oriented_triangle, multi_triangle):
    assert triangle.subgraph([Vertex(0), Vertex(1), Vertex(2)]) == triangle
    assert triangle.subgraph([0]) == GraphGenerator.empty(1)
    assert oriented_triangle.subgraph(
        [Vertex(0), Vertex(1), Vertex(2)]) == oriented_triangle
    assert oriented_triangle.subgraph(
        [0]) == GraphGenerator.empty(1, type="oriented")
    assert multi_triangle.subgraph(
        [Vertex(0)]) == GraphGenerator.empty(1, type="multiple")
    assert multi_triangle.subgraph([0, 1, 2]) == multi_triangle

# ----------- Multigraph tests --------------------


def test_init_multigraph(multi_triangle):
    assert len(multi_triangle) == 3
    assert len(multi_triangle.edges()) == 4


def test_multiple_graph_from_edge_list(multi_triangle):
    graph1 = MultiGraph.from_edge_list(
        "graph_examples/multigraphs/triangle_edge_list_duplicate.txt")
    assert len(graph1) == 3
    assert len(graph1.edges()) == 4


def test_multiple_export_as_edge_list():
    graph1 = MultiGraph.from_edge_list(
        "graph_examples/multigraphs/triangle_edge_list_duplicate.txt")
    graph1.export_as_edge_list(
        "graph_examples/multigraphs/triangle_edge_list_duplicate.txt")
    graph2 = MultiGraph.from_edge_list(
        "graph_examples/multigraphs/triangle_edge_list_duplicate.txt")
    assert graph1 == graph2


def test_multiple_export_as_adjacency_list():
    graph1 = MultiGraph.from_adjacency_dict(
        "graph_examples/multigraphs/triangle_adjacency_duplicate.txt")
    graph1.export_as_adjacency_dict(
        "graph_examples/multigraphs/triangle_adjacency_duplicate.txt")
    graph2 = MultiGraph.from_adjacency_dict(
        "graph_examples/multigraphs/triangle_adjacency_duplicate.txt")
    assert len(graph1.edges()) == 4
    assert graph1 == graph2


def test_multiple_export_as_adjacency_matrix():
    graph1 = MultiGraph.from_adjacency_matrix(
        "graph_examples/multigraphs/triangle_matrix_duplicate.txt")
    graph1.export_as_adjacency_matrix(
        "graph_examples/multigraphs/triangle_matrix_duplicate.txt")
    graph2 = MultiGraph.from_adjacency_matrix(
        "graph_examples/multigraphs/triangle_matrix_duplicate.txt")
    assert graph1 == graph2


def test_multiple_graph_from_adjacency_dict(multi_triangle):
    graph1 = MultiGraph.from_adjacency_dict(
        "graph_examples/multigraphs/triangle_adjacency_duplicate.txt")
    assert (graph1 == multi_triangle)


def test_multiple_graph_from_adjacency_matrix(multi_triangle):
    graph1 = MultiGraph.from_adjacency_matrix(
        "graph_examples/multigraphs/triangle_matrix_duplicate.txt")
    assert (graph1 == multi_triangle)


def test_multiple_all_import():
    graph_edge = MultiGraph.from_edge_list(
        "graph_examples/multigraphs/triangle_edge_list_duplicate.txt")
    graph_adj = MultiGraph.from_adjacency_dict(
        "graph_examples/multigraphs/triangle_adjacency_duplicate.txt")
    graph_mat = MultiGraph.from_adjacency_matrix(
        "graph_examples/multigraphs/triangle_matrix_duplicate.txt")
    assert graph_edge == graph_adj
    assert graph_adj == graph_mat
    assert graph_mat == graph_edge


def test_multiple_all_import_with_data():
    graph_edge = MultiGraph.from_edge_list(
        "graph_examples/multigraphs/triangle_edge_list_duplicate.txt",
        vertex_data="graph_examples/multigraphs/triangle_vertex_data.csv",
        edge_data="graph_examples/multigraphs/triangle_edge_data.csv")
    graph_adj = MultiGraph.from_adjacency_dict(
        "graph_examples/multigraphs/triangle_adjacency_duplicate.txt",
        vertex_data="graph_examples/multigraphs/triangle_vertex_data.csv",
        edge_data="graph_examples/multigraphs/triangle_edge_data.csv")
    graph_mat = MultiGraph.from_adjacency_matrix(
        "graph_examples/multigraphs/triangle_matrix_duplicate.txt",
        vertex_data="graph_examples/multigraphs/triangle_vertex_data.csv",
        edge_data="graph_examples/multigraphs/triangle_edge_data.csv")
    print(graph_edge.edges())
    print(graph_adj.edges())
    assert graph_edge == graph_adj
    assert graph_adj == graph_mat
    assert graph_mat == graph_edge
