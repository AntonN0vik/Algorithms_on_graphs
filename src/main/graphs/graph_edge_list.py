from src.main.graphs.graph import Graph


class GraphEdgeList(Graph):
    def __init__(self, directed=False):
        self._directed = directed
        self._edge_list = []

    def get_vertices_count(self) -> int:
        vertices = set()
        for edge in self._edge_list:
            vertices.add(edge[0])
            vertices.add(edge[1])
        return len(vertices)

    def get_edges_count(self) -> int:
        return len(self._edge_list)

    def get_vertices_list(self) -> list[int]:
        vertices = set()
        for edge in self._edge_list:
            vertices.add(edge[0])
            vertices.add(edge[1])
        return list(vertices)

    def get_edges_list(self) -> list[tuple[int, int, int]]:
        return self._edge_list

    def add_edge(self, v: int, u: int, weight=1):
        self._edge_list.append((v, u, weight))

        if not self._directed:
            self._edge_list.append((u, v, weight))

    def remove_edge(self, v: int, u: int):
        self._edge_list = [edge for edge in self._edge_list if
                           not (edge[0] == v and edge[1] == u)]
        if not self._directed:
            self._edge_list = [edge for edge in self._edge_list if
                               not (edge[0] == u and edge[1] == v)]

    def has_edge(self, v: int, u: int) -> bool:
        for edge in self._edge_list:
            if edge[0] == v and edge[1] == u:
                return True
        return False

    def get_edge_weight(self, v: int, u: int) -> int:
        for edge in self._edge_list:
            if edge[0] == v and edge[1] == u:
                return edge[2]
        return 0

    def get_neighbors(self, v: int) -> list:
        neighbors = []
        for edge in self._edge_list:
            if edge[0] == v:
                neighbors.append((edge[1], edge[2]))
        return neighbors

    def __str__(self):
        result = ""
        for edge in self._edge_list:
            result += f"({edge[0]}, {edge[1]}, weight={edge[2]})\n"
        return result
