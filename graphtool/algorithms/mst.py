# Minimum spanning tree algorithms

from ..graph import *


def MST(graph, algo='Kruskal'):
    if algo.lower() == 'prim':
        return prim(graph)
    elif algo.lower() == "kruskal":
        return kruskal(graph)
    else:
        raise Exception("algo should be 'Prim' or 'Kruskal'")


def kruskal(graph):
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


def Prim(graph):
    heap = [(0, 0, graph.vertices[0], None)]
    dist = dict()
    origin = dict()
    t = 0
    mst = []
    while len(heap) != 0:
        weight, _, node, edgemst = heappop(heap)
        if node in dist:
            continue
        dist[node] = weight
        origin[node] = edge.other(node)
        if edge is not None:
            mst.append(edge)
        for edge in graph.get_neighbours_edge(node):
            neighbour = edge.other(node)
            if neighbour not in dist:
                t += 1
                realweight = edge["weight"]
                heappush(heap, (realweight, t, neighbour, edge))
    return mst
