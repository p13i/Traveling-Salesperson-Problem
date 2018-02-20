import unittest

import networkx as nx
from tsp import held_karp
import numpy as np
from utils import get_from_tsplib


class TSPNaiveTestCase(unittest.TestCase):
    def test_tushar_roy(self):
        A = np.matrix([
            [0, 1, 15, 6],
            [2, 0, 7, 3],
            [9, 6, 0, 12],
            [10, 4, 8, 0]
        ])

        G = nx.from_numpy_matrix(A, create_using=nx.MultiDiGraph())

        optimal_tour, optimal_cost = held_karp.solver(G, source=0)

        self.assertEqual(optimal_tour, (0, 1, 3, 2, 0))
        self.assertEqual(optimal_cost, 21)

    def test_lut_modified(self):
        A = np.matrix([
            [0, 2, 1, 6, 1],
            [1, 0, 4, 4, 2],
            [5, 3, 0, 1, 5],
            [4, 7, 2, 0, 1],
            [2, 6, 3, 6, 0],
        ])

        G = nx.from_numpy_matrix(A, create_using=nx.MultiDiGraph())

        optimal_tour, optimal_cost = held_karp.solver(G, source=0)

        self.assertEqual(optimal_tour, (0, 2, 3, 4, 1, 0))
        self.assertEqual(optimal_cost, 10)

    def test_att48(self):
        G = get_from_tsplib('./att48.xml')
        G = G.subgraph(range(0, 10))

        optimal_tour, optimal_cost = held_karp.solver(G, source=0)

        a = 42
