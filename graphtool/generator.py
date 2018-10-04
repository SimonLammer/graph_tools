from random import randint, uniform
from graphtool.graph import *


def generate_random_graph(N, V):
    adj = [[0 for i in range(N)] for j in range(N)]
    possible_edges = [(i, j) for j in range(N) for i in range(j)]
    for i in range(V):
        (a, b) = possible_edges.pop(randint(0, len(possible_edges)))
        adj[a][b] = 1
    return Graph.from_adjacency_matrix(adj)


def generate_random_graph_proba(N, p):
    adj = [[1 if uniform(0, 1) < p else 0 for i in range(N)] for j in range(N)]
    return Graph.from_adjacency_matrix(adj)
