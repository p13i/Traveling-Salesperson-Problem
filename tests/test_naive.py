import unittest

import networkx as nx
from tsp import naive


class TSPNaiveTestCase(unittest.TestCase):
    def test_graph_not_fully_connected(self):
        G = nx.Graph()

        G.add_nodes_from([1, 2, 3])
        # Edge (3, 1) is missing
        G.add_edges_from([(1, 2), (2, 3)])

        with self.assertRaises(ValueError):
            naive.solver(G, 1)

    def test_source_not_in_graph(self):
        G = nx.Graph()

        with self.assertRaises(ValueError):
            naive.solver(G, 1)

    def test_small_graph(self):
        G = nx.Graph()

        G.add_nodes_from([1, 2, 3, 4])
        G.add_edge(1, 2, cost=6)
        G.add_edge(2, 3, cost=5)
        G.add_edge(3, 4, cost=4)
        G.add_edge(4, 1, cost=3)
        G.add_edge(1, 3, cost=2)
        G.add_edge(2, 4, cost=1)

        optimal_path, optimal_cost = naive.solver(G, 1)

        self.assertEqual(optimal_path, (1, 3, 4, 2))
        self.assertEqual(optimal_cost, 7)
