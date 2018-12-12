#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
graph implement with adjacent matrix

it is better to implement graph with adjacent matrix when the graph is dense
"""
from __future__ import print_function


class DenseGraph(object):
    def __init__(self, n, directed=False):
        self.n = n  # vertex number
        self.m = 0  # edge number
        self.directed = directed
        self.graph = [[0 for i in range(n)] for j in range(n)]

    def add_edge(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            if self.has_edge(i, j):
                # if there is already edge, return
                return
            # add edge only when there is no edge
            self.graph[i][j] = 1
            if self.directed is False:
                self.graph[j][i] = 1
            self.m += 1  # update edge number
        else:
            raise ValueError("The given two nodes is illegal")

    def has_edge(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            return self.graph[i][j]
        raise ValueError("The given two nodes is illegal")

    def edge_count(self):
        return self.m

    def vertex_count(self):
        return self.n

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.graph[i][j], end=" ")
            print("\n")


if __name__ == "__main__":
    import random

    graph = DenseGraph(10)
    for _ in range(10):
        i = random.randrange(0, 10)
        j = random.randrange(0, 10)

        graph.add_edge(i, j)

    graph.show()












