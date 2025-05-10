import unittest
from src.main.graphs.graph_adjacency_matrix import GraphAdjacencyMatrix


class TestGraphAdjacencyMatrix(unittest.TestCase):
    def setUp(self):
        self.graph_undirected = GraphAdjacencyMatrix(3, directed=False)
        self.graph_directed = GraphAdjacencyMatrix(3, directed=True)

    def test_initialization(self):
        empty_graph = GraphAdjacencyMatrix(3)
        expected_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(empty_graph._adj_matrix, expected_matrix)
        self.assertFalse(self.graph_undirected._directed)
        self.assertTrue(self.graph_directed._directed)

    def test_get_vertex_count(self):
        self.assertEqual(self.graph_undirected.get_vertices_count(), 3)

    def test_get_edges_count(self):
        self.assertEqual(self.graph_undirected.get_edges_count(), 3)

    def test_add_edge_undirected(self):
        self.graph_undirected.add_edge(0, 1, 10)
        self.assertEqual(self.graph_undirected._adj_matrix[0][1], 10)
        self.assertEqual(self.graph_undirected._adj_matrix[1][0], 10)

    def test_add_edge_directed(self):
        self.graph_directed.add_edge(0, 1, 10)
        self.assertEqual(self.graph_directed._adj_matrix[0][1], 10)
        self.assertEqual(self.graph_directed._adj_matrix[1][0], 0)

    def test_remove_edge_undirected(self):
        self.graph_undirected.add_edge(0, 1, 10)
        self.graph_undirected.remove_edge(0, 1)
        self.assertEqual(self.graph_undirected._adj_matrix[0][1], 0)
        self.assertEqual(self.graph_undirected._adj_matrix[1][0], 0)

    def test_remove_edge_directed(self):
        self.graph_directed.add_edge(0, 1, 10)
        self.graph_directed.remove_edge(0, 1)
        self.assertEqual(self.graph_directed._adj_matrix[0][1], 0)
        self.assertEqual(self.graph_directed._adj_matrix[1][0], 0)

    def test_has_edge_undirected(self):
        self.graph_undirected.add_edge(1, 2, weight=5)
        self.assertEqual(self.graph_undirected.has_edge(1, 2), True)
        self.assertEqual(self.graph_undirected.has_edge(2, 1), True)

    def test_has_edge_weight_directed(self):
        self.graph_directed.add_edge(1, 2, weight=5)
        self.assertEqual(self.graph_directed.has_edge(1, 2), True)
        self.assertEqual(self.graph_directed.has_edge(2, 1), False)

    def test_get_edge_weight_undirected(self):
        self.graph_undirected.add_edge(1, 2, weight=5)
        self.assertEqual(self.graph_undirected.get_edge_weight(1, 2), 5)
        self.assertEqual(self.graph_undirected.get_edge_weight(2, 1), 5)

    def test_get_edge_weight_directed(self):
        self.graph_directed.add_edge(1, 2, weight=5)
        self.assertEqual(self.graph_directed.get_edge_weight(1, 2), 5)
        self.assertEqual(self.graph_directed.get_edge_weight(2, 1), 0)

    def test_get_neighbors_no_edges(self):
        neighbors = self.graph_undirected.get_neighbors(1)
        self.assertEqual(neighbors, [])

    def test_get_neighbors_undirected(self):
        self.graph_undirected.add_edge(0, 1, 10)
        self.graph_undirected.add_edge(0, 2, 5)
        neighbors = self.graph_undirected.get_neighbors(0)
        expected_neighbors = [(1, 10), (2, 5)]
        self.assertListEqual(neighbors, expected_neighbors)

    def test_get_neighbors_directed(self):
        self.graph_directed.add_edge(0, 1, 10)
        self.graph_directed.add_edge(0, 2, 5)
        neighbors = self.graph_directed.get_neighbors(0)
        expected_neighbors = [(1, 10), (2, 5)]
        self.assertListEqual(neighbors, expected_neighbors)

    def test_str(self):
        self.graph_undirected.add_edge(0, 1, 2)
        expected_output = (
            "0 2 0 \n"
            "2 0 0 \n"
            "0 0 0 \n"
        )
        self.assertEqual(self.graph_undirected.__str__(), expected_output)


if __name__ == '__main__':
    unittest.main()
