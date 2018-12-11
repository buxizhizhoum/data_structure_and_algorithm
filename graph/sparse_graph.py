#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
implement graph with adjacent list

it is better to implement graph with adjacent list when the graph is sparse
"""
from __future__ import print_function


class SparseGraph(object):
    def __init__(self, n, directed=False):
        self.n = n
        self.m = 0
        self.directed = directed
        self.graph = [[] for _ in range(self.n)]

    def add_edge(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            self.graph[i].append(j)
            # if not direct graph
            # todo: attention, it is possible to add two edges between 2 point
            # this is a difference between graph implemented
            # with adjacent list and adjacent matrix
            # i != j prevent add edge between a node and itself.
            if i != j and not self.directed:
                self.graph[j].append(i)
            self.m += 1
        else:
            raise ValueError("input is illegal")

    def has_edge(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            if j in self.graph[i]:
                return True
        return False

    def vertex_count(self):
        return self.n

    def edge_count(self):
        return self.m

    def show(self):
        for index, sub_list in enumerate(self.graph):
            print("{}: {}".format(index, sub_list), end="\n", sep=" ")


if __name__ == "__main__":
    import random

    graph = SparseGraph(10)

    for _ in range(10):
        i = random.randrange(0, 10)
        j = random.randrange(0, 10)

        graph.add_edge(i, j)

    graph.show()



