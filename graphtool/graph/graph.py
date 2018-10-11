from random import random, randint, uniform
from .vertex_edge import Vertex, Edge
from ._parsing import *

class Graph:
    """
    A class representing a graph.
    Data are stored as adjacency lists stored in a dictionnaryself.
    Edges in the class graph are not oriented. For oriented edges, please use
    the class OrientedGraph
    """

    def __init__(self, _graph_dict, _edges=None, _matrix=None):
        """
        Initialization function. Is not meant to be called as it is.
        """
        self._dict = _graph_dict
        self._edges = _edges
        self._matrix = _matrix

    def __eq__(self, other):
        return self._dict == other._dict

    # --------------- Initialization methods --------------------------
    @staticmethod
    def from_edge_list(l, vertex_data:str = None, edge_data:str = None):
        """
        Imports a graph from a txt file containing an edge list

        Returns
        -------
        A new Graph object
        """
        if isinstance(l, str):
            # Load from a file
            edges = []
            with open(l, 'r') as f:
                for s in f.readlines():
                    s = s.strip().split()
                    a, b = Vertex(s[0]), Vertex(s[1])
                    edges.append(Edge(a, b))
        else:
            edges = l
        graph_dict = dict()
        for edge in edges:
            if edge.start not in graph_dict:
                graph_dict[edge.start] = set([edge.end])
            else:
                graph_dict[edge.start].add(edge.end)
            if edge.end not in graph_dict:
                graph_dict[edge.end] = set([edge.start])
            else:
                graph_dict[edge.end].add(edge.start)
        return Graph(graph_dict)

    @staticmethod
    def from_adjacency_dict(d, vertex_data:str = None, edge_data:str = None):
        """
        Imports a graph from a txt file containing an adjacency list

        Returns
        -------
        A new Graph object
        """
        if isinstance(d, str):  # Load from a file
            graph_dict = dict()
            with open(d, 'r') as f:
                for line in f.readlines():
                    line = line.strip().split()
                    v, adj_list = Vertex(line[0]), line[1:]
                    for adj in adj_list:
                        adj = Vertex(adj)
                        if v in graph_dict:
                            graph_dict[v].add(adj)
                        else:
                            graph_dict[v] = set([adj])
                        if adj in graph_dict:
                            graph_dict[adj].add(v)
                        else:
                            graph_dict[adj] = set([v])
            return Graph(graph_dict)
        else:
            return Graph(d)

    @staticmethod
    def from_adjacency_matrix(m, vertex_data:str = None, edge_data:str = None):
        """
        Imports a graph from a txt file containing an adjacency matrx

        Returns
        -------
        A new Graph object
        """
        adj_mat = None
        if isinstance(m, str):  # Load from a file
            with open(m, 'r') as f:
                adj_mat = [l.strip().split() for l in f.readlines()]
        else:
            adj_mat = m
        n = len(adj_mat)
        graph_dict = dict()
        edges = set()
        for i in range(n):
            v = Vertex(str(i))
            graph_dict[v] = set()
        for i in range(n):
            for j in range(n):
                vi, vj = Vertex(str(i)), Vertex(str(j))
                if float(adj_mat[i][j]) != 0:
                    graph_dict[vi].add(vj)
                    graph_dict[vj].add(vi)
                    edges.add(Edge(vi, vj, weight=float(adj_mat[i][j])))
        return Graph(graph_dict, edges)

    @staticmethod
    def empty(n:int):
        """
        Builds the graph of n vertices an no edges

        Returns
        -------
        A new Graph Object
        """
        graph_dict = dict()
        for i in range(n):
            graph_dict[Vertex(str(i))] = set()
        return Graph(graph_dict)

    @staticmethod
    def cycle(n:int):
        """
        Builds the cycle of size n, with vertex i being linked to
        vertices (i+1)%n and (i-1)%n

        Returns
        -------
        A new Graph Object
        """
        g = Graph.empty(n)
        for i in range(n-1):
            g.add_edge(str(i), str(i+1))
        g.add_edge(str(n-1), "0")
        return g

    @staticmethod
    def clique(n:int):
        """
        Builds the fully connected graph of size n, that is the graph of n
        vertices and all possible n(n-1)/2 edges

        Returns
        -------
        A new Graph Object
        """
        g = Graph.empty(n)
        for i in range(n):
            for j in range(i):
                g.add_edge(str(i), str(j))
        return g

    @staticmethod
    def erdos_renyi_proba(n:int, p:float):
        """
        Generates a graph through the Erdös-Renyi model.

        Parameters
        ----------
        'n' : int
            Number of vertices

        'p' : float between 0 and 1
            The probability for each edge to be present in the graph

        Returns
        -------
        A new Graph Object
        """
        p = min(max(p, 0), 1)
        g = Graph.empty(n)
        for i in range(n):
            for j in range(i):
                if random() <= p:
                    g.add_edge(str(i), str(j))
        return g

    @staticmethod
    def erdos_renyi_edge(n:int, l:int):
        """
        Generates a graph through the Erdös-Renyi model with fixed number
        of edges

        Parameters
        ----------
        'n' : int
            Number of vertices

        'l' : int
            Number of edges

        Returns
        -------
        A new Graph Object
        """
        adj = [[0 for i in range(n)] for j in range(n)]
        possible_edges = [(i, j) for j in range(n) for i in range(j)]
        for i in range(l):
            (a, b) = possible_edges.pop(randint(0, len(possible_edges) - 1))
            adj[a][b] = 1
        return Graph.from_adjacency_matrix(adj)
    # ------------- Exportation methods -----------------

    def export_as_edge_list(self, filename: str) -> None:
        """
        Exports the graph in form of an edge list

        Parameters
        ----------
        'filename' : string
            the relative path of the file to write back the data
        """
        with open(filename, 'w') as f:
            for e in self.edges():
                f.write(str(e.start)+" "+str(e.end)+"\n")

    def export_as_adjacency_dict(self, filename: str) -> None:
        """
        Exports the graph in form of an adjacency list

        Parameters
        ----------
        'filename' : string
            the relative path of the file to write back the data
        """
        with open(filename, 'w') as f:
            for v in self._dict:
                f.write(str(v)+" ")
                for neigh in self._dict[v]:
                    f.write(str(neigh)+" ")
                f.write("\n")

    def export_as_adjacency_matrix(self, filename: str) -> None:
        """
        Exports the graph in form of an adjacency matrix

        Parameters
        ----------
        'filename' : string
            the relative path of the file to write back the data
        """
        with open(filename, 'w') as f:
            mat = self.adjacency_matrix()
            n = len(mat)
            for i in range(n):
                string = ""
                for j in range(n):
                    string += str(mat[i][j])+" "
                string += "\n"
                f.write(string)

    # ---------------- Getters and setters -----------------------------

    def vertices(self):
        """
        Getter on the vertices of the graph

        Returns
        -------
        An iterator over the vertices of the graph
        """
        return self._dict.keys()

    def _generate_edges(self):
        """
        Generates the set of edges of the graph.
        This set is then stored into the self._edges attribute
        """
        self._edges = set()
        for a in self.vertices():
            for b in self._dict[a]:
                if(hash(b) < hash(a)):
                    continue
                self._edges.add(Edge(start=a, end=b))

    def edges(self):
        """
        Getter on the edges of the graph

        Returns
        -------
        An iterator over the edges of a the graph
        """
        if self._edges is None:
            self._generate_edges()
        return self._edges

    def _generate_adjacency(self):
        """
        Generates the adjacency matrix of the graph.
        This matrix is then stored into the self._matrix attribute
        """
        n = len(self._dict)  # number of vertices
        numbering = dict([(x, i) for (i, x) in enumerate(self._dict.keys())])
        # assign a number between 0 and n to all vertices
        self._matrix = [[0 for j in range(n)] for i in range(n)]
        if self._edges is not None:
            for e in self.edges():
                a, b = numbering[e.start], numbering[e.end]
                self._matrix[a][b] = e.weight
        else:  # matrix cannot be weighted
            for e in self.edges():
                a, b = numbering[e.start], numbering[e.end]
                self._matrix[a][b] = 1

    def adjacency_matrix(self):
        """
        Computes and return the adjacency matrix of the graph.

        Returns
        -------
        A numpy array of shape (N*N) where N is the number of vertices
        in the graph
        """
        if self._matrix is None:
            self._generate_adjacency()
        return self._matrix

    def get_neighbours(self, v):
        if not isinstance(v, Vertex):
            v = Vertex(v)
        return graph._dict[v]

    # ---------------  Modification of the data ------------------------
    def add_vertex(self, v) -> None:
        """
        Adds a new vertex to the graph

        Parameters
        ----------
        'v' : a Vertex object or a name for a Vertex
            If a name is provided, the method will build a Vertex with the name
            field being v.
        """
        self._matrix = None  # reset adjacency matrix
        if not isinstance(v, Vertex):
            v = Vertex(v)
        if v not in self._dict:
            self._dict[v] = set()

    def remove_vertex(self, v) -> None:
        """
        Removes a vertex from the graph. If the given vertex is not present,
        this method does not do anything.

        Parameters
        ----------
        'v' : a Vertex object or a name for a Vertex
            If a name is provided, the method will build a Vertex with the name
            field being v.
        """
        self._edges = None  # reset edges set
        self._matrix = None  # reset adjacency
        if not isinstance(v, Vertex):
            v = Vertex(v)
        if v in self._dict:
            self._dict.pop(v, None)
        for x in self._dict:
            self._dict[x].discard(v)

    def add_edge(self, *args):
        """
        Adds an edge in the graph. If one or both ends of the edge are not
        present in the graph, the coresponding vertices are added.

        Parameters
        ----------
        'args' : Edge | (Vertex, Vertex) | (name, name)
            The data needed to generate the edge. Can be directly an Edge
            object, or any pair of Vertex or vertex names.
        """
        e = Edge(args)
        if e.start not in self._dict:
            self._dict[e.start] = set([e.end])
        else:
            self._dict[e.start].add(e.end)
        if e.end not in self._dict:
            self._dict[e.end] = set([e.start])
        else:
            self._dict[e.end].add(e.start)
        if self._edges is not None:
            self._edges.add(e)

    def remove_edge(self, *args):
        """
        Removes an edge from the graph.

        Parameters
        ----------
        'args' : Edge | (Vertex, Vertex) | (name, name)
            The data needed to generate the edge. Can be directly an Edge
            object, or any pair of Vertex or vertex names.
        """
        e = Edge(args)
        self._dict[e.start].discard(e.end)
        self._dict[e.end].discard(e.start)
        if self._edges is not None:
            self._edges.discard(e)

    # ---------------- Stats computations -----------------------------
    def vertex_degree(self):
        """
        Returns the list of degrees of the vertices in the graph.

        Returns
        -------
        A list of integers
        """
        return [len(self._dict[v]) for v in self.vertices()]

    def degree_sequence(self):
        """
        Returns the list of degrees of the vertices in the graph sorted in
        decreasing order

        Returns
        -------
        A list of integers sorted in decreasing order
        """
        degree_list = self.vertex_degree()
        degree_list.sort(reverse=True)
        return degree_list

    def find_isolated_vertices(self):
        """
        Returns the list of isolated vertices, that is vertices with degree 0

        Returns
        -------
        A list of the names of vertices that have zero degree
        """
        return [v.name for v in self.vertices() if len(self._dict[v]) == 0]

    def density(self):
        """
        Computes the density of the graph, defined as the proportion of edges
            = {number of edges}/{total possible number of edges}
            = 2*{number of edges}/(N(N-1))

        Returns
        -------
        The density of the graph
        """
        e_nb = len(self.edges())
        v_nb = len(self.vertices())
        possible_edges = v_nb*(v_nb-1)/2
        return e_nb / possible_edges
