import networkx as nx


def check_arguments(G, source):

    if not isinstance(G, nx.MultiDiGraph):
        raise TypeError("`G` must be an instance of nx.MultiDiGraph")

    n = G.number_of_nodes()

    if G.number_of_edges() != (n * (n - 1)):
        raise ValueError("`G` is not fully connected.")

    if source not in G:
        raise ValueError("`source` node is not in `G`")


def get_adjacency_dicts(G):
    dicts = nx.to_dict_of_dicts(G)

    for n1 in dicts:
        for n2 in dicts[n1]:
            if len(dicts[n1][n2]) != 1 \
                    or 0 not in dicts[n1][n2] \
                    or 'weight' not in dicts[n1][n2][0]:
                raise ValueError("`G`'s adjacency matrix is not properly formatted.")

            dicts[n1][n2] = dicts[n1][n2][0]['weight']

    return dicts
