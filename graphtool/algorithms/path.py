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
            graph on which to perform the algorithm

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
    for k in range(n):
        for i in range(n):
            for j in range(n):
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
            Evaluate the remaining distance from a to b

    Returns
    -------
        The length l and the sequence of vertices of (one of the) shortest
        paths from v_start to v_end
    """
    heap = [(0, 0, 0, v_start, None)]
    dist = dict()
    origin = dict()
    t = 0
    while len(heap) != 0 and v_end not in dist:
        _, weight, _, node, father = heappop(heap)
        if node in dist:
            continue
        dist[node] = weight
        origin[node] = father
        for edge in graph.get_neighbours_edge(node):
            neighbour = edge.other(node)
            if neighbour not in dist:
                t += 1
                realweight = weight + edge["weight"]
                fakeweight = realweight + heuristic(neighbour, v_end)
                heappush(heap, (fakeweight, realweight, t, neighbour, node))

    def recover(node):
        ans = []
        while node is not None:
            ans.append(node)
            node = origin[node]
        return ans[::-1]
    if v_end not in dist:
        return float("inf"), []
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
    return diameter(Graph.renumber(comp_list[biggest]))
