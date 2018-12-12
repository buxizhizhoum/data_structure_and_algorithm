#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
bfs
"""
from Queue import Queue


class BFS(object):
    visited = {}

    def bfs(self, graph, cur):
        queue = Queue()
        queue.put(cur)
        self.visited[cur] = True

        while not queue.empty():
            node_id = queue.get()
            print(node_id)
            neighbors = graph.graph[node_id]

            # this is because the neighbors stores edge obj which contains
            # node info it is implemented in this way is due to the wish
            # to have same interface no matter in graph implemented in
            # adjacent matrix and adjacent list
            for edge in neighbors:
                node_id = edge.node_to()  # get the node id from edge obj

                if not self.visited.get(node_id):
                    queue.put(node_id)
                    # todo: visited status should be updated after node is put into queue
                    self.visited[node_id] = True


if __name__ == "__main__":
    from read_graph import read_graph

    filename = "/home/buxizhizhoum/1-Work/2-Codes/algorithm/graph/weighted_graph/test_graph.txt"

    graph = read_graph(filename)

    BFS().bfs(graph, 0)





