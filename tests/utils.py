import pytest
from graphtool.graph import *
from graphtool.algorithms import *


@pytest.fixture
def triangle():
    a, b, c = Vertex(0), Vertex(1), Vertex(2)
    return Graph.from_edge_list([Edge(a, b), Edge(b, c), Edge(c, a)])


@pytest.fixture
def oriented_triangle():
    return OrientedGraph.from_edge_list([Edge(0, 1, oriented=True),
                                         Edge(1, 2, oriented=True),
                                         Edge(2, 0, oriented=True)])


@pytest.fixture
def multi_triangle():
    return MultiGraph.from_edge_list([Edge(0, 1), Edge(1, 2),
                                      Edge(0, 1), Edge(2, 0)])
