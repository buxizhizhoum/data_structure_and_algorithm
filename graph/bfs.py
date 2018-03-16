#!/usr/bin/python
# -*- coding: utf-8 -*-

from queue import Queue
from graph import Vertex
from word_ledder import build_graph


def bfs(graph, start):
    start.set_distance(0)
    start.set_predecessor(0)
    # the queue will decide the next vertex to explore
    vertex_queue = Queue()
    vertex_queue.put(start)
    while vertex_queue.qsize() > 0:
        current_vertex = vertex_queue.get()  # get the point to search
        # search all the vertex that is connected to the point
        for nbr in current_vertex.get_connected_to():
            # color == white or color != black
            if nbr.get_color() == "white":
                # when founded, set to gray
                nbr.set_color("gray")
                nbr.set_distance(current_vertex.get_distance() + 1)
                nbr.set_predecessor(current_vertex)
                vertex_queue.put(nbr)
        # all the connected vertex is searched, set it to black
        current_vertex.set_color("black")
        print current_vertex


def traverse(y):
    x = y
    while x.get_predecessor():
        print x.get_id()
        x = x.get_predecessor()
    print x.get_predecessor()


if __name__ == "__main__":
    # create graph
    word_file = "./word_file.txt"
    graph = build_graph(word_file)
    print graph

    for k in graph.get_vertices():
        v = graph.get_vertex(k)
        for w in v.get_connected_to():
            print w, v
            # print w.get_id(), v.get_id()

    # bfs
    vertexes = graph.get_vertices()
    start_vertex = graph.get_vertex(vertexes[0])

    bfs(graph, start_vertex)

    # for k in graph.get_vertices():
    #     v = graph.get_vertex(k)
    #     for w in v.get_connected_to():
    #         print w, v
    #         # print w.get_id(), v.get_id()

    traverse(graph.get_vertex("POLL"))
