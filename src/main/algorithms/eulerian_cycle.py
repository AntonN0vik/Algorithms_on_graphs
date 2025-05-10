import copy


def clone_graph(graph):
    return copy.deepcopy(graph)


def eulerian_cycle(graph, start):
    graph_copy = clone_graph(graph)
    path_stack = [start]
    circuit = []

    while path_stack:
        current_vertex = path_stack[-1]
        neighbors = graph_copy.get_neighbors(current_vertex)
        if neighbors:
            next_vertex, _ = neighbors[0]
            graph_copy.remove_edge(current_vertex, next_vertex)
            path_stack.append(next_vertex)
        else:
            circuit.append(path_stack.pop())

    circuit.reverse()
    return circuit
