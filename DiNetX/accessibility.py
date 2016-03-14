#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import math


def accessibility(graph, weighted=True, h=3):
    """
    Accessibility provide an estimate of the number of nodes
    that can be visited in exactly h steps.

    :param graph: NetworkX graph
    :param weighted:
        If True than probabilities p_ij will be computed
        as fraction of sum of weights of level h and
        weight of edges connecting i and j or neighbors of i and j.
    :param h: number of steps
    :return: Values of accessibility for each node
    :rtype: dictionary where keys are as follows - n_h_j, where
        n represents node name, and j is current number of steps.

    .. note:: If graph is directed it will be converted to
    undirected one.

    .. seealso::
        :py:func:`in_accessibility`, :py:func:`out_accessibility`
    """
    if graph.is_directed():
        graph.to_undirected()

    accessibility_dict = {}
    for node in graph.nodes_iter():
        i = 1; neighbors = {}
        successors = graph.edges(node)
        neighbors[i] = successors
        _neighbors(graph, successors, neighbors, h-1, i+1)
        for j in range(1, h+1):
            if weighted:
                weights = sum([int(graph.get_edge_data(u, v).get('weight'))
                               for u, v in neighbors[j]])
            else:
                weights = len(neighbors[j])
            acc = 0
            tmp1 = [x[0] for x in neighbors[j]]
            tmp2 = [x[1] for x in neighbors[j]]

            for n in set(tmp2):
                weight = 0; degree = 0
                for s in set(tmp1):
                    if weighted:
                        if graph.has_edge(s, n):
                            weight += float(graph.get_edge_data(s, n).get('weight'))
                    else:
                        if graph.has_edge(s,n):
                            degree += 1.
                if weighted:
                    p_ij = weight/weights
                else:
                    p_ij = degree/weights
                try:
                    log_p_ij = math.log(p_ij)
                    acc += -1 * (p_ij * math.log(p_ij))
                except ValueError:
                    continue

            accessibility_dict[str(node) + '_h_' + str(j)] = math.exp(acc)

    return accessibility_dict


def in_accessibility(graph, weighted=True, h=3):
    """
    In-accessibility shows the average number of nodes from which
    a given node can be reached in exactly h steps.

    :param graph: NetworkX graph
    :param weighted:
        If True than probabilities p_ij will be computed
        as fraction of sum of in-weights of level h and
        weight of edges connecting i ad j or neighbors of i and j.
    :param h: number of steps
    :return: Values of in-accessibility for each node
    :rtype: dictionary where keys are as follows - n_h_j, where
        n represents node name, and j is current number of steps.


    .. seealso::
        :py:func:`accessibility`, :py:func:`out_accessibility`

    References:
        ..[1] Viana, Matheus P., et al. "Accessibility in networks:
        A useful measure for understanding social insect nest architecture."
        Chaos, Solitons & Fractals 46 (2013): 38-45.
    """
    if not graph.is_directed():
        raise nx.NetworkXError(
            "in_accessibility() not defined for undirected graphs.")

    accessibility_dict = {}
    for node in graph.nodes_iter():
        i = 1; neighbors = {}
        successors = graph.in_edges(node)
        neighbors[i] = successors
        _neighbors_in(graph, successors, neighbors, h-1, i+1)
        for j in range(1, h+1):
            if weighted:
                weights = sum([int(graph.get_edge_data(u, v).get('weight'))
                               for u, v in neighbors[j]])
            else:
                weights = len(neighbors[j])
            acc = 0
            tmp1 = [x[0] for x in neighbors[j]]
            tmp2 = [x[1] for x in neighbors[j]]

            for n in set(tmp1):
                weight = 0; degree = 0
                for s in set(tmp2):
                    if weighted:
                        if graph.has_edge(n,s):
                            weight += float(graph.get_edge_data(n,s).get('weight'))
                    else:
                        if graph.has_edge(n,s):
                            degree += 1.
                if weighted:
                    p_ij = weight/weights
                else:
                    p_ij = degree/weights
                try:
                    log_p_ij = math.log(p_ij)
                    acc += -1 * (p_ij * math.log(p_ij))
                except ValueError:
                    continue

            accessibility_dict[str(node) + '_h_' + str(j)] = math.exp(acc)

    return accessibility_dict


