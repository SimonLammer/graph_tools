
class Vertex:
    def __init__(self, data=None, neighbours=None):
        self.data = data
        if neighbours is None:
            self.neighbours = []
        else:
            self.neighbours = neighbours
        return self

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)


class Edge:
    def __init__(self, start=None, end=None, data=None):
        self.data = data
        self.start = start
        self.end = end
        return self


class Graph:
    def __init__(self):
        pass
