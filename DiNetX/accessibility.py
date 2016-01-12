#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import math


def accessibility(graph, weighted=True, h=3):
    """
    :param graph:
    :param weighted:
    :param h:
    :return:
    """
    if not graph.is_directed():
        raise nx.NetworkXError(
            "in_accessibility() not defined for undirected graphs.")

    accessibility_dict = {}
    for node in graph.nodes_iter():
        i = 1; neighbors = {}
        neigh = graph.edges(node)
        neighbors[i] = neigh
        _neighbors(graph, neigh, neighbors, h-1, i+1)

        for j in range(1, h+1):
            if weighted:
                weights = sum([int(graph.get_edge_data(u, v).get('weight'))
                               for u, v in neighbors[j]])
            else:
                weights = len(neighbors[j])
            acc = 0
            for u,v in neighbors[j]:
                if weighted:
                    weight = float(graph.get_edge_data(u, v).get('weight'))
                else:
                    weight = 1
                p_ij = weight/weights
                log_p_ij = math.log(p_ij)
                acc += -1 * (p_ij * math.log(p_ij))
                print acc
            accessibility_dict[str(node) + '_h_' + str(j)] = math.exp(acc)

    return accessibility_dict


def in_accessibility(graph, weighted=True, h=3):
    """

    :param graph:
    :param weighted:
    :param h:
    :return:
    """
    if not graph.is_directed():
        raise nx.NetworkXError(
            "in_accessibility() not defined for undirected graphs.")

    accessibility_dict = {}
    for node in graph.nodes_iter():
        i = 1; neighbors = {}
        successors = graph.out_edges(node)
        neighbors[i] = successors
        _neighbors_in(graph, successors, neighbors, h-1, i+1)

        for j in range(1, h+1):
            if weighted:
                out_weights = sum([int(graph.get_edge_data(u, v).get('weight'))
                                   for u, v in neighbors[j]])
            else:
                out_weights = len(neighbors[j])
            acc = 0
            for u,v in neighbors[j]:
                if weighted:
                    weight = float(graph.get_edge_data(u, v).get('weight'))
                else:
                    weight = 1
                p_ij = weight/out_weights
                log_p_ij = math.log(p_ij)
                acc += -1 * (p_ij * math.log(p_ij))
                print acc
            accessibility_dict[str(node) + '_h_' + str(j)] = math.exp(acc)

    return accessibility_dict


def out_accessibility(graph, weighted=True, h=3):
    """
    
    :param graph:
    :param weighted:
    :param h:
    :return:
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
                out_weights = sum([int(graph.get_edge_data(u, v).get('weight'))
                                   for u, v in neighbors[j]])
            else:
                out_weights = len(neighbors[j])
            acc = 0
            for u,v in neighbors[j]:
                if weighted:
                    weight = float(graph.get_edge_data(u, v).get('weight'))
                else:
                    weight = 1
                p_ij = weight/out_weights
                log_p_ij = math.log(p_ij)
                acc += -1 * (p_ij * math.log(p_ij))
                print acc
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
        neighbour_dict[i] = set(tmp)
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
            pred = graph.in_edges(p)
            if len(pred) > 0:
                tmp.append(pred)
        tmp = [val for sublist in tmp for val in sublist]
        neighbour_dict[i] = set(tmp)
        _neighbors_in(graph, tmp, neighbour_dict, num_levels-1, i+1)