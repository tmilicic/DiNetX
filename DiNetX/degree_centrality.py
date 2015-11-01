#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tanja Miličić"

import networkx as nx


def degree_centrality(graph, alpha=1):
    """
    Degree centrality is a product of the node degree,
    and his average weight adjusted by the tuning parameter.

    :param graph: NetworkX graph

    :param alpha: Positive tuning parameter

    :return: Values of degree centrality for each node
    :rtype: dictionary

    :raises ValueError: If alpha is negative

    .. note::
        If tuning parameter is between 0 and 1, then nodes with
        high degree will have greater degree centrality.
        Otherwise, if parameter is set above 1, nodes with low
        degree are taken as favorable.

    .. seealso:: in_degree_centrality, out_degree_centrality

    Reference
        .. [1] F. A. Tore Opsahl, “Node centrality in weighted networks:
            Generalizing degree and shortest paths”,
            Soc. Netw. - SOC Netw., vol. 32, no. 3, pp. 245–251, 2010.
    """

    if alpha < 0:
        raise ValueError("Alpha cannot be negative")

    degree_dict = {}

    for node in graph.nodes_iter():
        k = graph.degree(node)
        s = graph.degree(node, weight="weight")
        try:
            deg_centrality = k * (pow(s, alpha) / pow(k, alpha))
            degree_dict[node] = deg_centrality
        except ZeroDivisionError:
            degree_dict[node] = 0

    return degree_dict


def out_degree_centrality(graph, alpha=1):
    """
    Out-degree centrality is a product of the node out-degree,
    and his average out weight adjusted by the tuning parameter.

    :param graph: NetworkX graph

    :param alpha: Positive tuning parameter

    :return: Values of out-degree centrality for each node
    :rtype: dictionary

    :raises NetworkXError: If graph is undirected

    :raises ValueError: If alpha is negative

    .. note::
        If tuning parameter is between 0 and 1, then nodes with
        high out-degree will have greater out-degree centrality.
        Otherwise, if parameter is set above 1, nodes with low
        out-degree are taken as favorable.

    .. seealso:: in_degree_centrality, degree_centrality

    Reference
        .. [1] F. A. Tore Opsahl, “Node centrality in weighted networks:
            Generalizing degree and shortest paths”,
            Soc. Netw. - SOC Netw., vol. 32, no. 3, pp. 245–251, 2010.
    """

    if not graph.is_directed():
        raise nx.NetworkXError(
            "out_degree_centrality() not defined for undirected graphs.")

    if alpha < 0:
        raise ValueError("Alpha cannot be negative")

    out_degree_dict = {}

    for node in graph.nodes_iter():
        k_out = graph.out_degree(node)
        s_out = graph.out_degree(node, weight="weight")
        try:
            deg_centrality = k_out * (pow(s_out, alpha) / pow(k_out, alpha))
            out_degree_dict[node] = deg_centrality
        except ZeroDivisionError:
            out_degree_dict[node] = 0

    return out_degree_dict


def in_degree_centrality(graph, alpha=1):
    """
    In-degree centrality is a product of the node in-degree,
    and his average in weight adjusted by the tuning parameter.

    :param graph: NetworkX graph

    :param alpha: Positive tuning parameter
    :type alpha: float

    :return: Values of in-degree centrality for each node
    :rtype: dictionary

    :raises NetworkXError: If graph is undirected

    :raises ValueError: If alpha is negative

    .. note::
        If tuning parameter is between 0 and 1, then nodes with
        high in degree will have greater in-degree centrality.
        Otherwise, if parameter is set above 1, nodes with low
        in-degree are taken as favorable.

    .. seealso:: out_degree_centrality, degree_centrality

    Reference
        .. [1] F. A. Tore Opsahl, “Node centrality in weighted networks:
            Generalizing degree and shortest paths”,
            Soc. Netw. - SOC Netw., vol. 32, no. 3, pp. 245–251, 2010.
    """

    if not graph.is_directed():
        raise nx.NetworkXError(
            "in_degree_centrality() not defined for undirected graphs.")

    if alpha < 0:
        raise ValueError("Alpha cannot be negative")

    in_degree_dict = {}
    for node in graph.nodes_iter():
        k_in = graph.in_degree(node)
        s_in = graph.in_degree(node, weight="weight")
        try:
            deg_centrality = k_in * (pow(s_in, alpha) / pow(k_in, alpha))
            in_degree_dict[node] = deg_centrality
        except ZeroDivisionError:
            in_degree_dict[node] = 0

    return in_degree_dict
