from src.main.graphs.graph import Graph


class GraphAdjacencyMatrix(Graph):
    def __init__(self, size, directed=False):
        self._directed = directed
        self._size = size
        self._adj_matrix = [[0] * size for _ in range(size)]

    def get_vertices_count(self) -> int:
        return self._size

    def get_edges_count(self) -> int:
        return self._size

    def add_edge(self, v: int, u: int, weight=1):
        self._adj_matrix[v][u] = weight
        if not self._directed:
            self._adj_matrix[u][v] = weight

    def remove_edge(self, v: int, u: int):
        self._adj_matrix[v][u] = 0
        if not self._directed:
            self._adj_matrix[u][v] = 0

    def has_edge(self, v: int, u: int) -> bool:
        return self._adj_matrix[v][u] != 0

    def get_edge_weight(self, v: int, u: int) -> int:
        return self._adj_matrix[v][u]

    def get_neighbors(self, v: int) -> list:
        result = []
        for u in range(self._size):
            if self._adj_matrix[v][u]:
                result.append((u, self._adj_matrix[v][u]))

        return result

    def __str__(self):
        result = ""
        for v in range(self._size):
            for u in range(self._size):
                result += str(self._adj_matrix[v][u]) + ' '
            result += '\n'
        return result
