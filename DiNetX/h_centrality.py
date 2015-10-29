__author__ = 'tanja'

from DiNetX import h_degree


def h_centrality(graph):
    """
    H-centrality is ratio of h-degree and N-1 nodes.
    """
    h_degrees = h_degree.h_degree(graph)
    h_centrality_dict = {}
    for node, h_deg in h_degrees.iteritems():
        h_centrality_dict[node] = float(h_deg) / (graph.order() - 1)

    return h_centrality_dict


def in_h_centrality(graph):
    h_degrees = h_degree.in_h_degree(graph)
    h_centrality_dict = {}
    for node, h_deg in h_degrees.iteritems():
        h_centrality_dict[node] = float(h_deg) / (graph.order() - 1)

    return h_centrality_dict


def out_h_centrality(graph):
    h_degrees = h_degree.out_h_degree(graph)
    h_centrality_dict = {}
    for node, h_deg in h_degrees.iteritems():
        h_centrality_dict[node] = float(h_deg) / (graph.order() - 1)

    return h_centrality_dict