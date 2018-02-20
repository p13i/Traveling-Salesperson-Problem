import xml.etree.ElementTree as ET
import networkx as nx


def get_from_tsplib(filepath):
    e = ET.parse(filepath)
    root = e.getroot()
    graph = root.find('graph')

    G = nx.MultiDiGraph()

    for i, vertex in enumerate(graph.getchildren()):
        v = i
        G.add_node(v)

        for edge in vertex.getchildren():
            G.add_edge(v, int(edge.text), weight=float(edge.attrib['cost']))

    return G
