import unittest
from src.main.graphs.graph_adjacency_list import GraphAdjacencyList


class TestGraphAdjacencyList(unittest.TestCase):
    def setUp(self):
        self.graph_undirected = GraphAdjacencyList(directed=False)
        self.graph_directed = GraphAdjacencyList(directed=True)

    def test_initialization(self):
        graph = GraphAdjacencyList()
        self.assertFalse(graph._directed)
        self.assertEqual(graph._adj_list, {})
        self.assertFalse(self.graph_undirected._directed)
        self.assertTrue(self.graph_directed._directed)

    def test_get_vertices_count(self):
        self.assertEqual(self.graph_undirected.get_vertices_count(), 0)
        self.graph_undirected.add_edge(0, 1)
        self.graph_undirected.add_edge(2, 3)
        self.assertEqual(self.graph_undirected.get_vertices_count(), 4)

    def test_get_edges_count(self):
        self.assertEqual(self.graph_undirected.get_edges_count(), 0)
        self.graph_undirected.add_edge(0, 1)
        self.assertEqual(self.graph_undirected.get_edges_count(), 1)
        self.graph_undirected.add_edge(1, 2)
        self.assertEqual(self.graph_undirected.get_edges_count(), 2)
        self.assertEqual(self.graph_directed.get_edges_count(), 0)
        self.graph_directed.add_edge(0, 1)
        self.assertEqual(self.graph_directed.get_edges_count(), 1)

    def test_add_edge_undirected(self):
        self.graph_undirected.add_edge(0, 1, 10)
        self.assertIn(1, [neighbor[0] for neighbor in self.graph_undirected._adj_list[0]])
        self.assertIn(0, [neighbor[0] for neighbor in self.graph_undirected._adj_list[1]])
        self.assertEqual(self.graph_undirected._adj_list[0][0][1], 10)
        self.assertEqual(self.graph_undirected._adj_list[1][0][1], 10)

    def test_add_edge_directed(self):
        self.graph_directed.add_edge(0, 1, 10)
        self.assertIn(1, [neighbor[0] for neighbor in self.graph_directed._adj_list[0]])
        self.assertNotIn(0, [neighbor[0] for neighbor in self.graph_directed._adj_list[1]])
        self.assertEqual(self.graph_directed._adj_list[0][0][1], 10)

    def test_remove_edge_undirected(self):
        self.graph_undirected.add_edge(0, 1, 10)
        self.graph_undirected.remove_edge(0, 1)
        self.assertFalse(self.graph_undirected.has_edge(0, 1))
        self.assertFalse(self.graph_undirected.has_edge(1, 0))

    def test_remove_edge_directed(self):
        self.graph_directed.add_edge(0, 1, 10)
        self.graph_directed.remove_edge(0, 1)
        self.assertFalse(self.graph_directed.has_edge(0, 1))

    def test_has_edge_undirected(self):
        self.graph_undirected.add_edge(1, 2, weight=5)
        self.assertTrue(self.graph_undirected.has_edge(1, 2))
        self.assertTrue(self.graph_undirected.has_edge(2, 1))

    def test_has_edge_directed(self):
        self.graph_directed.add_edge(1, 2, weight=5)
        self.assertTrue(self.graph_directed.has_edge(1, 2))
        self.assertFalse(self.graph_directed.has_edge(2, 1))

    def test_get_edge_weight_undirected(self):
        self.graph_undirected.add_edge(1, 2, weight=5)
        self.assertEqual(self.graph_undirected.get_edge_weight(1, 2), 5)
        self.assertEqual(self.graph_undirected.get_edge_weight(2, 1), 5)

    def test_get_edge_weight_directed(self):
        self.graph_directed.add_edge(1, 2, weight=5)
        self.assertEqual(self.graph_directed.get_edge_weight(1, 2), 5)
        self.assertEqual(self.graph_directed.get_edge_weight(2, 1), 0)

    def test_get_neighbors_no_edges(self):
        neighbors = self.graph_undirected.get_neighbors(0)
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
        output_str = str(self.graph_undirected)
        self.assertIn("0: [(1, 2)]", output_str)
        self.assertIn("1: [(0, 2)]", output_str)


if __name__ == '__main__':
    unittest.main()
