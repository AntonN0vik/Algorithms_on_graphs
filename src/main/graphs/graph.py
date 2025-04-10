from abc import ABC, abstractmethod


class Graph(ABC):
    @abstractmethod
    def get_vertices_count(self) -> int:
        raise NotImplementedError("Не реализован в подклассе")

    @abstractmethod
    def get_edges_count(self) -> int:
        raise NotImplementedError("Не реализован в подклассе")

    @abstractmethod
    def add_edge(self, v: int, u: int, weight=1):
        raise NotImplementedError("Не реализован в подклассе")

    @abstractmethod
    def remove_edge(self, v: int, u: int):
        raise NotImplementedError("Не реализован в подклассе")

    @abstractmethod
    def has_edge(self, v: int, u: int) -> bool:
        raise NotImplementedError("Не реализован в подклассе")

    @abstractmethod
    def get_edge_weight(self, v: int, u: int) -> int:
        raise NotImplementedError("Не реализован в подклассе")

    @abstractmethod
    def get_neighbors(self, v: int) -> list:
        raise NotImplementedError("Не реализован в подклассе")

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("Не реализован в подклассе")
