import unittest
import logging
from parameterized import parameterized
import inspect

import numpy as np
import networkx as nx

from gt_tsp import naive, held_karp

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestingGraph(object):
    def __init__(self, name, A, source,
                 optimal_tour_solution, optimal_cost_solution):
        """
        Simple wrapper for graphs used when testing this package.
        Allows for code re-use between the packages
        :param name: The name of this graph
        :param A: The adjacency matrix
        :param source: The source node
        :param optimal_tour_solution: The solved tour
        :param optimal_cost_solution: The cost of the solution
        """
        self.name = name
        self.A = A
        self.source = source
        self.optimal_tour_solution = optimal_tour_solution
        self.optimal_cost_solution = optimal_cost_solution


TESTING_GRAPHS = [
    TestingGraph(
        name='tushar_roy',
        A=np.matrix([
            [0, 1, 15, 6],
            [2, 0, 7, 3],
            [9, 6, 0, 12],
            [10, 4, 8, 0],
        ]),
        source=0,
        optimal_tour_solution=(0, 1, 3, 2, 0),
        optimal_cost_solution=21,
    ),
    TestingGraph(
        name='2',
        A=np.matrix([
            [0, 2, 1, 6, 1],
            [1, 0, 4, 4, 2],
            [5, 3, 0, 1, 5],
            [4, 7, 2, 0, 1],
            [3, 6, 3, 6, 0],
        ]),
        source=0,
        optimal_tour_solution=(0, 2, 3, 4, 1, 0),
        optimal_cost_solution=10,
    ),
]

SOLVER_FUNCS = [naive.solver, held_karp.solver]


def get_method_name(solver_func, testing_graph):
    return 'Test: %s.%s on graph %s' % (
        inspect.getmodule(solver_func).__name__,
        solver_func.__name__, testing_graph.name,)


tests = [
    # The tuple below ends up being the *args to the test function
    (get_method_name(solver_func, testing_graph), solver_func, testing_graph)
    for solver_func in SOLVER_FUNCS
    for testing_graph in TESTING_GRAPHS
]


class TSPSolverTestCase(unittest.TestCase):

    @parameterized.expand(tests)
    def test(self, test_name, solver_func, testing_graph):
        G = nx.from_numpy_matrix(
            A=testing_graph.A,
            create_using=nx.MultiDiGraph(),
        )

        logger.info('Running: %s' % test_name)

        optimal_tour, optimal_cost = solver_func(G, testing_graph.source)
        logger.debug('Computed optimal tour: %s' % str(optimal_tour))
        logger.debug('Computed optimal cost: %d' % optimal_cost)

        self.assertEqual(testing_graph.optimal_tour_solution, optimal_tour)
        self.assertEqual(testing_graph.optimal_cost_solution, optimal_cost)
