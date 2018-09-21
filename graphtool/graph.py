
class Vertex:
    def __init__(self, data=None, neighbours=None):
        self.data = data
        if neighbours is None:
            self.neighbours = []
        return self

    def add_neighbours(self, neighbour):
        self.neighbours.append(neighbour)


class Edge:
    pass


class Graph:
    def __init__(self):
        pass