def out_accessibility(graph, weighted=True, h=3):
    """
    Out-accessibility shows the average number of nodes that can
    be reached in exactly h steps from the given node.
    :param graph: NetworkX graph
    :param weighted:
        If True than probabilities p_ij will be computed
        as fraction of sum of out-weights of level h and
        weight of edges connecting i and j or neighbors of i and j.
    :param h: number of steps
    :return: Values of accessibility for each node
    :rtype: dictionary where keys are as follows - n_h_j, where
        n represents node name, and j is current number of steps.


    .. seealso::
        :py:func:`accessibility`, :py:func:`in_accessibility`

    References:
        ..[1] Viana, Matheus P., et al. "Accessibility in networks:
        A useful measure for understanding social insect nest architecture."
        Chaos, Solitons & Fractals 46 (2013): 38-45.
    """
    if not graph.is_directed():
        raise nx.NetworkXError(
            "in_accessibility() not defined for undirected graphs.")

    accessibility_dict = {}
    for node in graph.nodes_iter():
        i = 1; neighbors = {}
        successors = graph.out_edges(node)
        neighbors[i] = successors
        _neighbors_out(graph, successors, neighbors, h-1, i+1)
        for j in range(1, h+1):
            if weighted:
                weights = sum([int(graph.get_edge_data(u, v).get('weight'))
                               for u, v in neighbors[j]])
            else:
                weights = len(neighbors[j])
            acc = 0
            tmp1 = [x[0] for x in neighbors[j]]
            tmp2 = [x[1] for x in neighbors[j]]

            for n in set(tmp2):
                weight = 0; degree = 0
                for s in set(tmp1):
                    if weighted:
                        if graph.has_edge(s,n):
                            weight += float(graph.get_edge_data(s,n).get('weight'))
                    else:
                        if graph.has_edge(s,n):
                            degree += 1.
                if weighted:
                    p_ij = weight/weights
                else:
                    p_ij = degree/weights
                try:
                    log_p_ij = math.log(p_ij)
                    acc += -1 * (p_ij * math.log(p_ij))
                except ValueError:
                    continue

            accessibility_dict[str(node) + '_h_' + str(j)] = math.exp(acc)

    return accessibility_dict


###############################################################################
#                           HELPER FUNCTIONS
###############################################################################


def _neighbors(graph, neighbors, neighbour_dict, num_levels, i):
    if num_levels == 0:
        return neighbour_dict
    else:
        tmp = []
        for n, s in neighbors:
            succ = graph.edges(s)
            if len(succ) > 0:
                tmp.append(succ)
        tmp = [val for sublist in tmp for val in sublist]
        neighbour_dict[i] = list(set(tmp))
        _neighbors(graph, tmp, neighbour_dict, num_levels-1, i+1)


def _neighbors_out(graph, neighbors, neighbour_dict, num_levels, i):
    if num_levels == 0:
        return neighbour_dict
    else:
        tmp = []
        for n, s in neighbors:
            succ = graph.out_edges(s)
            if len(succ) > 0:
                tmp.append(succ)
        tmp = [val for sublist in tmp for val in sublist]
        neighbour_dict[i] = set(tmp)
        _neighbors_out(graph, tmp, neighbour_dict, num_levels-1, i+1)


def _neighbors_in(graph, neighbors, neighbour_dict, num_levels, i):
    if num_levels == 0:
        return neighbour_dict
    else:
        tmp = []
        for n, p in neighbors:
            pred = graph.in_edges(n)
            if len(pred) > 0:
                tmp.append(pred)
        tmp = [val for sublist in tmp for val in sublist]
        neighbour_dict[i] = set(tmp)
        _neighbors_in(graph, tmp, neighbour_dict, num_levels-1, i+1)
