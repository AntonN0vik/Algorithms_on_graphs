import unittest
from src.main.graphs.graph_adjacency_matrix import GraphAdjacencyMatrix


class TestGraphAdjacencyMatrix(unittest.TestCase):
    def setUp(self):
        self.graph = GraphAdjacencyMatrix(5)

    def test_add_edge(self):
        self.graph.add_edge(1, 2)
        self.assertTrue(self.graph.has_edge(1, 2))
        self.assertTrue(self.graph.has_edge(2, 1))

    def test_get_vertices_count(self):
        self.assertEqual(self.graph.get_vertices_count(), 5)

    def test_get_edges_count_undirected(self):
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        self.assertEqual(self.graph.get_edges_count(), 2)

    def test_get_edges_count_directed(self):
        directed_graph = GraphAdjacencyMatrix(5, directed=True)
        directed_graph.add_edge(1, 2)
        directed_graph.add_edge(2, 3)
        self.assertEqual(directed_graph.get_edges_count(), 2)

    def test_remove_edge(self):
        self.graph.add_edge(1, 2)
        self.graph.remove_edge(1, 2)
        self.assertFalse(self.graph.has_edge(1, 2))
        self.assertFalse(self.graph.has_edge(2, 1))

    def test_has_edge(self):
        self.graph.add_edge(1, 2)
        self.assertTrue(self.graph.has_edge(1, 2))
        self.assertFalse(self.graph.has_edge(1, 3))

    def test_get_edge_weight(self):
        self.graph.add_edge(1, 2, weight=3)
        self.assertEqual(self.graph.get_edge_weight(1, 2), 3)
        self.assertEqual(self.graph.get_edge_weight(2, 1), 3)

    def test_get_neighbors(self):
        self.graph.add_edge(1, 2, weight=3)
        self.graph.add_edge(1, 3, weight=5)
        neighbors = self.graph.get_neighbors(1)
        self.assertIn((2, 3), neighbors)
        self.assertIn((3, 5), neighbors)
        self.assertEqual(len(neighbors), 2)

    def test_get_vertices_list(self):
        vertices = self.graph.get_vertices_list()
        self.assertEqual(len(vertices), 5)
        for i in range(5):
            self.assertIn(str(i), vertices)

    def test_get_edges_list_undirected(self):
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        edges = self.graph.get_edges_list()
        self.assertIn(('1', '2'), edges)
        self.assertIn(('2', '3'), edges)
        self.assertEqual(len(edges), 2)

    def test_get_edges_list_directed(self):
        directed_graph = GraphAdjacencyMatrix(5, directed=True)
        directed_graph.add_edge(1, 2)
        directed_graph.add_edge(2, 3)
        edges = directed_graph.get_edges_list()
        self.assertIn(('1', '2'), edges)
        self.assertIn(('2', '3'), edges)
        self.assertNotIn(('2', '1'), edges)
        self.assertNotIn(('3', '2'), edges)
        self.assertEqual(len(edges), 2)

    def test_str(self):
        self.graph.add_edge(1, 2, weight=3)
        expected_representation = (
            "0 0 0 0 0 \n"
            "0 0 3 0 0 \n"
            "0 3 0 0 0 \n"
            "0 0 0 0 0 \n"
            "0 0 0 0 0 \n"
        )
        self.assertEqual(str(str(self.graph)), expected_representation)


if __name__ == '__main__':
    unittest.main()
