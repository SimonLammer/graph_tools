from random import random, randint, uniform, shuffle
from .vertex_edge import Vertex, Edge
from .graph import Graph
from .orientedGraph import OrientedGraph
from .multiGraph import MultiGraph


class GraphGenerator:

    @staticmethod
    def empty(n: int, type: str = None):
        """
        Builds the graph of n vertices an no edges.

        Parameters
        ----------
            'n' : int
                The number of vertices of the graph
            'type' : str
                The type of the graph to be returned.
                Type can be "simple", "oriented" or "multiple"

        Returns
        -------
            A new Graph Object
        """
        if type is None:
            type = "simple"

        graph_dict = dict()
        for i in range(n):
            if type == "multiple":
                graph_dict[Vertex(i)] = []
            else:
                graph_dict[Vertex(i)] = set()
        if type == "oriented":
            return OrientedGraph(graph_dict)
        elif type == "multiple":
            return MultiGraph(graph_dict)
        return Graph(graph_dict)

    @staticmethod
    def cycle(n: int, type: str = None):
        """
        Builds the cycle of size n, with vertex i being linked to
        vertices (i+1)%n and (i-1)%n

        Parameters
        ----------
            'n' : int
                The number of vertices of the graph
            'type' : str
                The type of the graph to be returned.
                Type can be "simple", "oriented" or "multiple"

        Returns
        -------
            A new Graph Object
        """
        g = GraphGenerator.empty(n, type=type)
        for i in range(n):
            g.add_edge(i, (i+1) % n)
        return g

    @staticmethod
    def clique(n: int, type: str = None):
        """
        Builds the fully connected graph of size n, that is the graph of n
        vertices and all possible n(n-1)/2 edges

        Parameters
        ----------
            'n' : int
                The number of vertices of the graph
            'type' : str
                The type of the graph to be returned.
                Type can be "simple", "oriented" or "multiple"

        Returns
        -------
            A new Graph Object
        """
        g = GraphGenerator.empty(n, type=type)
        for i in range(n):
            for j in range(i):
                g.add_edge(i, j)
                g.add_edge(j, i)
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
    def barabasi_albert(n, p, m=None):
        """
        Returns a graph built by the Barabasi-Albert model.

        Parameters
        ---------
            'n' : int
                total number of nodes

            'p' : float in [0;1]
                probability of joining two nodes in the initial small random
                graph. This small graph has size m

            'm' : int
                number of nodes in the small initial erdos-renyi graph.
                If not specified, it will take value n//10

        Returns
        -------
        A new Graph object
        """
        from graphtool.algorithms.search import get_connected_components
        if m is None:
            m = n//10
        G = GraphGenerator.erdos_renyi_proba(m, p)
        comp = get_connected_components(G)
        if len(comp) > 1:
            v1 = list(comp[0].vertices())[0]
            for i in range(1, len(comp)):
                v = list(comp[i].vertices())[0]
                G.add_edge(v1, v)
        assert (len(get_connected_components(G)) == 1)
        for i in range(m, n):
            G.add_vertex(i)
            deg = {j: len(G._dict[j]) for j in G._dict}
            deg_tot = sum(G.vertex_degree())
            for j in range(i):
                if random() < deg[j]/deg_tot:
                    G.add_edge(i, j)
        return G

    @staticmethod
    def configuration_model(seq, allow_multiple=False):
        """
        Returns a graph built by the Molloy-Reed generation process.
        In this process, we feed the degree distribution. Each node is asigned
        a given degree according to this distribution.
        We then merge half-edges uniformly until there is no half-edge left.

        Parameters
        ---------
            'seq' : container
            The degree sequence

            'allow_multiple' : boolean (default to False)
                If set to False, will merge multiple edges between the same
                pair of vertices into a single one

        Returns
        -------
        A new Graph object
        """
        if sum(seq) % 2 != 0:
            raise Exception("The sum of degrees should be even!")
        n = len(seq)
        if allow_multiple:
            graph_dict = {Vertex(i): [] for i in range(n)}
        else:
            graph_dict = {Vertex(i): set() for i in range(n)}
        seq2 = []
        for i in range(n):
            seq2 += [i]*seq[i]
        m = len(seq2)//2
        shuffle(seq2)
        seq2 = [Vertex(x) for x in seq2]
        for i in range(m):
            if allow_multiple:
                graph_dict[seq2[2*i]].append(seq2[2*i+1])
            else:
                graph_dict[seq2[2*i]].add(seq2[2*i+1])
        if allow_multiple:
            return MultiGraph(graph_dict)
        return Graph(graph_dict)
