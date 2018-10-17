from random import random, randint, uniform
from .vertex_edge import Vertex, Edge
from .graph import Graph
from ._parsing import *


class OrientedGraph:
    """
    A class representing an oriented graph.
    Data are stored as adjacency lists stored in a dictionnaryself.
    Edges in this class are oriented.
    """

    def __init__(self, _graph_dict, _edges=None, _matrix=None):
        """
        Initialization function. Is not meant to be called as it is.

        self._dict_in : Vertex -> set of vertices that can reach v
        self._dict_out : Vertex -> set of vertices reachable from v
        self._edges : Vertex pair -> corresponding Edge
        self._matrix : adjacency matrix
        """
        self._dict_out = _graph_dict
        self._dict_in = {v: set() for v in _graph_dict}
        for v in _graph_dict:
            for u in _graph_dict[v]:
                self._dict_in[u].add(v)
        self._edges = _edges
        self._matrix = _matrix

    def __eq__(self, other):
        return (self._dict_in == other._dict_in
                and self._dict_out == other._dict_out)

    def __str__(self):
        return str(self._dict_in)+"\n"+str(self._dict_out)

    def __len__(self):
        """
        Number of vertices in the graph
        """
        return len(self._dict_out)

    # --------------- Initialization methods --------------------------

    @staticmethod
    def from_edge_list(l, vertex_data: str = None, edge_data: str = None):
        """
        Imports a graph from a txt file containing an edge list

        Returns
        -------
        A new OrientedGraph object
        """
        if vertex_data is not None:
            vertex_data = parse_node_data(vertex_data)
        if edge_data is not None:
            edge_data = parse_edge_data(edge_data, oriented=True)

        edges = dict()
        if isinstance(l, str):
            # Load from a file
            with open(l, 'r') as f:
                for s in f.readlines():
                    s = s.strip().split()
                    xa, xb = int(s[0]), int(s[1])
                    if vertex_data is None:
                        a, b = Vertex(xa), Vertex(xb)
                    else:
                        a, b = vertex_data[xa], vertex_data[xb]
                    if edge_data is None:
                        e = Edge(a, b, oriented=True)
                        edges[(a, b)] = e
                    else:
                        e = edge_data.get((a, b), None)
                        edges[(a, b)] = e
        else:
            for e in l:
                e = Edge(e)
                edges[(e["start"], e["end"])] = e
                if not e.oriented:
                    edges[(e["end"], e["start"])] = Edge.revert(e)
        graph_dict = dict()
        for key in edges:
            edge = edges[key]
            if edge.start not in graph_dict:
                graph_dict[edge.start] = set([edge.end])
            else:
                graph_dict[edge.start].add(edge.end)
        return OrientedGraph(graph_dict, _edges=edges)

    @staticmethod
    def from_adjacency_dict(d, vertex_data: str = None, edge_data: str = None):
        """
        Imports a graph from a txt file containing an adjacency list

        Returns
        -------
        A new OrientedGraph object
        """
        edges = None
        if isinstance(d, str):  # Load from a file
            if vertex_data is not None:
                vertex_data = parse_node_data(vertex_data)
            if edge_data is not None:
                edge_data = parse_edge_data(edge_data, oriented=True)
                edges = dict()
            graph_dict = dict()
            with open(d, 'r') as f:
                for line in f.readlines():
                    line = line.strip().split()
                    if vertex_data is None:
                        v = Vertex(int(line[0]))
                    else:
                        v = vertex_data[int(line[0])]
                    adj_list = line[1:]
                    for adj in adj_list:
                        if vertex_data is None:
                            adj = Vertex(int(adj))
                        else:
                            adj = vertex_data[int(adj)]
                        if v in graph_dict:
                            graph_dict[v].add(adj)
                        else:
                            graph_dict[v] = set([adj])
                        if edge_data is not None:
                            edges[(v, adj)] = edge_data[(v, adj)]
            return OrientedGraph(graph_dict, _edges=edges)
        else:
            return OrientedGraph(d)

    @staticmethod
    def from_adjacency_matrix(m, vertex_data: str = None,
                              edge_data: str = None):
        """
        Imports a graph from a txt file containing an adjacency matrx

        Returns
        -------
        A new OrientedGraph object
        """
        if vertex_data is not None:
            vertex_data = parse_node_data(vertex_data)
        if edge_data is not None:
            edge_data = parse_edge_data(edge_data, oriented=True)

        adj_mat = None
        if isinstance(m, str):  # Load from a file
            with open(m, 'r') as f:
                adj_mat = [l.strip().split() for l in f.readlines()]
        else:
            adj_mat = m
        n = len(adj_mat)
        graph_dict = dict()
        edges = dict()
        for i in range(n):
            for j in range(n):
                if vertex_data is None:
                    vi, vj = Vertex(i), Vertex(j)
                else:
                    vi, vj = vertex_data[i], vertex_data[j]
                if float(adj_mat[i][j]) != 0:
                    if (vi not in graph_dict):
                        graph_dict[vi] = set([vj])
                    else:
                        graph_dict[vi].add(vj)
                    if edge_data is not None:
                        e = edge_data.get((vi, vj), Edge(vi, vj))
                        edges[(i, j)] = e
                    else:
                        edges[(i, j)] = Edge(vi, vj)
        return OrientedGraph(graph_dict, _edges=edges)

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
            for v in self._dict_out:
                f.write(str(v)+" ")
                for neigh in self._dict_out[v]:
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

    def subgraph(self, vertices):
        """
        Extract a subgraph of the graph, containing the relevant vertices
        and edges

        Parameters
        ----------
        'vertices' : a container
            Contains the relevant vertices. If it is not a set, is converted
            into a set

        Returns
        -------
        A new OrientedGraph object
        """
        vertices = set([Vertex(v) for v in vertices])
        graph_dict = {v: set() for v in vertices}
        edges = None
        if self._edges is not None:
            edges = dict()
        for v in vertices:
            for u in vertices:
                if v != u and u in self._dict_out[v]:
                    graph_dict[v].add(u)
                    if edges is not None:
                        edges[(v, u)] = self._edges[(v, u)]
        return OrientedGraph(graph_dict, _edges=edges)

    # ---------------- Getters and setters -----------------------------

    def symetrize(self):
        """
        Builds a non-oriented graph by symetrizing every edge of the oriented
        graph.

        Returns
        -------
        A Graph object
        """
        edges = None
        if self._edges is not None:
            edges = dict()
            for (u, v) in self._edges:
                edges[(u, v)] = self._edges[(u, v)]
                edges[(v, u)] = self._edges[(u, v)]
        graph_dict = dict()
        for u in self._dict_out:
            graph_dict[u] = self._dict_out[u] | self._dict_in[u]
        return Graph(graph_dict, edges)

    def vertices(self):
        """
        Getter on the vertices of the graph

        Returns
        -------
        An iterator over the vertices of the graph
        """
        return self._dict_out.keys()

    def _generate_edges(self):
        """
        Generates the set of edges of the graph.
        This set is then stored into the self._edges attribute
        """
        self._edges = dict()
        for a in self.vertices():
            for b in self._dict_out[a]:
                self._edges[(a, b)] = Edge(a, b)

    def edges(self):
        """
        Getter on the edges of the graph

        Returns
        -------
        An iterator over the edges of a the graph
        """
        if self._edges is None:
            self._generate_edges()
        return set(self._edges.values())

    def _generate_adjacency(self):
        """
        Generates the adjacency matrix of the graph.
        This matrix is then stored into the self._matrix attribute
        """
        try:
            n = len(self._dict_out)  # number of vertices
            # assign a number between 0 and n to all vertices
            self._matrix = [[0 for j in range(n)] for i in range(n)]
            for u in self._dict_out:
                for v in self._dict_out[u]:
                    self._matrix[u.id][v.id] = 1
        except Exception as e:
            # roll-back operations on matrix before continuing
            self._matrix = None
            raise e

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
        """
        Returns the vertices that are adjacent to v, ie the set of u such that
        the oriented edge (v,u) exists

        Parameters
        ----------
        'v' : A Vertex object or an integer (vertex id)
            The vertex from which to extract the neighbourhood

        Returns
        -------
        The set of out-neighbours of v
        """
        if not isinstance(v, Vertex):
            assert isinstance(v, int)
            v = Vertex(v)
        return self._dict_out[v]

    def get_neighbours_in(self, v):
        """
        Returns the vertices that can lead to v, ie the set of u such that the
        oriented edge (u,v) exists.

        Parameters
        ----------
        'v' : A Vertex object or an integer (vertex id)
            The vertex from which to extract the neighbourhood

        Returns
        -------
        The set of in-neighbours of v
        """
        if not isinstance(v, Vertex):
            assert isinstance(v, int)
            v = Vertex(v)
        return self._dict_in[v]

    def get_neighbours_edge(self, v):
        """
        Returns the edges of the graph that start from v

        Parameters
        ----------
        'v' : A Vertex object or an integer (vertex id)
            The vertex from which to extract the neighbourhood

        Returns
        -------
        The set of neighbours of v
        """
        if not isinstance(v, Vertex):
            assert isinstance(v, int)
            v = Vertex(v)
        if self._edges is None:
            return set([Edge(v, u) for u in self._dict_out[v]])
        else:
            output = set()
            for e in self.edges():
                if e.start == v:
                    output.add(e)
            return output

    def get_neighbours_edge_in(self, v):
        """
        Returns the edges of the graph that lead to v

        Parameters
        ----------
        'v' : A Vertex object or an integer (vertex id)
            The vertex from which to extract the neighbourhood

        Returns
        -------
        The set of neighbours of v
        """
        if not isinstance(v, Vertex):
            assert isinstance(v, int)
            v = Vertex(v)
        if self._edges is None:
            return set([Edge(u, v) for u in self._dict_in[v]])
        else:
            output = set()
            for e in self.edges():
                if e.end == v:
                    output.add(e)
            return output

    # ---------------  Modification of the data ------------------------
    def add_vertex(self, v) -> None:
        """
        Adds a new vertex to the graph

        Parameters
        ----------
        'v' : a Vertex object or a integer for a Vertex id
            If an integer is provided, the method will build a Vertex with the
            id field being v.
        """
        self._matrix = None  # reset adjacency matrix
        if not isinstance(v, Vertex):
            assert isinstance(v, int)
            v = Vertex(v)
        if v not in self._dict_out:
            self._dict_out[v] = set()
            self._dict_in[v] = set()

    def remove_vertex(self, v) -> None:
        """
        Removes a vertex from the graph. If the given vertex is not present,
        this method does not do anything.

        Parameters
        ----------
        'v' : a Vertex object or a integer for a Vertex id
            If an integer is provided, the method will build a Vertex with the
            id field being v.
        """
        if not isinstance(v, Vertex):
            assert isinstance(v, int)
            v = Vertex(v)

        if self._edges is not None:
            for e in self._edges:
                if self._edges[e].start == v or self._edges[e].end == v:
                    self._edges.pop(e, None)

        self._matrix = None  # reset adjacency

        if v in self._dict_in:
            self._dict_in.pop(v, None)
            self._dict_out.pop(v, None)
        for x in self._dict_out:
            self._dict_out[x].discard(v)
            self._dict_in[x].discard(v)

    def add_edge(self, *args) -> None:
        """
        Adds an edge in the graph. If one or both ends of the edge are not
        present in the graph, the coresponding vertices are added.

        Parameters
        ----------
        'args' : Edge | (Vertex, Vertex) | (name, name)
            The data needed to generate the edge. Can be directly an Edge
            object, or any pair of Vertex or vertex names.
        """
        e = Edge(args, oriented=True)
        if e.start not in self._dict_out:
            self._dict_out[e.start] = set([e.end])
        else:
            self._dict_out[e.start].add(e.end)
        if e.end not in self._dict_in:
            self._dict_in[e.end] = set([e.start])
        else:
            self._dict_in[e.end].add(e.start)
        if self._edges is not None:
            self._edges[(e.start, e.end)] = e

    def remove_edge(self, *args) -> None:
        """
        Removes an edge from the graph.

        Parameters
        ----------
        'args' : Edge | (Vertex, Vertex) | (name, name)
            The data needed to generate the edge. Can be directly an Edge
            object, or any pair of Vertex or vertex names.
        """
        e = Edge(args)
        self._dict_out[e.start].discard(e.end)
        self._dict_in[e.end].discard(e.start)
        if self._edges is not None:
            self._edges.pop((e.start, e.end), None)

# ---------------- Stats computations -----------------------------
    def get_sources(self):
        """
        Gets the list of vertices that have in-degree 0
        """
        assert 1 == 0
        return []

    def get_sinks(self):
        """
        Gets the list of vertices that have out degree 0
        """
        assert 1 == 0
        return []
