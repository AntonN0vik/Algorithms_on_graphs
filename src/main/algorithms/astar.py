import heapq
from src.main.graphs.graph import Graph


def astar(graph: Graph, start: int, end: int, heuristic):
    vertices_count = graph.get_vertices_count()

    distances = [float('inf')] * vertices_count
    distances[start] = 0

    previous = [None] * vertices_count

    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start, end), start))

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex == end:
            break

        if current_distance != distances[current_vertex] + heuristic(
                current_vertex, end):
            continue

        for neighbor, weight in graph.get_neighbors(current_vertex):
            tentative_distance = distances[current_vertex] + weight
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (
                tentative_distance + heuristic(neighbor, end), neighbor))

    return distances, previous
