Graph algorithms in Graphtool
=============================

Shortest Path Computation
-------------------------

Several different algorithms are implemented for computing the shortest path in graphs.

**Floyd-Warshall algorithm** ::

    all_shortest_paths(graph)


**A* algorithm**

The A* (A star) algorithm is an approximate algorithm for computing the shortest path between two nodes in a graph. It is a variant
of the Dijkstra algorithm that uses a heuristic function to compute the remaining distance to the goal node ::

    def my_heuristic(a,b):
        return 42

    shortest_path(graph, v_start, v_end, my_heuristic)

Dijkstra's algorithm is also implemented by default (null heuristic) ::

    dijkstra(graph, v_start, v_end)


Connected Components
--------------------

`get_connected_components` in the graphtool.algorithms.search module returns the list of connected components as subgraphs, each component being a new Graph object extracted from the original graph


Clustering Coefficients
-----------------------

Various Coefficients can be computed thanks to the graphtool.algorithms.clustering module.

**Global clustering coefficient** : it is defined as 3*{number of triangle}/{number of connected triplets}, and is computed by the `global_clustering_coeff` function

**Local clustering coefficient** : for a vertex v, it is defined as 2*{number of edges between neighbours of v}/{degree v}{degree v - 1}. It can be computed using the `local_clustering_coeff` function

**Averaged local clustering coeff**: the average over all vertices v of `local_clustering_coeff(v)`

Minimal Spanning Trees
----------------------

Two algorithms have been implemented for computing the minimal spanning tree of a graph : Kruskal's algorithm and Prim's algorithm. The `MST` function provides a unified interface for those two algorithms. It returns a list of Edge objects present in the MST ::

    l = MST(graph, algo="Kruskal") # Kruskal is default value for 'algo'
    l2 = MST(graph, algo="Prim")

The argument `algo` does not take capital letters into account, so that "Kruskal", "kruskal" and "KrUsKaL" will be recognized.
