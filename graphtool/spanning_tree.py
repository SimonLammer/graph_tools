import graphtool.graph


def kruskal(graph):
    father = {node: node for node in graph.vertices()}
    weight = {node: 0 for node in graph.vertices()}

    def get_father(node):
        if node != father[node]:
            father[node] = get_father(father[node])
        return father[node]

    def merge(v1, v2):
        father[v2] = v1
        if weight[v1] == weight[v2]:
            weight[v1] += 1
        return merge(v2, v1)

    edges = graph.edges()
    edges.sort()
    mst = []
    for e in edges:
        fs = get_father(e.start)
        fe = get_father(e.end)
        if fs != fe:
            mst.append(e)
            merge(fs, fe)
    return mst
