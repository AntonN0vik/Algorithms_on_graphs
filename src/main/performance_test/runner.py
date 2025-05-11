import csv

from src.main.algorithms.dijkstra import dijkstra
from src.main.algorithms.astar import astar
from src.main.performance_test.runtime_benchmark import runtime_benchmark
from src.main.performance_test.memory_benchmark import memory_benchmark
from src.main.graphs.graph_generator import generate_random_graph


def heuristic(u, v):
    return 0


def heuristic_simple(u, v):
    return abs(u - v)


def heuristic_squared(u, v):
    return (u - v) ** 2


def run_dijkstra(graph, start, end):
    return dijkstra(graph, start)


def run_astar(graph, start, end):
    return astar(graph, start, end, heuristic)


def run_astar_simple(graph, start, end):
    return astar(graph, start, end, heuristic_simple)


def run_astar_squared(graph, start, end):
    return astar(graph, start, end, heuristic_squared)


algorithms = {
    "dijkstra": run_dijkstra,
    "astar": run_astar,
    "astar_simple": run_astar_simple,
    "astar_squared": run_astar_squared
}

graph_types = ['adjacency_list', 'adjacency_matrix', 'edge_list']


def run_benchmark():
    with open('benchmark_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Graph Type", "Algorithm", "Size", "Avg Time (s)", "Std Dev",
            "Peak Memory (KB)"
        ])

        for size in [10, 50, 100, 200, 500]:
            graphs = generate_random_graph(size, directed=False, density=0.2)

            start, end = 0, size - 1

            for g_type in graph_types:
                graph = graphs[g_type]

                for alg_name, alg_func in algorithms.items():
                    avg_time, std_dev = runtime_benchmark(
                        lambda: alg_func(graph, start, end))
                    peak_memory = memory_benchmark(
                        lambda: alg_func(graph, start, end))

                    writer.writerow([
                        g_type, alg_name, size, f"{avg_time:.6f}",
                        f"{std_dev:.6f}", f"{peak_memory:.2f}"
                    ])


if __name__ == "__main__":
    run_benchmark()
