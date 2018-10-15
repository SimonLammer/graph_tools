from heapq import *
from copy import copy
from ..graph.vertex_edge import Vertex, Edge
from ..graph.graph import Graph
from ..graph.orientedGraph import OrientedGraph
from .search import get_connected_components


def all_shortest_paths(graph):
    """
    Floyd-Warshall algorithm.

    Parameters
    ----------
        'graph' : a Graph object

    Returns
    -------
        A matrix M (list of list) where M[i][j] = the length of the
        shortest path from vertex i to vertex j
    """
    adj = copy(graph.adjacency_matrix())
    n = len(adj)
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 0 and i != j:
                adj[i][j] = float("inf")
    for i in range(n):
        for j in range(n):
            for k in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])
    return adj


def shortest_path(graph, v_start, v_end, heuristic):
    """
    A* algorithm

    Parameters
    ----------
        'graph' : a Graph object
            graph on which to perform the search

        'v_start' : a Vertex object
            Starting point of the algorithm

        'v_end' : a Vertex object
            Target point of the algorithm

        'heuristic' : a function (Vertex a, Vertex b) -> weight
            Evaluate the distance from a to b

    Returns
    -------
        The length l and the sequence of vertices of (one of the) shortest
        paths from v_start to v_end
    """
    heap = [(0, 0, v_start, None)]
    dist = dict([(x, float("inf")) for x in graph.vertices()])
    dist[v_start] = 0
    origin = dict([(x, None) for x in graph.vertices()])
    t = 0
    while not (len(heap) == 0) and v_end not in dist:
        weight, node, _, father = heappop(heap)
        if node in dist:
            continue
        dist[node] = weight
        origin[node] = father
        for neighbour in graph.get_neighbours(node):
            if dist[neighbour] == float("inf"):
                t += 1
                newweight = weight + heuristic(neighbour, v_end)
                heappush(heap, (newweight, t, neighbour, node))

    def recover(node):
        ans = []
        while origin[node] is not None:
            ans.append(node)
            node = origin[node]
        return ans
    return dist[v_end], recover(v_end)


def dijkstra(graph, v_start, v_end):
    """
    Dijkstra's algorithm

    Parameters
    ----------
        'graph' : a Graph object
            graph on which to perform the search

        'v_start' : a Vertex object
            Starting point of the algorithm

        'v_end' : a Vertex object
            Target point of the algorithm

    Returns
    -------
        The length l and the sequence of vertices of (one of the) shortest
        paths from v_start to v_end
    """
    def no_heuristic(a, b):
        return 0
    return shortest_path(graph, v_start, v_end, no_heuristic)


def diameter(graph):
    """
    The diameter is defined as the longest shortest path among all pairs
    of vertices. It is by convention infinite for non-connected graphs

    Parameters
    ----------
        'graph' : a Graph object
            The graph on which to perform the algorithm

    Returns
    -------
        The diameter of the graph.
    """
    paths = all_shortest_paths(graph)
    n = len(paths)
    maxi = -float("inf")
    for i in range(n):
        for j in range(n):
            if paths[i][j] >= maxi:
                maxi = paths[i][j]
    return maxi


def biggest_component_diameter(graph):
    """

    TODO

    Computes the diameter of the biggest component of the graph

    Parameters
    ----------
        'graph' : a Graph object
            The graph on which to perform the algorithm

    Returns
    -------
        The diameter of the biggest component of the graph
    """
    comp_list = get_connected_components(graph)
    n = 0
    biggest = -1
    for i in range(len(comp_list)):
        if len(comp_list[i]) > n:
            n = len(comp_list[i])
            biggest = i
    return 0  # diameter(comp_list[biggest])
