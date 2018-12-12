#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
edge used in weight graph
"""


class Edge(object):
    def __init__(self, a, b, weight):
        self.a = a  # node
        self.b = b  # node
        self.w = weight  # weight

    def weight(self):
        """
        return weight of current edge
        :return:
        """
        return self.w

    def a(self):
        """
        return one node of current edge
        :return:
        """
        return self.a

    def b(self):
        """
        return one node
        :return:
        """
        return self.b

    def other(self, node):
        """
        get the other node on the edge according to the known edge
        :return:
        """
        if node == self.a or node == self.b:
            if node == self.a:
                return self.b
            return self.a

    def __gt__(self, other):
        """
        operator overloading
        :param other:
        :return:
        """
        return self.w > other.w

    def __lt__(self, other):
        return self.w < other.w

    def __ge__(self, other):
        return self.w >= other.w

    def __le__(self, other):
        return self.w <= other.w

    def __eq__(self, other):
        return self.w == other.w


if __name__ == "__main__":
    edge = Edge(1, 2, 0.1)
    print(edge.a)



