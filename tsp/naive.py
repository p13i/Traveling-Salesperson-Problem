import typing
import networkx as nx
import itertools
from tsp import INFINITY


def solver(G, source):  # type: (nx.Graph, typing.Any) -> typing.Tuple[typing.List[typing.Any], int]
    """
    Produces the optimal TSP tour using a naive solution - O(n!)
    :param G: A fully connected networkx graph.
    :param source: A source node in G.
    :return: A list of nodes to visit, forming a TSP tour, and the cost of that tour.
    """

    n = G.number_of_nodes()

    if G.number_of_edges() != (n * (n - 1) // 2):
        raise ValueError("`graph` is not fully connected.")

    if source not in G:
        raise ValueError("`source` is not in `graph`")

    best_node_permutation = None
    best_cost = INFINITY

    for node_permutation in itertools.permutations(G.nodes):
        if node_permutation[0] is not source:
            continue

        cost_of_node_permutation = 0
        for i in range(0, n - 1):
            current_node = node_permutation[i]
            next_node = node_permutation[i + 1]
            edge = G.get_edge_data(current_node, next_node)
            cost_of_node_permutation += edge['cost']

        if cost_of_node_permutation < best_cost:
            best_node_permutation = node_permutation
            best_cost = cost_of_node_permutation

    return best_node_permutation, best_cost
