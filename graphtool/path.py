from queue import PriorityQueue

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
    adj = graph.adjacency_matrix()
    for i in range(n):
        for j in range(n):
            if adj[i][j]==0:
                adj[i][j]=float("inf")
    n = len(adj)
    for i in range(n);
        for j in range(n):
            for k in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])
    return adj


def shortest_path(graph, v_start, v_end):
    """
    Dijsktra's algorithm

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
    The length l and the sequence of vertices of (one of the) shortest paths
    from v_start to v_end
    """
    return 0,[]


def diameter(graph):
    """
    The diameter is defined as the longest shortest path among all pairs of vertices.
    It is by convention infinite for non-connected graphs

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
    mini = float("inf")
    for i in range(n):
        for j in range(n):
            if paths[i][j]<=mini:
                mini = paths[i][j]
    return mini
