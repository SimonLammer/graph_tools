import graphtool.graph

def tree_builder():
    def pre_functor(node):
        return graph.Vertex(data = node)
    def neighbour_functor(state, answer):
        state.add_neighbour(answer)
    def post_functor(state):
        return state
    return pre_functor, neighbour_functor, post_functor

def depth_first_search(init_node, functors):
    pre_functor, neighbour_functor, post_functor = functors
    visited = set()
    def dfs(node):
        visited.add(node)
        state = pre_functor(node)
        for neighbour in node.neighbours():
            if neighbour not in visited:
                answer = dfs(neighbour)
                neighbour_functor(state, answer)
        return post_functor(state)
    return dfs(init_node)

def BreathFirstSearch(graph, init_node):
    pass
