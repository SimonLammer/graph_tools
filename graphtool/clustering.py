import graphtool.graph


def is_erdos_gallai(sequence):
    """
    Returns True if and only if the graph respects the Erdös-Gallai
    property.
    See https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gallai_theorem
    """
    degree_sum = sum(sequence)
    n = len(sequence)
    for k in range(1, n+1):
        comp = sum([min(k, sequence[i]) for i in range(k+1, n+1)])
        if degree_sum > k*(k-1) + comp:
            return False
    return True


def clustering_coeff(graph):
    """
    Returns the clustering coefficient of a given graph.
    The clustering coefficient is defined by
        3*{number of triangles}/{number of connected triplets}
    """
    v = graph.vertices()
    e = graph.edges()
    triangles = 0
    connected_triplets = 0
    for v1 in v:
        for v2 in v:
            for v3 in v:
                a = Edge(v1, v2)
                b = Edge(v2, v3)
                c = Edge(v1, v3)
                intersect = e.intersection({a, b, c})
                if len(intersect) >= 2:
                    connected_triplets += 1
                if len(intersect) == 3:
                    triangles += 1
    if connected_triplets == 0:
        return 0
    return 3*triangles/connected_triplets


def local_clustering_coeff(graph, v):
    if not isinstance(v, Vertex):
        v = Vertex(v)
    neigh = graph.get_neighbours(v)
    k = len(neigh)  # degree of v
    if k < 2:
        return 0
    e = 0
    for edge in graph.edges():
        if edge.start in neigh and edge.end in neigh:
            e += 1
    return (2*e)/(k*(k-1))


def average_local_clustering_coeff(graph):
    c = 0
    n = 0
    for v in graph.vertices():
        c += local_clustering_coeff(graph, v)
        n += 1
    return c/n


def get_core_k(graph, k):
    """
    TODO
    """
    return Graph({})


def get_core_all(graph):
    """
    TODO
    """
    return []
