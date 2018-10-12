import pytest
import os
from graphtool.graph import *
from graphtool.search import *
from graphtool.path import *


def test_shortest_path():
    graph_files = os.listdir("graph_examples/")
    for path in graph_files:
        if ".txt" in path:
            graph = Graph.from_edge_list("graph_examples/"+path)
            adj = all_shortest_paths(graph)
            N = len(adj)
            for i in range(N):
                for j in range(i):
                    assert adj[i][j] == shortest_path(graph,
                                                      Vertex(i),
                                                      Vertex(j),
                                                      lambda a, b: 1)[0]


def test_dijsktra():
    graph_files = os.listdir("graph_examples/")
    for path in graph_files:
        if ".txt" in path:
            graph = Graph.from_edge_list("graph_examples/"+path)
            adj = all_shortest_paths(graph)
            N = len(adj)
            for i in range(N):
                for j in range(i):
                    assert adj[i][j] == dijkstra(graph,
                                                 Vertex(i),
                                                 Vertex(j))[0]
