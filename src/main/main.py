from src.main.graphs.graph_generator import generate_random_graph
from src.main.algorithms.dijkstra import dijkstra
from src.main.algorithms.astar import astar
from src.main.algorithms.eulerian_cycle import eulerian_cycle
from src.main.algorithms.shortest_path import get_shortest_path
from src.main.visualization.graph_visualization import create_video


def heuristic(a, b):
    return abs(a - b)


def run_algorithms_on_graphs(size, directed=False, density=0.27, max_weight=10, create_graph_video=False):

    graphs = generate_random_graph(size, directed, density, max_weight)

    start_vertex = 0
    end_vertex = size - 1

    for representation_type, graph in graphs.items():
        print(f"--- {representation_type.upper()} ---")
        print(graph)
        print()
        print("Алгоритм Дейкстры:")
        dijkstra_distances, dijkstra_previous = dijkstra(graph, start_vertex)
        print(f"Расстояния от вершины {start_vertex}: {dijkstra_distances}")
        dijkstra_path = get_shortest_path(dijkstra_previous, start_vertex, end_vertex)
        print(f"Кратчайший путь до вершины {end_vertex}: {dijkstra_path}")
        print()
        print("Алгоритм A*:")
        astar_distances, astar_previous = astar(graph, start_vertex, end_vertex, heuristic)
        print(f"Расстояния от вершины {start_vertex}: {astar_distances}")
        astar_path = get_shortest_path(astar_previous, start_vertex, end_vertex)
        print(f"Кратчайший путь до вершины {end_vertex}: {astar_path}")

    if create_graph_video:
        print(f"\nСоздаём видео для {representation_type.upper()}...\n")
        create_video(graphs["adjacency_list"], representation_type, start_vertex, end_vertex)

if __name__ == "__main__":
    run_algorithms_on_graphs(size=9, directed=True, density=0.3, max_weight=5,
                             create_graph_video=True)

