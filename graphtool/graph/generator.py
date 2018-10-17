from random import random, randint, uniform, shuffle
from .vertex_edge import Vertex, Edge
from .graph import Graph
from .orientedGraph import OrientedGraph


class GraphGenerator:

    @staticmethod
    def empty(n: int, oriented: bool = False):
        """
        Builds the graph of n vertices an no edges

        Returns:
            A new Graph Object
        """
        graph_dict = dict()
        for i in range(n):
            graph_dict[Vertex(i)] = set()
        if oriented:
            return OrientedGraph(graph_dict)
        return Graph(graph_dict)

    @staticmethod
    def cycle(n: int, oriented: bool = False):
        """
        Builds the cycle of size n, with vertex i being linked to
        vertices (i+1)%n and (i-1)%n

        Returns:
            A new Graph Object
        """
        g = GraphGenerator.empty(n, oriented)
        for i in range(n):
            g.add_edge(i, (i+1) % n)
        return g

    @staticmethod
    def clique(n: int, oriented: bool = False):
        """
        Builds the fully connected graph of size n, that is the graph of n
        vertices and all possible n(n-1)/2 edges

        Returns:
            A new Graph Object
        """
        g = GraphGenerator.empty(n)
        for i in range(n):
            for j in range(i):
                g.add_edge(i, j)
        return g

    @staticmethod
    def erdos_renyi_proba(n: int, p: float):
        """
        Generates a graph through the Erdös-Renyi model.

        Parameters:
            'n' : int
                Number of vertices

            'p' : float between 0 and 1
                The probability for each edge to be present in the graph

        Returns:
            A new Graph Object
        """
        p = min(max(p, 0), 1)
        g = GraphGenerator.empty(n)
        for i in range(n):
            for j in range(i):
                if random() <= p:
                    g.add_edge(i, j)
        return g

    @staticmethod
    def erdos_renyi_edge(n: int, l: int):
        """
        Generates a graph through the Erdös-Renyi model with fixed number
        of edges

        Parameters:
            'n' : int
                Number of vertices

            'l' : int
                Number of edges

        Returns:
            A new Graph Object
        """
        adj = [[0 for i in range(n)] for j in range(n)]
        possible_edges = [(i, j) for j in range(n) for i in range(j)]
        for i in range(l):
            (a, b) = possible_edges.pop(randint(0, len(possible_edges) - 1))
            adj[a][b] = 1
        return Graph.from_adjacency_matrix(adj)

    @staticmethod
    def chung_lu(seq):
        """
        TODO
        """
        if sum(seq) % 2 != 0:
            raise Exception("The sum of degrees should be even!")
        k_tot = sum(seq)
        n = len(seq)
        G = GraphGenerator.empty(n)
        for i in range(n):
            for j in range(i):
                if seq[i]*seq[j]/k_tot > random():
                    G.add_edge(i, j)
        return G

    @staticmethod
    def molloy_reed(seq):
        """
        TODO
        """
        if sum(seq) % 2 != 0:
            raise Exception("The sum of degrees should be even!")
        n = len(seq)
        G = GraphGenerator.empty(n)
        seq2 = []
        for i in range(n):
            seq2 += [i]*seq[i]
        m = len(seq2)//2
        shuffle(seq2)
        for i in range(m):
            if seq2[2*i] != seq2[2*i+1]:
                G.add_edge(seq2[2*i], seq2[2*i+1])
        return G
