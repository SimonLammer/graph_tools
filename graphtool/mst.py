# Minimum spanning tree algorithms


def MST(graph, algo='Kruskal'):
    if algo.lower() == 'prim':
        return Prim(graph)
    elif algo.lower() == "kruskal":
        return Kruskal(graph)
    else:
        raise Exception("algo should be 'Prim' or 'Kruskal'")


def Kruskal(graph):
    pass


def Prim(graph):
    pass
