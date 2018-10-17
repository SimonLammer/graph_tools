# Minimum spanning tree algorithms

from ..graph import *
from heapq import *


def MST(graph, algo='Kruskal'):
    """
    Minimal Spanning Tree.

    Parameters
    ----------
    'graph' : Graph
        The graph to explore

    'algo' : "Kruskal" or "Prim"
        The algo to use to get the MST. Default to Kruskal

    Returns
    -------
        A minimal spanning tree of the graph
    """
    if algo.lower() == 'prim':
        return prim(graph)
    elif algo.lower() == "kruskal":
        return kruskal(graph)
    else:
        raise Exception("algo should be 'Prim' or 'Kruskal'")


def kruskal(graph):
    """
    Kruskal algorithm

    Returns
    -------
    The minimal spanning tree on the graph
    """
    father = {node: node for node in graph.vertices()}
    weight = {node: 0 for node in graph.vertices()}

    def get_father(node):
        if node != father[node]:
            father[node] = get_father(father[node])
        return father[node]

    def merge(f1, f2):
        if weight[f1] >= weight[f2]:
            father[f2] = f1
            if weight[f1] == weight[f2]:
                weight[f1] += 1
        else:
            merge(f2, f1)

    edges = list(graph.edges())
    edges.sort()
    mst = []
    for e in edges:
        fs = get_father(e.start)
        fe = get_father(e.end)
        if fs != fe:
            mst.append(e)
            merge(fs, fe)
    return mst


def prim(graph):
    """
    Prim algorithm

    Returns
    -------
    The minimal spanning tree on the graph
    """
    heap = [(0, 0, next(iter(graph.vertices())), None)]
    dist = dict()
    t = 0
    mst = []
    while len(heap) != 0:
        weight, _, node, edgemst = heappop(heap)
        if node in dist:
            continue
        dist[node] = weight
        if edgemst is not None:
            mst.append(edgemst)
        for edge in graph.get_neighbours_edge(node):
            neighbour = edge.other(node)
            if neighbour not in dist:
                t += 1
                realweight = edge["weight"]
                heappush(heap, (realweight, t, neighbour, edge))
    return mst
