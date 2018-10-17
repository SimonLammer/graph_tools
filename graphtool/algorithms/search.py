from ..graph import *


def no_pre_functor(node):
    """
    Simple functor doing nothing on the node
    """
    return None


def no_neighbour_functor(state, answer):
    """
    Simple functor doing nothing with the neighbours data
    """
    return None


def no_post_functor(state):
    """
    Simple functor doing nothing after the exploration of neighbours
    """
    return None


def tree_builder_functors():
    """
    Returns three functors allowing to generate a covering tree with a DFS
    rooted in the starting node

    Returns
    -------
    Three functors
    """
    def pre_functor(node):
        return node

    def neighbour_functor(state, answer):
        state.add_neighbour(answer)

    def post_functor(state):
        return state
    return pre_functor, neighbour_functor, post_functor


def count_nodes_functors():
    """
    Returns three functors allowing to count the number of nodes in the
    connected component of the starting node of a DFS

    Returns
    -------
    Three functors
    """
    def pre_functor(node):
        return 1

    def neighbour_functor(state, answer):
        return state + answer

    def post_functor(state):
        return state
    return pre_functor, neighbour_functor, post_functor


def depth_first_search(graph, init_node, functors):
    """
    Explores the graph. The functors argument contains three functors :
    pre_functor, neighbour_functor, post_functor. When exploring, when the
    explorer reaches a node, it calls pre_functor on the node. Then, calls
    recursively each neighbour. Each neighbour returns a value. Each value
    returned by a neighbour is given to neighbour_functor, updating the state
    of the node, initialized by the pre_functor call. Then, when all neighbours
    returned, the node returns the value of post_functor.
    This allows to do very adaptative operations during the exploration

    Parameters
    ----------
    'graph' : Graph
        the graph to explore
    'init_node' : Vertex
        the node where to start the exploration
    'functors' : {functor, functor, functor}
        pre_functor : called when reaching a node for the first time
        neighbour_functor : called on each neighbour return value
        post_functor : called when leaving the node

    Returns
    -------
    The return value of the initial node
    """
    pre_functor, neighbour_functor, post_functor = functors
    visited = set()

    def dfs(node):
        visited.add(node)
        state = pre_functor(node)
        for neighbour in graph.get_neighbours(node):
            if neighbour not in visited:
                answer = dfs(neighbour)
                state = neighbour_functor(state, answer)
        return post_functor(state)
    return dfs(init_node)


def topological_sort(graph):
    """
    On an oriented graph, does a topological exploration of the graph

    Parameters
    ----------
    'graph' : Graph
        the graph to explore

    Returns
    -------
    A list of the nodes, sorted by topological order
    """
    degrees = {vertex: 0 for vertex in graph.vertices()}
    for edge in graph.edges():
        degrees[edge.end] += 1
    stack = [vertex for (vertex, degree) in degrees.items() if degree == 0]
    total_order = []
    while not stack:
        vertex = stack.pop()
        for neighbour in graph.get_neighbours_out(vertex):
            degrees[neighbour] -= 1
            if degrees[neighbour] == 0:
                stack.append(neighbour)
        total_order.append(vertex)
    if len(graph) != len(total_order):
        print(len(graph), len(total_order))
        raise Exception("Topological sort error : cycles found graph")
    return total_order


def get_connected_components(graph):
    """
    Explores the graph and returns all connected components.

    Parameters
    ----------
    'graph' : Graph
        the graph to explore

    Returns
    -------
    A list components. Each component is the list of all vertices in the
    component
    """
    seen = set()
    components = []

    def pre_functor(node):
        component.append(node)
        seen.add(node)

    def explore_components(node):
        functors = (pre_functor, no_neighbour_functor, no_post_functor)
        return depth_first_search(graph, node, functors)

    for vertex in graph.vertices():
        if vertex not in seen:
            component = []
            explore_components(vertex)
            components.append(component)
    return [graph.subgraph(comp) for comp in components]


def breath_first_search():
    pass
