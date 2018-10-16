Vertices, Edges and Graphs
==========================

The Graph class and the OrientedGraph classes are the main classes of this library.
Graph and OrientedGraph are relations between vertices.

The Vertex class
----------------
The Vertex class is build around an integer, called the vertex id. It can contain
every data you can imagine, implemented as a python dictionnary ::

    from graphtool.graph import Vertex
    u = Vertex(0) # 0 is the id of the vertex
    v = Vertex(1, data={"name" : "toto",
                        "weight" : 42,
                        "is_colored" : True,
                        "color" : "red" })

The Edge class
--------------
An Edge is a link between two Vertex objects.

    from graphtool.graph import Vertex,Edge
    e1 = Edge(0,1) # between Vertex(0) and Vertex(1), created on the go

    e2 = Edge(3,4, data={"weight" : 0.45, "label" : "friend"})

    u = Vertex(42, data={"name" : "foo"})
    v = Vertex(77, data={"name" : "bar"})
    e3 = Edge(u,v) # When Vertex objects are already created

    e4 = Edge(e1) # copy constructor


The Graph class
---------------

Graphs are stored as an adjacency dictionnary over their

**Initialize a Graph**

A graph can be initialized from a file through the three classical ways:
- With an edge list ::
    l = [Edge(0,1), Edge(1,2), Edge(2,0)]
    g = Graph.from_edge_list(l)
    # or alternatively, from a file:
    g = Graph.from_edge_list("file.txt")
- With an adjacency list ::
   d = {Vertex(0) : set([Vertex(1), Vertex(2)])}
   g = Graph.from_adjacency_dict(d)
   # or alternatively, from a file:
   g = Graph.from_adjacency_dict("file.txt")
- With an adjacency matrix ::
   m = [[0,1,1],[1,0,1],[1,1,0]]
   g = Graph.from_adjacency_matrix(m)
   # or alternatively, from a file:
   g = Graph.from_adjacency_matrix("file.txt")

**Getters and Setters**

`my_graph.vertices()` returns the set of vertices of the graph
`my_graph.edges()` returns the set of edges of the graph

**Manipulation on Graphs**
Graph and OrientedGraph implement various methods to modify their data:
`add_edge`, `remove_edge`, `add_vertex`, `remove_edge`

The OrientedGraph class
-----------------------
The OrientedGraph class is almost similar to the Graph class in terms of API, but
considers each of its Edge objects as oriented (that is, e.start and e.end are no longer symetrical)

A graph can be initialized from a file through the three classical ways:
- With an edge list ::
    l = [Edge(0,1), Edge(1,2, oriented=True), Edge(2,0, oriented=True)]
    g = OrientedGraph.from_edge_list(l)
    # or alternatively, from a file:
    g = OrientedGraph.from_edge_list("file.txt")

For initializing a Graph with an Edge list, one has to specify if the Edge is oriented or not. Since Edge objects are not oriented by default, seing `Edge(0,1)` instead of
`Edge(0,1, oriented=True)` in the list will result in the insertion of both Edge(0,1) and Edge(1,0) edges in the graph

- With an adjacency list ::
   d = {Vertex(0) : set([Vertex(1), Vertex(2)])}
   g = OrientedGraph.from_adjacency_dict(d)
   # or alternatively, from a file:
   g = OrientedGraph.from_adjacency_dict("file.txt")
- With an adjacency matrix ::
   m = [[0,1,1],[0,0,1],[1,0,0]]
   g = OrientedGraph.from_adjacency_matrix(m)
   # or alternatively, from a file:
   g = OrientedGraph.from_adjacency_matrix("file.txt")

A note on graph generators
--------------------------

The GraphGenerator class implements some static methods to proceduraly generate
some graphs ::

    from graphtool.graph.generator import *

    g1 = GraphGenerator.empty(10) # an empty graph
    g2 = GraphGenerator.clique(10) # a full graph
    g3 = GraphGenerator.cycle(10, oriented=True) # an oriented cycle
    g4 = GraphGenerator.erdos_renyi_proba(100,0.1)
    g4 = GraphGenerator.chung_lu([1,1,2,2,3])
    g5 = GraphGenerator.molloy_reed([1,1,2,2,3])
