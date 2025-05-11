import random
from src.main.graphs.graph_adjacency_list import GraphAdjacencyList
from src.main.graphs.graph_adjacency_matrix import GraphAdjacencyMatrix
from src.main.graphs.graph_edge_list import GraphEdgeList


def generate_random_graph(size, directed=False, density=0.5, max_weight=10):
    graphs = {
        "adjacency_list": GraphAdjacencyList(directed),
        "adjacency_matrix": GraphAdjacencyMatrix(size, directed),
        "edge_list": GraphEdgeList(directed)
    }

    vertex_degree = {v: 0 for v in range(size)}

    for i in range(size):
        for j in range(size):
            if i != j and random.random() < density:
                weight = random.randint(1, max_weight)
                for graph in graphs.values():
                    graph.add_edge(i, j, weight)
                vertex_degree[i] += 1
                vertex_degree[j] += 1 if not directed else 0

    for v in range(size):
        if vertex_degree[v] == 0:
            u = random.choice([u for u in range(size) if u != v])
            weight = random.randint(1, max_weight)
            for graph in graphs.values():
                graph.add_edge(v, u, weight)
            vertex_degree[v] += 1
            vertex_degree[u] += 1 if not directed else 0

    return graphs
