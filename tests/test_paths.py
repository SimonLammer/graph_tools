import pytest
import random
import os
from graphtool.graph import *
from graphtool.algorithms import *
from utils import *

graph_files = ["graph_100n_1000m.txt",
               "triangle_edge_list.txt", "not_connex_10n.txt"]


def test_shortest_path():
    for g in graph_files:
        graph = Graph.from_edge_list("graph_examples/"+g)
        adj = all_shortest_paths(graph)
        N = len(adj)
        for a in range(10):
            i = random.randint(0, N-1)
            j = random.randint(0, N-1)
            length, fullpath = shortest_path(graph,
                                             Vertex(i),
                                             Vertex(j),
                                             lambda a, b: 0)
            # print(i, j, adj[i][j], length, fullpath)
            assert adj[i][j] == length


def test_dijsktra():
    for g in graph_files:
        graph = Graph.from_edge_list("graph_examples/"+g)
        adj = all_shortest_paths(graph)
        N = len(adj)
        for a in range(10):
            i = random.randint(0, N-1)
            j = random.randint(0, N-1)
            assert adj[i][j] == dijkstra(graph,
                                         Vertex(i),
                                         Vertex(j))[0]
