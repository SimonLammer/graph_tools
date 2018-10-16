from ..graph import *


def no_pre_functor(node):
    return None


def no_neighbour_functor(state, answer):
    return None


def no_post_functor(state):
    return None


def tree_builder_functors():
    def pre_functor(node):
        return node

    def neighbour_functor(state, answer):
        state.add_neighbour(answer)

    def post_functor(state):
        return state
    return pre_functor, neighbour_functor, post_functor


def count_nodes_functors():
    def pre_functor(node):
        return 1

    def neighbour_functor(state, answer):
        return state + answer

    def post_functor(state):
        return state
    return pre_functor, neighbour_functor, post_functor


def depth_first_search(graph, init_node, functors):
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
    degrees = {vertex: 0 for vertex in graph.vertices()}
    for edge in graph.edges():
        degrees[edge.end] += 1
    stack = [vertex for (vertex, degree) in degrees.items() if degree == 0]
    total_order = []
    while not stack:
        vertex = stack.pop()
        for neighbour in grah.get_neighbours(vertex):
            degrees[neighbour] -= 1
            if degrees[neighbour] == 0:
                stack.append(neighbour)
        total_order.append(vertex)
    if len(graph.vertices()) != len(total_order):
        raise Exception("Cycles found in the graph")
    return total_order


def get_connected_components(graph):
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
    return components


def breath_first_search():
    pass
