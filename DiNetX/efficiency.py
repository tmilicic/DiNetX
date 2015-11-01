#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tanja Miličić"


import networkx as nx


def global_efficiency(graph, weight=True, to_undirected=False):
    """
    Compute value of global efficiency for a given graph.

    :param graph: NetworkX graph

    :param weight:
        If True then all shortest paths will be computed
        as a sum of weights of all traversed edges.
        Else shortest paths will be sum of jumps needed
        from one node to every other.

    :type weight: boolean, (default = True)

    :param to_undirected:
        If True all edges will become undirected.

    :type to_undirected: boolean, (default = False)

    :return: Value of global efficiency for given graph
    :rtype: dictionary

    .. seealso::
        :py:func:`local_efficiency`

    Reference
        .. [1] V. Latora and M. Marchiori,
            “Efficient Behavior of Small-World Networks”,
            Phys.Rev. Lett., vol. 87, no. 19, Oct. 2001.
    """
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
    """
    Compute local efficiency for a given graph.
    Local efficiency is the average efficiency of
    the local subgraphs.

    :param graph: NetworkX graph

    :param weight:
        If True then all shortest paths will be computed
        as a sum of weights of all traversed edges.
        Else shortest paths will be sum of jumps needed
        from one node to every other.
    :type weight: boolean, (default = True)

    :param to_undirected: If True all edges will become undirected.
    :type to_undirected: boolean, (default = False)

    :return: Value of local efficiency of given graph
    :rtype: dictionary

    .. seealso::
        :py:func:`global_efficiency`

    .. note::
        Local efficiency shows similar characteristics as
        clustering coefficient. It reveals how much the system
        is fault tolerant, in other words it shows how efficient
        the communication is between the first neighbors of i when
        i is removed.

    Reference
        .. [1] V. Latora and M. Marchiori,
            “Efficient Behavior of Small-World Networks”,
            Phys.Rev. Lett., vol. 87, no. 19, Oct. 2001.
    """

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

