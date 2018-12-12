#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
graph implement with adjacent matrix

it is better to implement graph with adjacent matrix when the graph is dense
"""
from __future__ import print_function
from edge import Edge


class DenseGraph(object):
    def __init__(self, n, directed=False):
        self.n = n  # vertex number
        self.m = 0  # edge number
        self.directed = directed
        # when an edge is described by a obj, initialize it to None
        self.graph = [[None for i in range(n)] for j in range(n)]

    def add_edge(self, i, j, w):
        """
        add edge with weight to a graph
        :param i: node
        :param j: node
        :param w: weight
        :return:
        """
        if 0 <= i < self.n and 0 <= j < self.n:
            if self.has_edge(i, j):
                # if there is already edge, set it to None and decr m by 1
                # todo: be careful to maintain m when there is already a edge
                self.graph[i][j] = None
                if not self.directed:
                    self.graph[j][i] = None

                self.m -= 1
            # add edge
            self.graph[i][j] = Edge(i, j, w)
            if self.directed is False:
                self.graph[j][i] = Edge(j, i, w)
            self.m += 1  # update edge number
        else:
            raise ValueError("The given two nodes is illegal")

    def has_edge(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            return self.graph[i][j] is not None
        raise ValueError("The given two nodes is illegal")

    def edge_count(self):
        return self.m

    def vertex_count(self):
        return self.n

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                # show weight if edge
                if not self.graph[i][j]:
                    w = None
                else:
                    w = "{:.2}".format(self.graph[i][j].w)
                print(w, end=" ")
            print("\n")


if __name__ == "__main__":
    import random

    graph = DenseGraph(10)
    for _ in range(10):
        i = random.randrange(0, 10)
        j = random.randrange(0, 10)
        w = random.random()

        graph.add_edge(i, j, w)

    graph.show()












