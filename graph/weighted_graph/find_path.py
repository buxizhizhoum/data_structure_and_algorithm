#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
find path between 2 nodes in graph


            0-------------------6
            | \               | |
            | \             |   |
            |  7-----------2    |
            | / \\       / \    |
           / /  \ ---\  /  \    |
          / /   \     1    \    |
         / /    \   /   \   \  |
        / /     \  /      \ \ |
        4--------5-----------3
"""


class Path(object):
    def __init__(self, graph, start):
        self.graph = graph  # graph obj
        self.start = start  # start node

        self.visited = {}  # visited cache
        self.from_ = {}  # cache where the node is from

    def find_path(self):
        self.dfs(self.start)

    def dfs(self, node):
        self.visited[node] = True

        neighbors = self.graph.graph[node]
        # neighbors stores the edge obj that connected to node
        for edge in neighbors:
            # get node_id from edge
            node_id = edge.node_to()
            # node_id may not exist in self.visited
            if not self.visited.get(node_id):
                # store which node that new node is from
                self.from_[node_id] = node
                self.dfs(node_id)

    def has_path(self, end):
        """
        where there is a path from self.start to end
        :param end:
        :return:
        """
        # if there is flag in self.from_, it means that the node end is reached
        # from self.start, and there is a path between self.start and end
        if self.from_.get(end):
            return True
        return False

    def path(self, end):
        """
        extract the path from self.start to end node
        :param end: end node
        :return:
        """
        if not self.has_path(end):
            return None

        # traceback to find the path, until no node to traceback
        stack = []
        before = end
        while before is not None:
            stack.append(before)
            before = self.from_.get(before)

        # extract path from stack
        res = []
        while stack:
            res.append(stack.pop())

        return res

    def show_path(self, end):
        paths = self.path(end)
        if not paths:
            return

        for item in paths:
            print(item)


if __name__ == "__main__":
    from read_graph import read_graph

    filename = "/home/buxizhizhoum/1-Work/2-Codes/algorithm/graph/weighted_graph/test_graph.txt"

    graph = read_graph(filename)

    path_obj = Path(graph, start=0)
    path_obj.find_path()
    path_obj.show_path(end=3)


