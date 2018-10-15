from ..graph import *


def is_erdos_gallai(sequence):
    """
    Returns True if and only if the graph respects the Erdös-Gallai
    property.
    See https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gallai_theorem
    """
    assert len(sequence) > 0
    if sum(sequence) % 2 == 1:
        return False
    n = len(sequence)
    degree_sum = 0
    min_sum = [0]*n
    min_sum[n-1] = min(n, sequence[n-1])
    for k in range(n-2, -1, -1):
        min_sum[k] = min_sum[k+1]+min(sequence[k], k+1)
    for k in range(n-1):
        degree_sum += sequence[k]
        if degree_sum > k*(k+1) + min_sum[k+1]:
            return False
    degree_sum += sequence[n-1]
    return degree_sum <= n*(n-1)


def global_clustering_coeff(graph):
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
        for v2 in graph.get_neighbours(v1):
            for v3 in graph.get_neighbours(v1):
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
