import pytest
from graphtool.graph import Graph, Edge


def test_test():
    assert True


def test_graph_from_edge_list():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    graph2 = Graph.from_edge_list([Edge(0, 1), Edge(1, 2), Edge(2, 0)])
    print(graph1._dict)
    print(graph2._dict)


def test_find_isolated_vertices():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.find_isolated_vertices() == []


def test_density():
    graph1 = Graph.from_edge_list("graph_examples/triangle_edge_list.txt")
    assert graph1.density() == 1
