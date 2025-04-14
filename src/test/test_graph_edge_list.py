import unittest
from src.main.graphs.graph_edge_list import GraphEdgeList


class TestGraphEdgeList(unittest.TestCase):
    def setUp(self):
        self.graph = GraphEdgeList()

    def test_add_edge(self):
        self.graph.add_edge(1, 2)
        self.assertTrue(self.graph.has_edge(1, 2))
        self.assertTrue(self.graph.has_edge(2, 1))

    def test_get_vertices_count(self):
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        self.assertEqual(self.graph.get_vertices_count(), 3)

    def test_get_edges_count_undirected(self):
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        self.assertEqual(self.graph.get_edges_count(), 4)

    def test_get_edges_count_directed(self):
        directed_graph = GraphEdgeList(directed=True)
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
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        vertices = self.graph.get_vertices_list()
        self.assertIn(1, vertices)
        self.assertIn(2, vertices)
        self.assertIn(3, vertices)
        self.assertEqual(len(vertices), 3)

    def test_get_edges_list_undirected(self):
        self.graph.add_edge(1, 2, weight=3)
        edges = self.graph.get_edges_list()
        self.assertIn((1, 2, 3), edges)
        self.assertIn((2, 1, 3), edges)
        self.assertEqual(len(edges), 2)

    def test_get_edges_list_directed(self):
        directed_graph = GraphEdgeList(directed=True)
        directed_graph.add_edge(1, 2, weight=3)
        directed_graph.add_edge(2, 3, weight=5)
        edges = directed_graph.get_edges_list()
        self.assertIn((1, 2, 3), edges)
        self.assertIn((2, 3, 5), edges)
        self.assertNotIn((2, 1, 3), edges)
        self.assertNotIn((3, 2, 5), edges)
        self.assertEqual(len(edges), 2)

    def test_str(self):
        self.graph.add_edge(1, 2, weight=3)
        output_str = str(self.graph)
        self.assertIn("(1, 2, weight=3)", output_str)
        self.assertIn("(2, 1, weight=3)", output_str)


if __name__ == '__main__':
    unittest.main()
