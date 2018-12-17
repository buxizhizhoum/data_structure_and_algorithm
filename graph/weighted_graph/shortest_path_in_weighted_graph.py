#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
find shortest path in weighted graph
"""
from Queue import PriorityQueue


class ShortestPath(object):
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start

        self.from_ = {}
        # if id is integer, cost could be stored into a list
        self.cost = {node: float("inf") for node in range(len(self.graph.graph))}
        self.processed = {}

    def find_path(self):
        return self.bfs_dj(self.graph.graph, self.start)

    def bfs_dj(self, graph, start):
        """
        迪杰斯塔拉算法
        :param graph:
        :param start:
        :return:
        """
        queue = PriorityQueue()
        queue.put((0, start))
        self.cost[start] = 0

        while not queue.empty():
            # get the cheapest node from priority queue
            _, node = queue.get()
            
            neighbors = graph[node]  # get node list connected to node
            for edge in neighbors:
                _, node_id, node_w = edge.a, edge.b, edge.w
                # if not processed yet, update cost
                if not self.processed.get(node_id):
                    queue.put((self.cost[node] + node_w, node_id))
                    # update cost if cost is less
                    if self.cost[node] + node_w < self.cost[node_id]:
                        self.cost[node_id] = self.cost[node] + node_w
                        self.from_[node_id] = node

            # after update all its neighbors, mark node as processed
            self.processed[node] = True

        return self.cost


if __name__ == "__main__":
    from read_graph import read_graph

    filename = "/home/buxizhizhoum/1-Work/2-Codes/algorithm/graph/weighted_graph/test_graph.txt"

    graph = read_graph(filename)

    path_obj = ShortestPath(graph, start=0)
    print(path_obj.find_path())
    print(path_obj.from_)
    # path_obj.show_path(end=3)




