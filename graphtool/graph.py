
class Vertex:
    def __init__(self, name=None, data=None):
        self.name = name
        self.data = data

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "V("+str(self.name)+")"

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
        self.data = kwargs.get("data",None)
        self.oriented = kwargs.get("oriented",False)
        print(args)
        if len(args)==1 and isinstance(args[0],Edge):
            self.start = args[0].start
            self.end = args[0].end
            self.data = args[0].data
            self.oriented = args[0].oriented
        else:
            a,b = None,None
            if len(args)==1:
                a,b = args[0][0], args[0][1]
            elif len(args)==2:
                a,b = args[0],args[1]
            else:
                raise Exception("Too many arguments : only 2 were expected")
            if not isinstance(a,Vertex):
                a = Vertex(a)
            if not isinstance(b,Vertex):
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

    def __init__(self, _graph_dict):
        """
        Initialization function. Is not meant to be called as it is.
        """
        self._dict = _graph_dict
        self._edges = None

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
        if isinstance(d, str):
            # Load from a file
            pass
        return Graph(d)

    @staticmethod
    def from_adjacency_matrix(m):
        if isinstance(m, str):
            # Load from a file
            pass
        return Graph({})

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
        return Graph({})

    @staticmethod
    def clique(n):
        return Graph({})

    @staticmethod
    def erdos_renyi(n, p):
        """
        TODO
        """
        return Graph({})

    # ---------------- Getters and setters -----------------------------
    def vertices(self):
        """
        Returns an iterator over the vertices of the graph
        """
        return self._dict.keys()

    def _generate_edges(self):
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

    # ---------------  Modification of the data ------------------------
    def add_vertex(self, v):
        """
        v := Vertex | name
        """
        if not isinstance(v, Vertex):
            v = Vertex(v)

        if v not in self._dict:
            self._dict[v] = set()

    def remove_vertex(self, v):
        """
        v := Vertex | name
        """
        if not isinstance(v, Vertex):
            v = Vertex(v)

        if v in self._dict:
            del self._dict[v]
        for x in self._dict:
            self._dict[x].remove(v)

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

    def remove_edge(self, *args):
        """
        args = Edge | (Vertex, Vertex) | (name, name)
        """
        e = Edge(args)
        self._dict[e.start].remove(e.end)
        self._dict[e.end].remove(e.start)

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

    def is_erdos_gallai(self):
        """
        Returns True if and only if the graph respects the Erdös-Gallai
        property.
        See https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gallai_theorem
        """
        return False


class OrientedGraph:
    """
    TODO
    """
    pass
