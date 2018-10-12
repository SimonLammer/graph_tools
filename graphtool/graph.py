from random import random, randint, uniform


class Vertex:
    def __init__(self, name=None, data=None):
        self.name = name
        self.data = data

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return "V("+str(self.name)+")"

    def __hash__(self):
        return hash(self.name)


class Edge:
    def __init__(self, *args, **kwargs):
        """
        Different ways to initialize an Edge:
        - Edge(edge)
        - Edge(iterable of length 2) containing either two Vertex objects or
            two names of vertices
        - Edge(a,b) where a and b are either Vertex objects or vertices' names
        """
        self.data = kwargs.get("data", None)
        self.oriented = kwargs.get("oriented", False)
        self.weight = kwargs.get("weight", 1)
        if len(args) == 1 and isinstance(args[0], Edge):
            self.start = args[0].start
            self.end = args[0].end
            self.data = args[0].data
            self.oriented = args[0].oriented
        else:
            a, b = None, None
            if len(args) == 0:
                a, b = kwargs.get("start", None), kwargs.get("end", None)
                if a is None or b is None:
                    raise Exception("Invalid argument")
            elif len(args) == 1:
                a, b = args[0][0], args[0][1]
            elif len(args) == 2:
                a, b = args[0], args[1]
            else:
                raise Exception("Too many arguments : only 2 were expected")
            if not isinstance(a, Vertex):
                a = Vertex(a)
            if not isinstance(b, Vertex):
                b = Vertex(b)
            self.start = a
            self.end = b

    def __eq__(self, other):
        if self.oriented:
            return self.stat == other.start and self.end == other.end
        return {self.start, self.end} == {other.start, other.end}

    def __repr__(self):
        return "Edge("+str(self.start)+", "+str(self.end)+")"

    def __hash__(self):
        return hash((self.start, self.end, self.oriented))


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
    def from_edge_list(l):
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
    def from_adjacency_dict(d):
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
    def from_adjacency_matrix(m):
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
    def empty(n):
        """
        Returns the graph of n vertices without edges
        """
        graph_dict = dict()
        for i in range(n):
            graph_dict[Vertex(str(i))] = set()
        return Graph(graph_dict)

    @staticmethod
    def cycle(n):
        """
        Builds the cycle of size n, with vertex i being linked to
        vertices (i+1)%n and (i-1)%n
        """
        g = Graph.empty(n)
        for i in range(n-1):
            g.add_edge(str(i), str(i+1))
        g.add_edge(str(n-1), "0")
        return g

    @staticmethod
    def clique(n):
        """
        Builds the fully connected graph of size n
        """
        g = Graph.empty(n)
        for i in range(n):
            for j in range(i):
                g.add_edge(str(i), str(j))
        return g

    @staticmethod
    def erdos_renyi_proba(n, p):
        """
        Generates a graph through the Erdös-Renyi model.
        n = number of vertices
        Each edge of the graph is present with probability p
        """
        p = min(max(p, 0), 1)
        g = Graph.empty(n)
        for i in range(n):
            for j in range(i):
                if random() <= p:
                    g.add_edge(str(i), str(j))
        return g

    @staticmethod
    def erdos_renyi_edge(n, l):
        """
        Generates a graph through the Erdös-Renyi model.
        n = number of vertices
        l = number of edges
        """
        adj = [[0 for i in range(n)] for j in range(n)]
        possible_edges = [(i, j) for j in range(n) for i in range(j)]
        for i in range(l):
            (a, b) = possible_edges.pop(randint(0, len(possible_edges) - 1))
            adj[a][b] = 1
        return Graph.from_adjacency_matrix(adj)
    # ------------- Exportation methods -----------------

    def export_as_edge_list(self, filename: str):
        with open(filename, 'w') as f:
            for e in self.edges():
                f.write(str(e.start)+" "+str(e.end)+"\n")

    def export_as_adjacency_dict(self, filename: str):
        with open(filename, 'w') as f:
            for v in self._dict:
                f.write(str(v)+" ")
                for neigh in self._dict[v]:
                    f.write(str(neigh)+" ")
                f.write("\n")

    def export_as_adjacency_matrix(self, filename: str):
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
        Returns an iterator over the vertices of the graph
        """
        return self._dict.keys()

    def _generate_edges(self):
        """
        Generated the set of edges of the graph.
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
        Returns an iterator over the edges of a the graph
        """
        if self._edges is None:
            self._generate_edges()
        return self._edges

    def _generate_adjacency(self):
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
        if self._matrix is None:
            self._generate_adjacency()
        return self._matrix

    def get_neighbours(self, v):
        if not isinstance(v, Vertex):
            v = Vertex(v)
        return self._dict[v]

    # ---------------  Modification of the data ------------------------
    def add_vertex(self, v):
        """
        v := Vertex | name
        """
        self._matrix = None  # reset matrix
        if not isinstance(v, Vertex):
            v = Vertex(v)
        if v not in self._dict:
            self._dict[v] = set()

    def remove_vertex(self, v):
        """
        v := Vertex | name
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
        args = Edge | (Vertex, Vertex) | (name, name)
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
        args = Edge | (Vertex, Vertex) | (name, name)
        """
        e = Edge(args)
        self._dict[e.start].discard(e.end)
        self._dict[e.end].discard(e.start)
        if self._edges is not None:
            self._edges.discard(e)

    # ---------------- Stats computations -----------------------------
    def vertex_degree(self):
        return [len(self._dict[v]) for v in self.vertices()]

    def degree_sequence(self):
        degree_list = self.vertex_degree()
        degree_list.sort(reverse=True)
        return degree_list

    def find_isolated_vertices(self):
        return [v.name for v in self.vertices() if len(self._dict[v]) == 0]

    def density(self):
        e_nb = len(self.edges())
        v_nb = len(self.vertices())
        possible_edges = v_nb*(v_nb-1)/2
        return e_nb / possible_edges


class OrientedGraph:
    """
    TODO
    """

    def __init__(self):
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
