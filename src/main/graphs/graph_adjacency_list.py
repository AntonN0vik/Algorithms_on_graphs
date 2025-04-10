from src.main.graphs.graph import Graph


class GraphAdjacencyList(Graph):
    def __init__(self, directed=False):
        self._directed = directed
        self._adj_list = {}

    def get_vertices_count(self) -> int:
        return len(self._adj_list)

    def get_edges_count(self) -> int:
        count = 0
        for edges in self._adj_list.values():
            count += len(edges)

        if self._directed:
            return count
        else:
            return count // 2

    def add_edge(self, v: int, u: int, weight=1):
        if v not in self._adj_list:
            self._adj_list[v] = []
        if u not in self._adj_list:
            self._adj_list[u] = []
        self._adj_list[v].append((u, weight))

        if not self._directed:
            self._adj_list[u].append((v, weight))

    def remove_edge(self, v: int, u: int):
        if v in self._adj_list:
            self._adj_list[v] = [edge for edge in self._adj_list[v] if edge[0] != u]
        if not self._directed and u in self._adj_list:
            self._adj_list[u] = [edge for edge in self._adj_list[u] if edge[0] != v]

    def has_edge(self, v: int, u: int) -> bool:
        if v not in self._adj_list:
            return False

        for edge in self._adj_list[v]:
            if edge[0] == u:
                return True

        return False

    def get_edge_weight(self, v: int, u: int) -> int:
        if v not in self._adj_list:
            return 0

        for edge in self._adj_list[v]:
            if edge[0] == u:
                return edge[1]

        return 0

    def get_neighbors(self, v: int) -> list:
        return self._adj_list.get(v, [])

    def __str__(self):
        result = ""
        for v in self._adj_list:
            result += f"{v}: {self._adj_list[v]}\n"
        return result
