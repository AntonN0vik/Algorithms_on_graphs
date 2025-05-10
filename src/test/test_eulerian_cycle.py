import unittest
from src.main.algorithms.eulerian_cycle import eulerian_cycle
from src.main.graphs.graph_adjacency_list import GraphAdjacencyList
from src.main.graphs.graph_adjacency_matrix import GraphAdjacencyMatrix
from src.main.graphs.graph_edge_list import GraphEdgeList


class TestEulerianCycle(unittest.TestCase):
    def setUp(self):
        self.expected_cycle = [0, 1, 2, 0]

    def test_cycle_adjacency_list(self):
        graph = GraphAdjacencyList(directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)

        result = eulerian_cycle(graph, 0)
        self.assertEqual(result, self.expected_cycle)

    def test_cycle_adjacency_matrix(self):
        graph = GraphAdjacencyMatrix(3, directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)

        result = eulerian_cycle(graph, 0)
        self.assertEqual(result, self.expected_cycle)

    def test_cycle_edge_list(self):
        graph = GraphEdgeList(directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)

        result = eulerian_cycle(graph, 0)
        self.assertEqual(result, self.expected_cycle)

    def test_multiple_edges(self):
        expected = [0, 1, 0, 2, 0]
        graph = GraphAdjacencyList(directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 0)
        graph.add_edge(2, 0)

        result = eulerian_cycle(graph, 0)
        self.assertEqual(result, expected)

    def test_single_vertex(self):
        graph = GraphAdjacencyList(directed=True)
        graph._adjacency_list[0] = []

        result = eulerian_cycle(graph, 0)
        self.assertEqual(result, [0])


if __name__ == '__main__':
    unittest.main()
