from src.main.graphs.graph import Graph


class GraphAdjacencyList(Graph):
    def __init__(self, directed=False):
        self._directed = directed
        self._adjacency_list = {}

    def get_vertices_count(self) -> int:
        return len(self._adjacency_list)

    def get_edges_count(self) -> int:
        edge_count = 0
        for edges_list in self._adjacency_list.values():
            edge_count += len(edges_list)
        return edge_count if self._directed else edge_count // 2

    def get_vertices_list(self) -> list[str]:
        return list(self._adjacency_list.keys())

    def get_edges_list(self) -> list[tuple[str, str]]:
        edges = []
        for v, neighbors in self._adjacency_list.items():
            for u, weight in neighbors:
                if self._directed or (u, v) not in edges:
                    edges.append((v, u))
        return edges

    def add_edge(self, v: int, u: int, weight=1):
        if v not in self._adjacency_list:
            self._adjacency_list[v] = []
        if u not in self._adjacency_list:
            self._adjacency_list[u] = []
        self._adjacency_list[v].append((u, weight))
        if not self._directed:
            self._adjacency_list[u].append((v, weight))

    def remove_edge(self, v: int, u: int):
        if v in self._adjacency_list:
            self._adjacency_list[v] = [edge for edge in self._adjacency_list[v] if edge[0] != u]
        if not self._directed and u in self._adjacency_list:
            self._adjacency_list[u] = [edge for edge in self._adjacency_list[u] if edge[0] != v]

    def has_edge(self, v: int, u: int) -> bool:
        if v not in self._adjacency_list:
            return False
        for edge in self._adjacency_list[v]:
            if edge[0] == u:
                return True
        return False

    def get_edge_weight(self, v: int, u: int) -> int:
        if v not in self._adjacency_list:
            return 0
        for edge in self._adjacency_list[v]:
            if edge[0] == u:
                return edge[1]
        return 0

    def get_neighbors(self, v: int) -> list:
        return self._adjacency_list.get(v, [])

    def __str__(self):
        result = ""
        for v in self._adjacency_list:
            result += f"{v}: {self._adjacency_list[v]}\n"
        return result
