#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Tanja Miličić'

import networkx as nx


def h_degree(graph):
    """
    H-degree of a node is equal to n if this node has
    at least n neighbours and the strength of each link
    between them is greater or equal to n.

    For example if node A has degree 4 and weight of
    edges 1,3,3,5 then it's h-degree will be 3.

    Parameters
    ----------
    graph: NetworkX graph

    Returns
    -------
    h_degree_dict: dictionary
        Values of h-degree for each node

    References:
    ------------
    .. [1] Zhao, Star X., Ronald Rousseau, and Y. Ye Fred.
        "h-Degree as a basic measure in weighted networks",
        Journal of Informetrics 5.4 (2011): 668-677.
    """

    h_degree_dict = {}
    for node in graph.nodes_iter():
        weights = [w.get('weight') for u, c, w
                   in graph.edges(node, data=True)]

        h_degree_dict[node] = _find_h_degree(weights)

    return h_degree_dict


def in_h_degree(graph):
    """
    In-h-degree of a node is equal to n if this node has
    at least n incoming edges and the strength of each edge
    is greater or equal to n.

    For example if node A has degree 5 and weight of
    edges 5,3,3,1,1 then it's in-h-degree will be 3.

    Parameters
    ----------
    graph: NetworkX graph

    Returns
    -------
    h_degree_dict: dictionary
        Values of in-h-degree for each node

    References:
    ------------
    .. [1] Zhao, Star X., Ronald Rousseau, and Y. Ye Fred.
        "h-Degree as a basic measure in weighted networks",
        Journal of Informetrics 5.4 (2011): 668-677.
    """

    if not graph.is_directed():
        raise nx.NetworkXError(
            "in_h_degree() not defined for undirected graphs.")

    h_degree_dict = {}
    for node in graph.nodes_iter():
        in_weights = [w.get('weight') for u, c, w
                      in graph.in_edges(node, data=True)]

        h_degree_dict[node] = _find_h_degree(in_weights)

    return h_degree_dict


def out_h_degree(graph):
    """
    Out-h-degree of a node is equal to n if this node has
    at least n outgoing edges and the strength of each edge
    is greater or equal to n.

    For example if node A has out-degree 3 and weight of
    edges 3,3,2 then it's out-h-degree will be 2.

    Parameters
    ----------
    graph: NetworkX graph

    Returns
    -------
    h_degree_dict: dictionary
        Values of out-h-degree for each node

    References:
    ------------
    .. [1] Zhao, Star X., Ronald Rousseau, and Y. Ye Fred.
        "h-Degree as a basic measure in weighted networks",
        Journal of Informetrics 5.4 (2011): 668-677.
    """

    if not graph.is_directed():
        raise nx.NetworkXError(
            "out_h_degree() not defined for undirected graphs.")

    h_degree_dict = {}
    for node in graph.nodes_iter():
        out_weights = [w.get('weight') for u, c, w
                       in graph.out_edges(node, data=True)]

        h_degree_dict[node] = _find_h_degree(out_weights)

    return h_degree_dict


def _find_h_degree(weights):
    i = 1
    best_h_degree = 1
    while True:
        tmp = len([x for x in weights if x >= i])
        if i < tmp:
            best_h_degree = i
        elif i == tmp:
            best_h_degree = tmp
        else:
            break
        i += 1

    return best_h_degree

