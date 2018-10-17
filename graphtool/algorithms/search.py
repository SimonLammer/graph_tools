from ..graph import *


def no_pre_functor(node):
    """
    Empty functor that does nothing when visiting a node
    """
    return None


def no_neighbour_functor(state, answer):
    """
    Empty functor that does nothing with neighbour data
    """
    return None


def no_post_functor(state):
    """
    Empty functor that does nothing when leaving a node
    """
    return None


# def tree_builder_functors():
#     """
#     Set of functors building the DFS tree when called on a graph
#     """
#     def pre_functor(node):
#         return node

#     def neighbour_functor(state, answer):
#         state.add_neighbour(answer)

#     def post_functor(state):
#         return state
#     return pre_functor, neighbour_functor, post_functor


def count_nodes_functors():
    """
    Set of functors counting the number of nodes in the connected component of
    the starting node
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
    Generic Depth First Search algorithm, using functors to describe what to do
    at each node

    Parameters:
        'graph': Graph
            The graph to explore

        'init_node' : Vertex
            The starting node

        'functors' : set of 3 functors
            'pre_functor' : called on each node when first visiting it
            'neighbour_functor' : process the data returned by each neighbour
            'post_functor' : what the actual node will return

    Returns:
        The return value of the init node
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
    Topological Sort on the graph

    Returns:
        The list of the vertices ordered
    """
    degrees = graph.get_out_degrees()
    stack = list(graph.get_sinks())
    total_order = []
    while stack:
        vertex = stack.pop()
        for neighbour in graph.get_neighbours_in(vertex):
            degrees[neighbour] -= 1
            if degrees[neighbour] == 0:
                stack.append(neighbour)
        total_order.append(vertex)
    if len(graph) != len(total_order):
        raise Exception("Topological sort error : cycles found graph")
    return total_order


def get_connected_components(graph):
    """
    Get the connected components of the graph

    Returns:
        List of components. Each component is the list of the vertices in it
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
    """
    TODO
    """
    pass
