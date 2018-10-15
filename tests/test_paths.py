import pytest
import os
from graphtool.graph import *
from graphtool.algorithms import *

graph_files = ["graph_100n_1000m.txt","triangle_edge_list.txt"]
#graph_files = ["triangle_edge_list.txt"]

def test_shortest_path():
    for g in graph_files:
        graph = Graph.from_edge_list("graph_examples/"+g)
        adj = all_shortest_paths(graph)
        N = len(adj)
        for i in range(N):
            for j in range(i):
                length, fullpath = shortest_path(graph,
                                Vertex(i),
                                Vertex(j),
                                lambda a, b: 0)
                print(i, j, adj[i][j], length, fullpath)
                assert adj[i][j] == length


def test_dijsktra():
    for g in graph_files:
        graph = Graph.from_edge_list("graph_examples/"+g)
        adj = all_shortest_paths(graph)
        N = len(adj)
        for i in range(N):
            for j in range(i):
                assert adj[i][j] == dijkstra(graph,
                                             Vertex(i),
                                             Vertex(j))[0]
