from random import random, randint, uniform
from .vertex_edge import Vertex, Edge
from ._parsing import *


class OrientedGraph:
    """
    TODO
    """

    def __init__(self, _dict, _edges = None, _adjacency = None):
        pass

    """
    @staticmethod
    def erdos_renyi_edge(N, V):
        adj = [[0 for i in range(N)] for j in range(N)]
        possible_edges = [(i, j) for j in range(N) for i in range(j)]
        for i in range(V):
            (a, b) = possible_edges.pop(randint(0, len(possible_edges) - 1))
            adj[a][b] = 1
        return Graph.from_adjacency_matrix(adj)

    def erdos_renyi_proba(N, p):
        adj = [[1 if uniform(0, 1) < p else 0 for i in range(N)]
               for j in range(N)]
        return Graph.from_adjacency_matrix(adj)
    """
