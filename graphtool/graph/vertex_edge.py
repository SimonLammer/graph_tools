class Vertex:
    """
    Documentation TODO
    """
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
