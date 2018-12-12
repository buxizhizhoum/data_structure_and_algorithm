#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
read a graph from a file
"""
from sparse_graph import SparseGraph as Graph


def read_graph(fullname):
    with open(fullname, "r") as f:
        lines = f.readlines()

    n, m = lines[0].split()
    graph = Graph(int(n))
    for line in lines[1:]:
        node_from, node_to, weight = line.split()

        graph.add_edge(int(node_from), int(node_to), float(weight))

    graph.show()
    return graph


if __name__ == "__main__":
    filename = "/home/buxizhizhoum/1-Work/2-Codes/algorithm/graph/weighted_graph/test_graph.txt"
    read_graph(filename)


