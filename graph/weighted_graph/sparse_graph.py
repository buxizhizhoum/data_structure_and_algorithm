#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
implement graph with adjacent list

it is better to implement graph with adjacent list when the graph is sparse
"""
from __future__ import print_function
from edge import Edge


class SparseGraph(object):
    def __init__(self, n, directed=False):
        self.n = n  # node count
        self.m = 0  # edge count
        self.directed = directed  # whether it is a directed graph
        # initialize graph to a 2D list
        self.graph = [[] for _ in range(self.n)]

    def add_edge(self, i, j, w):
        """
        add edge between node i and node j with weight w
        :param i:
        :param j:
        :param w: weight
        :return:
        """
        if 0 <= i < self.n and 0 <= j < self.n:
            self.graph[i].append(Edge(i, j, w))
            # if not direct graph
            # todo: attention, it is possible to add two edges between 2 point
            # this is a difference between graph implemented
            # with adjacent list and adjacent matrix
            # i != j prevent add edge between a node and itself.
            if i != j and not self.directed:
                self.graph[j].append(Edge(j, i, w))
            self.m += 1
        else:
            raise ValueError("input is illegal")

    def has_edge(self, i, j):
        """
        chk if there is edge between node i and node j, regardless of weight
        :param i:
        :param j:
        :return:
        """
        if 0 <= i < self.n and 0 <= j < self.n:
            for edge in self.graph[i]:
                # if the other node is j, means there is edge
                if edge.other() == j:
                    return True
        return False

    def vertex_count(self):
        """
        vertex count
        :return:
        """
        return self.n

    def edge_count(self):
        """
        return edge numbers
        :return:
        """
        return self.m

    def show(self):
        for index, edge_list in enumerate(self.graph):

            print("{}->".format(index), end=" ")
            for edge in edge_list:
                print("{}:{:.4f}".format(edge.node_to(), edge.weight()), end=", ")
            print("\n")


if __name__ == "__main__":
    import random

    graph = SparseGraph(10)

    for _ in range(10):
        # random.seed()
        i = random.randrange(0, 10)
        j = random.randrange(0, 10)
        w = random.random()

        graph.add_edge(i, j, w)

    graph.show()



