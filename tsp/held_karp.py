import typing
import networkx as nx
import itertools
from tsp import INFINITY
import copy


def solver(G, source):  # type: (nx.Graph, typing.Any) -> typing.Tuple[typing.List[typing.Any], int]
    """
    Produces the optimal TSP tour using the Held-Karp, dynamic programming approach - O(n^2 * 2^n)
    :param G: A fully connected networkx MultiDiGraph.
    :param source: A source node in G.
    :return: A list of nodes to visit, forming a TSP tour, and the cost of that tour.
    """

    n = G.number_of_nodes()

    if source not in G:
        raise ValueError("`source` is not in `graph`")

    distance = get_adjacency_dicts(G)

    min_cost_dp = {}  # type: typing.Dict[Index, int]
    parent = {}  # type: typing.Dict[Index, typing.Any]

    nodes_except_source = list(G.nodes)
    nodes_except_source.remove(source)

    for _set in _power_set(nodes_except_source):  # type: set
        _set = set(_set)

        for current_vertex in nodes_except_source:
            if current_vertex in _set:
                continue

            index = Index(current_vertex, _set)

            min_cost = INFINITY

            min_prev_vertex = source

            set_copy = set(copy.deepcopy(_set))

            for prev_vertex in _set:
                cost = distance[prev_vertex][current_vertex]['weight'] + _get_cost(set_copy, prev_vertex, min_cost_dp)
                if cost < min_cost:
                    min_cost = cost
                    min_prev_vertex = prev_vertex

            if len(_set) == 0:
                min_cost = distance[source][current_vertex]['weight']

            min_cost_dp[index] = min_cost
            parent[index] = min_prev_vertex

    _set = set(nodes_except_source)
    min = INFINITY
    prev_vertex = None
    set_copy = copy.deepcopy(_set)

    for vertex in _set:
        cost = distance[vertex][source]['weight'] + _get_cost(set_copy, vertex, min_cost_dp)
        if cost < min:
            min = cost
            prev_vertex = vertex

    parent[Index(source, _set)] = prev_vertex

    tour = _get_tour(source, parent, G.nodes)

    return tour, min


def get_adjacency_dicts(G):
    dicts = nx.to_dict_of_dicts(G)

    if isinstance(G, nx.MultiDiGraph):

        for n1 in dicts:
            for n2 in dicts[n1]:
                if len(dicts[n1][n2]) != 1 \
                        or 0 not in dicts[n1][n2]:
                    raise ValueError()

                dicts[n1][n2] = dicts[n1][n2][0]

    return dicts

def _get_tour(source, parent, nodes):
    _set = set(nodes)

    start = source

    stack = []

    while True:
        stack.append(start)
        _set.remove(start)
        start = parent[Index(start, _set)]
        if start == source:
            break

    stack.append(source)

    return tuple(stack[::-1])

def _get_cost(set, prev_vertex, min_cost_dp):
    set.remove(prev_vertex)
    index = Index(prev_vertex, set)
    cost = min_cost_dp[index]
    set.add(prev_vertex)
    return cost


def _power_set(s):
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


class Index(object):
    def __init__(self, vertex, vertex_set):
        self.vertex = vertex  # type: typing.Any
        self.vertex_set = frozenset(vertex_set)  # type: frozenset

    def __eq__(self, other):
        if other is None or not isinstance(other, Index):
            return False
        return other.vertex == self.vertex \
            and other.vertex_set == self.vertex_set

    def __hash__(self):
        return 31 * self.vertex + hash(self.vertex_set)

    def __str__(self):
        return "%s - {%s}" % (self.vertex, self.vertex_set)
