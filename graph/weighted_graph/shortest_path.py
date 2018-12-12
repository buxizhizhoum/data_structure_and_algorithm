#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
find shortest path from start node to end node

breadth, a node, next level is the nodes connected to this node in one step ...
"""
from Queue import Queue


class ShortestPath(object):
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start

        self.visited = {}  # status, whether a node is visited
        self.from_ = {}  # cache where the node is from
        self.order = {}  # cache the visit order of a node {node_id: 1}

    def find_path(self):
        self.bfs(self.start)

    def bfs(self, node):
        """
        breadth first search
        :param node:
        :return:
        """
        queue = Queue()

        queue.put(node)
        self.visited[node] = True
        self.order[node] = 0

        while not queue.empty():
            # get a node from queue
            cur_node = queue.get()
            # get nodes that is connected to this node
            neighbors = self.graph.graph[cur_node]

            for edge in neighbors:
                node_id = edge.node_to()

                if self.visited.get(node_id) is None:
                    queue.put(node_id)
                    self.visited[node_id] = True
                    # cache the node that current node is from
                    self.from_[node_id] = cur_node
                    # cache the visit order of node
                    self.order[node_id] = self.order[cur_node] + 1

    def has_path(self, end):
        """
        where there is a path between self.start and end
        :param end:
        :return:
        """
        if self.from_.get(end) is not None:
            return True
        return False

    def path(self, end):
        """
        extract path from self.start to end
        :param end:
        :return:
        """
        if not self.has_path(end):
            return None

        stack = []
        cur = end
        while cur is not None:
            stack.append(cur)
            # get node before
            cur = self.from_.get(cur)

        res = []
        while stack:
            res.append(stack.pop())

        return res

    def show_path(self, end):
        path = self.path(end)

        print(path)


if __name__ == "__main__":
    from read_graph import read_graph

    filename = "/home/buxizhizhoum/1-Work/2-Codes/algorithm/graph/weighted_graph/test_graph.txt"

    graph = read_graph(filename)

    path_obj = ShortestPath(graph, start=0)
    path_obj.find_path()
    path_obj.show_path(end=3)






