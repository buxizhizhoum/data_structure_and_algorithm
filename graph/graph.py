#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
code mainly refer to Brad Miller,
Introduction to Data Structures and Algorithms in Python
this is just for learning, the copy right belong to Brad Miller.

create vertex, then add edge, and it becomes a graph.
"""
import sys


class Vertex(object):
    def __init__(self, key):
        """
        connected_to dict is used to trace the vertex it connected to.
        :param key:
        """
        self.id = key
        self.connected_to = {}
        self.color = "white"
        # in theory, dist should be infinite, practice it could be a large num
        self.distance = sys.maxsize
        self.predecessor = None
        self.discovery = 0
        self.finish = 0

    def add_neighbor(self, neighbor, wight):
        self.connected_to[neighbor] = wight

    def __str__(self):
        return "%s, %s connected to: %s, %s" \
               % (self.id, self.color, str([x.id for x in self.connected_to]), self.color)

    def get_connected_to(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

    def set_color(self, color):
        self.color = color

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def set_discovery(self, dtime):
        self.discovery =dtime

    def set_distance(self, distance):
        self.distance = distance

    def set_finish(self, ftime):
        self.finish = ftime

    def get_color(self):
        return self.color

    def get_predecessor(self):
        return self.predecessor

    def get_discovery(self):
        return self.discovery

    def get_distance(self):
        return self.distance

    def get_finish(self):
        return self.finish


class Graph(object):
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertex = 0

    def add_vertex(self, key):
        self.num_vertex += 1
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex

        return new_vertex

    def get_vertex(self, key):
        if key in self.vertex_dict:
            return self.vertex_dict[key]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertex_dict

    def add_edge(self, f, t, wight=0):
        """
        add vertex first, if it is not in graph vertex list, add it first, and
        then add neighbor
        :param f: vertex
        :param t: vertex
        :param wight: wight of edge
        :return:
        """
        if f not in self.vertex_dict:
            self.add_vertex(f)
        if t not in self.vertex_dict:
            self.add_vertex(t)
        self.vertex_dict[f].add_neighbor(self.vertex_dict[t], wight)

    def get_vertices(self):
        return self.vertex_dict.keys()

    def __iter__(self):
        return iter(self.vertex_dict.values())


if __name__ == "__main__":
    """
    create vertex, then add edge, and it becomes a graph.
    """
    g = Graph()
    for item in range(6):
        g.add_vertex(item)

    print(g.vertex_dict)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for k in g.get_vertices():
        v = g.get_vertex(k)
    # for v in g:  #  more graceful
        for w in v.get_connected_to():
            # print(("%s, %s") % (v.get_id(), w.get_id()))
            print v, w
