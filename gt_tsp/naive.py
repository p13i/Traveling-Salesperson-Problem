from typing import Tuple, List, Any, Dict  # noqa: 401
import networkx as nx  # noqa: 401
import itertools
from gt_tsp import INFINITY
from . import utils


def solver(G, source):  # type: (nx.Graph, Any) -> Tuple[Tuple[Any, ...], int]
    """
    Produces the optimal TSP tour using a naive solution - O(n!)
    :param G: A fully connected networkx graph.
    :param source: A source node in G.
    :return: A list of nodes to visit, forming a TSP tour, and the cost of
    that tour.
    """

    utils.check_arguments(G, source)

    n = G.number_of_nodes()

    best_node_permutation = tuple()  # type: Tuple[Any, ...]
    best_cost = INFINITY

    distance = utils.get_adjacency_dicts(G)

    for node_permutation in itertools.permutations(G.nodes):
        if node_permutation[0] != source:
            continue

        cost_of_node_permutation = 0
        for i in range(0, n):
            current_node = node_permutation[i]
            next_node = node_permutation[(i + 1) % n]
            cost_of_node_permutation += distance[current_node][next_node]

        if cost_of_node_permutation < best_cost:
            best_node_permutation = tuple(node_permutation + (source,))
            best_cost = cost_of_node_permutation

    return best_node_permutation, best_cost
