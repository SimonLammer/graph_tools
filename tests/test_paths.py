import pytest
import os
from graphtool.graph import *
from graphtool.search import *
from graphtool.path import *


def test_shortest_path():
    graph_files = os.listdir("graph_examples/")
    for path in graph_files:
        graph = Graph.from_edge_list("graph_examples/"+path)
        adj = all_shortest_paths(graph)
        N = len(adj)
        for i in range(N):
            for j in range(i):
                assert adj[i][j] == shortest_path(graph,
                                                  Vertex(str(i)),
                                                  Vertex(str(j)),
                                                  lambda a, b: 1)
