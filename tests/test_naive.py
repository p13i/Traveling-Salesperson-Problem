import unittest
import numpy as np
import networkx as nx
from tsp import naive


class TSPHeldKarpTestCase(unittest.TestCase):
    def test_tushar_roy(self):
        """
        Based on graph from: https://www.youtube.com/watch?v=-JjA4BLQyqE
        """

        A = np.matrix([
            [ 0,  1, 15,  6],
            [ 2,  0,  7,  3],
            [ 9,  6,  0, 12],
            [10,  4,  8,  0],
        ])

        G = nx.from_numpy_matrix(A, create_using=nx.MultiDiGraph())

        optimal_tour, optimal_cost = naive.solver(G, 0)

        self.assertEqual((0, 1, 3, 2, 0), optimal_tour)
        self.assertEqual(21, optimal_cost)

    def test_2(self):
        A = np.matrix([
            [0, 2, 1, 6, 1],
            [1, 0, 4, 4, 2],
            [5, 3, 0, 1, 5],
            [4, 7, 2, 0, 1],
            [3, 6, 3, 6, 0],
        ])

        G = nx.from_numpy_matrix(A, create_using=nx.MultiDiGraph())

        optimal_tour, optimal_cost = naive.solver(G, 0)

        self.assertEqual((0, 2, 3, 4, 1, 0), optimal_tour)
        self.assertEqual(10, optimal_cost)
