#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tanja Miličić"


import networkx as nx


def global_efficiency(graph, weight=True, to_undirected=False):

    n = graph.order()
    sum_dij = 0

    if to_undirected is True:
        graph = graph.to_undirected()

    if weight is True:
        for node in graph.nodes():
            shortest_paths = nx.single_source_dijkstra_path_length(graph, node)
            sum_dij += sum(1 / d_ij for d_ij in shortest_paths.values() if d_ij != 0)

    else:
        for node in graph.nodes():
            shortest_paths = nx.single_source_shortest_path_length(graph, node)
            sum_dij += sum(1 / d_ij for d_ij in shortest_paths.values() if d_ij != 0)

    try:
        efficiency = 1. / (n * (n - 1)) * sum_dij
    except ZeroDivisionError:
        efficiency = 0

    return efficiency


def local_efficiency(graph, weight=True, to_undirected=False):

    if to_undirected is True:
        graph = graph.to_undirected()

    sum_global_efficiency = 0
    for node in graph:
        neighbors = graph.neighbors(node)
        subgraph = graph.subgraph(neighbors)
        glob_efficiency = global_efficiency(subgraph, weight, to_undirected)
        sum_global_efficiency += glob_efficiency

    efficiency = 1. / graph.order() * sum_global_efficiency

    return efficiency

