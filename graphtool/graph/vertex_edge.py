class Vertex:
    """
    'id' : integer

    'data' : dict

    A vertex is designed as an integer on which we build additionnal data
    """

    def __init__(self, id: int, data: dict = None):
        self.id = id
        if data is None:
            self.data = dict({"name": str(self.id)})
        else:
            self.data = data
            if "name" not in self.data:
                self.data["name"] = str(self.id)
            self.id = self.data.get("id", self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return self.data["name"]

    def __repr__(self):
        return "V("+str(self.id)+")"

    def __getitem__(self, attr):
        return self.data[attr]

    def __hash__(self):
        return hash(self.id)


class Edge:
    def __init__(self, *args, **kwargs):
        """
        Different ways to initialize an Edge:
        - Edge(edge)
        - Edge(iterable of length 2) containing either two Vertex objects or
            two names of vertices
        - Edge(a,b) where a and b are either Vertex objects or vertices' names
        """
        self.data = kwargs.get("data", dict())
        self.oriented = kwargs.get("oriented", False)
        if len(args) == 1 and isinstance(args[0], Edge):
            self.start = args[0].start
            self.end = args[0].end
            self.data = args[0].data
            self.oriented = args[0].oriented
        else:
            a, b = None, None
            if len(args) == 0:
                # start and end are either specified as own kwargs or as
                # a key in data dict
                a, b = kwargs.get("start", None), kwargs.get("end", None)
                if a is None:
                    a = self.data.get("start", None)
                if b is None:
                    b = self.data.get("end", None)
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
            self.data["start"] = a
            self.data["end"] = b
            if "weight" not in self.data:
                self.data["weight"] = 1

    def __eq__(self, other):
        if self.oriented:
            return self.start == other.start and self.end == other.end
        return {self.start, self.end} == {other.start, other.end}

    def __lt__(self, other):
        if "weight" in self.data and "weight" in other.data:
            return self.data["weight"] < other.data["weight"]
        return True

    def __gt(self, other):
        if "weight" in self.data and "weight" in other.data:
            return self.data["weight"] > other.data["weight"]
        return True

    def __getitem__(self, attr):
        return self.data[attr]

    def __repr__(self):
        return "Edge("+str(self.start)+", "+str(self.end)+")"

    def __hash__(self):
        return hash((self.start, self.end, self.oriented))

    def other(self, v):
        if self.start == v:
            return self.end
        elif self.end == v:
            return self.start
        raise Exception("Error in Edge.other method : \n\
            Vertex {} is not incident to edge {}".format(v, self))
