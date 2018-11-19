from .vertex_edge import Vertex, Edge
from .graph import Graph
from ._parsing import *


class MultiGraph(Graph):
    """
    A class representing a graph.
    Data are stored as adjacency lists stored in a dictionnary
    """

    def __init__(self, _graph_dict, _edges=None, _matrix=None):
        """
        Initialization function. Is not meant to be called as it is.

        Parameters:
            self._dict : Vertex -> set of neighbours vertices
            self._edges : Vertex pair -> corresponding Edge
            self._matrix : adjacency matrix
        """
        self._dict = _graph_dict
        self._edges = _edges
        self._matrix = _matrix

    def __eq__(self, other):
        if (self._dict.keys() != other._dict.keys()):
            return False
        a = self.edges()
        b = other.edges()
        a.sort()
        b.sort()
        return a == b

    # --------------- Initialization methods --------------------------

    @staticmethod
    def from_edge_list(l, vertex_data: str = None, edge_data: str = None):
        """
        Imports a graph from a txt file containing an edge list

        Returns
        -------
            A new Graph object
        """
        if vertex_data is not None:
            vertex_data = parse_node_data(vertex_data)
        if edge_data is not None:
            edge_data = parse_edge_data(edge_data)

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
                        e = Edge(a, b)
                        if (a, b) not in edges:
                            edges[(a, b)] = [e]
                        else:
                            edges[(a, b)].append(e)
                        if (b, a) not in edges:
                            edges[(b, a)] = [e]
                        else:
                            edges[(b, a)].append(e)

                    else:
                        e = edge_data.get((a, b), None)
                        if e is None:
                            e = edge_data.get((b, a), [Edge(a, b)])
                        edges[(a, b)] = e
        else:
            for e in l:
                e = Edge(e)
                if (e["start"], e["end"]) not in edges:
                    edges[(e["start"], e["end"])] = [e]
                else:
                    edges[(e["start"], e["end"])].append(e)
        graph_dict = dict()
        for key in edges:
            for edge in edges[key]:
                if edge.start not in graph_dict:
                    graph_dict[edge.start] = [edge.end]
                else:
                    graph_dict[edge.start].append(edge.end)
                if edge.end not in graph_dict:
                    graph_dict[edge.end] = [edge.start]
                else:
                    graph_dict[edge.end].append(edge.start)
        for key in list(edges.keys()):
            a, b = key
            edges[(b, a)] = edges[(a, b)]
        return MultiGraph(graph_dict, _edges=edges)

    @staticmethod
    def from_adjacency_dict(d, vertex_data: str = None, edge_data: str = None):
        """
        Imports a graph from a txt file containing an adjacency list

        Returns
        -------
            A new Graph object
        """
        if vertex_data is not None:
            vertex_data = parse_node_data(vertex_data)
        edges = None
        if edge_data is not None:
            edge_data = parse_edge_data(edge_data)
            edges = dict()
            for (a, b) in edge_data:
                edges[(a, b)] = edge_data[(a, b)]
                edges[(b, a)] = edge_data[(a, b)]

        if isinstance(d, str):  # Load from a file
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
                            v = vertex_data[int(adj)]
                        if v in graph_dict:
                            graph_dict[v].append(adj)
                        else:
                            graph_dict[v] = [adj]
            return MultiGraph(graph_dict, _edges=edges)
        else:
            return MultiGraph(d, _edges=edges)

    @staticmethod
    def from_adjacency_matrix(m, vertex_data: str = None,
                              edge_data: str = None):
        """
        Imports a graph from a txt file containing an adjacency matrix

        Returns
        -------
            A new Graph object
        """
        if vertex_data is not None:
            vertex_data = parse_node_data(vertex_data)
        if edge_data is not None:
            edge_data = parse_edge_data(edge_data)

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
            v = Vertex(i)
            graph_dict[v] = []
        for i in range(n):
            for j in range(i):
                if vertex_data is None:
                    vi, vj = Vertex(i), Vertex(j)
                else:
                    vi, vj = vertex_data[i], vertex_data[j]
                if int(adj_mat[i][j]) != 0:
                    n_edge_ij = abs(int(adj_mat[i][j]))
                    for k in range(n_edge_ij):
                        graph_dict[vi].append(vj)
                    if edge_data is not None:
                        e = edge_data.get((vi, vj), None)
                        if e is None:
                            e = edge_data.get(
                                (vj, vi), [Edge(vi, vj)]*n_edge_ij)
                        edges[(i, j)] = e
                        edges[(j, i)] = e
                    else:
                        e = [Edge(vi, vj)]*n_edge_ij
                        edges[(i, j)] = e
                        edges[(j, i)] = e
        return MultiGraph(graph_dict, _edges=edges)

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
        A new Graph object
        """
        vertices = set([Vertex(v) if isinstance(v, int)
                        else v for v in vertices])
        graph_dict = {v: [] for v in vertices}
        edges = None
        if self._edges is not None:
            edges = dict()
        for v in vertices:
            for u in vertices:
                if v != u and u in self._dict[v]:
                    graph_dict[v].append(u)
                    graph_dict[u].append(v)
                    if edges is not None:
                        edges[(u, v)] = self._edges[(u, v)]
                        edges[(v, u)] = self._edges[(v, u)]
        return MultiGraph(graph_dict, _edges=edges)

    def renumber(self):
        """
        Returns a copy of the graph where all the vertices have been renumbered
        from 0 to n. Does not copy edge or vertex data, but only
        the combinatorial structure

        Returns
        -------
        A Graph Object
        """
        graph_dict = dict()
        vertices = {x: Vertex(i)
                    for (i, x) in enumerate(list(self.vertices()))}
        for v in self._dict:
            graph_dict[vertices[v]] = []
            for u in self._dict[v]:
                graph_dict[vertices[v]].append(vertices[u])
        return MultiGraph(graph_dict)

    # ---------------- Getters and setters -----------------------------

    def vertices(self):
        """
        Getter on the vertices of the graph

        Returns:
            An iterator over the vertices of the graph
        """
        return self._dict.keys()

    def _generate_edges(self):
        """
        Generates the set of edges of the graph.
        This set is then stored into the self._edges attribute
        """
        self._edges = dict()
        for a in self.vertices():
            for b in self._dict[a]:
                if(hash(b) < hash(a)):
                    continue
                e = Edge(a, b)
                if (a, b) not in self._edges:
                    self._edges[(a, b)] = [e]
                    self._edges[(b, a)] = [e]
                else:
                    self._edges[(a, b)].append(e)
                    self._edges[(b, a)].append(e)

    def edges(self, erase_multiple=False):
        """
        Getter on the edges of the graph

        Parameters
        ----------
            'erase_multiple' : bool
            If set to True, will do not consider duplicate edges

        Returns
        -------
            An iterator over the edges of a the graph
        """
        if self._edges is None:
            self._generate_edges()
        result = [x for ((a, b), sublist) in self._edges.items()
                  for x in sublist if a <= b]
        if erase_multiple:
            return set(result)
        return result

    def _generate_adjacency(self):
        """
        Generates the adjacency matrix of the graph.
        This matrix is then stored into the self._matrix attribute
        """
        try:
            n = len(self._dict)  # number of vertices
            # assign a number between 0 and n to all vertices
            self._matrix = [[0 for j in range(n)] for i in range(n)]
            for u in self._dict:
                for v in self._dict[u]:
                    self._matrix[u.id][v.id] += 1
                    self._matrix[v.id][u.id] += 1
        except Exception as e:
            self._matrix = None
            raise e

    def adjacency_matrix(self):
        """
        Computes and return the adjacency matrix of the graph.

        Returns:
            A numpy array of shape (N*N) where N is the number of vertices
            in the graph
        """
        if self._matrix is None:
            self._generate_adjacency()
        return self._matrix

    def get_neighbours_edge(self, v):
        """
        Returns the edges of the graph that are incident to v

        Parameters
        ----------
            'v' : A Vertex object or an integer (vertex id)
                The vertex from which to extract the neighbourhood

        Returns:
            The list of edge neighbours of v
        """
        if not isinstance(v, Vertex):
            assert isinstance(v, int)
            v = Vertex(v)
        if self._edges is None:
            return [Edge(v, u) for u in self._dict[v]]
        else:
            output = []
            for e in self.edges():
                if e.start == v or e.end == v:
                    output.append(e)
            return output

    # ---------------  Modification of the data ------------------------
    def add_vertex(self, v) -> None:
        """
        Adds a new vertex to the graph

        Parameters
        ----------
            'v' : a Vertex object or a integer for a Vertex id
                If an integer is provided, the method will build a Vertex
                with the id field being v.
        """
        self._matrix = None  # reset adjacency matrix
        if not isinstance(v, Vertex):
            assert isinstance(v, int)
            v = Vertex(v)
        if v not in self._dict:
            self._dict[v] = []

    def remove_vertex(self, v) -> None:
        """
        Removes a vertex from the graph. If the given vertex is not present,
        this method does not do anything.

        Parameters
        ----------
            'v' : a Vertex object or a integer for a Vertex id
                If an integer is provided, the method will build a Vertex
                with the id field being v.
        """
        self._edges = None  # reset edges set
        self._matrix = None  # reset adjacency
        if not isinstance(v, Vertex):
            assert isinstance(v, int)
            v = Vertex(v)
        if v in self._dict:
            self._dict.pop(v, None)
        for x in self._dict:
            try:
                self._dict[x].remove(v)
            except ValueError:
                continue

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
            self._dict[e.start] = [e.end]
        else:
            self._dict[e.start].append(e.end)
        if e.start != e.end and e.end not in self._dict:
            self._dict[e.end] = [e.start]
        elif e.start != e.end:
            self._dict[e.end].append(e.start)
        if self._edges is not None:
            if (e.start, e.end) not in self._edges:
                self._edges[(e.start, e.end)] = [e]
                if e.start != e.end:
                    self._edges[(e.end, e.start)] = [e]
            else:
                self._edges[(e.start, e.end)].append(e)
                if e.start != e.end:
                    self._edges[(e.end, e.start)].append(e)

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
        try:
            self._dict[e.start].remove(e.end)
        except ValueError:
            pass
        try:
            self._dict[e.end].remove(e.start)
        except ValueError:
            pass
        if self._edges is not None:
            self._edges[(e.start, e.end)] = self._edges[(e.start, e.end)][1:]
            self._edges[(e.end, e.start)] = self._edges[(e.end, e.start)][1:]

    # ----- statistics -------

    def number_of_loops(self):
        """
        Computes the number of loops in the graph. A loop is an edge for which
        the starting point and the ending point are the same vertex

        Returns
        -------
            An integer equal to the number of loops in the graph
        """
        n = 0
        for e in self.edges():
            if e.start == e.end:
                n += 1
        return n

    def number_of_multiple_edges(self):
        """
        Computes the number of multiple edges in the graph, that is the
        number of edges we can delete from the graph without changing
        any connectivity relationships.

        Returns
        -------
            An integer equal to the number of multiple loops.
        """
        seen = {(a, b): False for a in self.vertices()
                for b in self.vertices()}
        n = 0
        for e in self.edges():
            v = [e.start, e.end]
            v.sort()
            if seen[(v[0], v[1])]:
                n += 1
            seen[(v[0], v[1])] = True
        return n
