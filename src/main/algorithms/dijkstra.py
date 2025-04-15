import heapq
from src.main.graphs.graph import Graph


def dijkstra(graph: Graph, start: int):
    vertices_count = graph.get_vertices_count()

    distances = [float('inf')] * vertices_count
    distances[start] = 0

    previous = [None] * vertices_count

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous
