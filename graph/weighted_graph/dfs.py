#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
dfs
"""


class DFS(object):
    """
    depth first search
    """
    visited = {}

    def dfs(self, graph, cur):
        """
        recursion, depth first search
        :param graph: the graph obj to search
        :param cur: current node
        :return:
        """
        # get nodes that connected to current node
        neighbors = graph.graph[cur]

        print(cur)

        # mark current node as visited
        self.visited[cur] = True
        # search on nodes that is connected to current node
        for edge in neighbors:
            # edge.node_to() is node id that self.graph[start] connected to
            if edge.node_to() not in self.visited:
                self.dfs(graph, edge.node_to())


if __name__ == "__main__":
    from read_graph import read_graph

    filename = "/home/buxizhizhoum/1-Work/2-Codes/algorithm/graph/weighted_graph/test_graph.txt"

    graph = read_graph(filename)

    DFS().dfs(graph, 0)



