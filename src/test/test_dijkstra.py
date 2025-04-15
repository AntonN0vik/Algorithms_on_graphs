import unittest
from src.main.algorithms.dijkstra import dijkstra
from src.main.algorithms.shortest_path import get_shortest_path
from src.main.graphs.graph_adjacency_list import GraphAdjacencyList
from src.main.graphs.graph_adjacency_matrix import GraphAdjacencyMatrix
from src.main.graphs.graph_edge_list import GraphEdgeList


class TestDijkstra(unittest.TestCase):
    def test_shortest_path_undirected_graph(self):
        graph = GraphAdjacencyList()

        graph.add_edge(0, 1, 4)
        graph.add_edge(0, 2, 2)
        graph.add_edge(1, 2, 1)
        graph.add_edge(1, 3, 5)
        graph.add_edge(2, 3, 8)
        graph.add_edge(2, 4, 10)
        graph.add_edge(3, 4, 2)

        distances, previous = dijkstra(graph, 0)

        self.assertEqual(distances, [0, 3, 2, 8, 10])
        self.assertEqual(previous, [None, 2, 0, 1, 3])
        self.assertEqual(get_shortest_path(previous, 0, 4), [0, 2, 1, 3, 4])

    def test_shortest_path_directed_graph(self):
        graph = GraphAdjacencyList(directed=True)
        graph.add_edge(0, 1, 2)
        graph.add_edge(0, 2, 6)
        graph.add_edge(1, 3, 5)
        graph.add_edge(2, 3, 8)
        graph.add_edge(3, 0, 10)

        distances, previous = dijkstra(graph, 0)

        self.assertEqual(distances, [0, 2, 6, 7])
        self.assertEqual(previous, [None, 0, 0, 1])
        self.assertEqual(get_shortest_path(previous, 0, 3), [0, 1, 3])

    def test_different_graph_representations(self):
        adj_list_graph = GraphAdjacencyList()
        adj_list_graph.add_edge(0, 1, 2)
        adj_list_graph.add_edge(0, 2, 4)
        adj_list_graph.add_edge(1, 2, 1)
        adj_list_graph.add_edge(1, 3, 7)
        adj_list_graph.add_edge(2, 3, 3)

        adj_matrix_graph = GraphAdjacencyMatrix(4)
        adj_matrix_graph.add_edge(0, 1, 2)
        adj_matrix_graph.add_edge(0, 2, 4)
        adj_matrix_graph.add_edge(1, 2, 1)
        adj_matrix_graph.add_edge(1, 3, 7)
        adj_matrix_graph.add_edge(2, 3, 3)

        edge_list_graph = GraphEdgeList()
        edge_list_graph.add_edge(0, 1, 2)
        edge_list_graph.add_edge(0, 2, 4)
        edge_list_graph.add_edge(1, 2, 1)
        edge_list_graph.add_edge(1, 3, 7)
        edge_list_graph.add_edge(2, 3, 3)

        distances1, _ = dijkstra(adj_list_graph, 0)
        distances2, _ = dijkstra(adj_matrix_graph, 0)
        distances3, _ = dijkstra(edge_list_graph, 0)

        expected_distances = [0, 2, 3, 6]
        self.assertEqual(distances1, expected_distances)
        self.assertEqual(distances2, expected_distances)
        self.assertEqual(distances3, expected_distances)

    def test_path_to_self(self):
        graph = GraphAdjacencyList()
        graph.add_edge(0, 1, 1)
        distances, previous = dijkstra(graph, 0)
        self.assertEqual(get_shortest_path(previous, 0, 0), [0])


if __name__ == '__main__':
    unittest.main()
