from abc import ABC, abstractmethod


class Graph(ABC):
    @abstractmethod
    def get_vertices_count(self) -> int:
        """Вернуть кол-во вершин в графе"""
        pass

    @abstractmethod
    def get_edges_count(self) -> int:
        """Вернуть кол-во ребер в графе"""
        pass

    @abstractmethod
    def get_vertices_list(self) -> list[str]:
        """Вернуть список всех вершин в графе"""
        pass

    @abstractmethod
    def get_edges_list(self) -> list[tuple[str, str]]:
        """Вернуть список всех рёбер без учёта весов"""
        pass

    @abstractmethod
    def add_edge(self, v: int, u: int, weight=1):
        """Добавить ребро между вершинами v и u с весом weight"""
        pass

    @abstractmethod
    def remove_edge(self, v: int, u: int):
        """Удалить ребро между вершинами v и u"""
        pass

    @abstractmethod
    def has_edge(self, v: int, u: int) -> bool:
        """Проверить, существует ли ребро между вершинами v и u"""
        pass

    @abstractmethod
    def get_edge_weight(self, v: int, u: int) -> int:
        """Получить вес ребра между вершинами v и u"""
        pass

    @abstractmethod
    def get_neighbors(self, v: int) -> list[tuple[int, int]]:
        """Получить список соседей и веса для вершины v"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Вернуть строковое представление графа"""
        pass
