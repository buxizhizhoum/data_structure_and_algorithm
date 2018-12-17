#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
lazy prim to generate MST

always process the edge with minimum weight until there is no edge to process
or no nodes to process

priority queue is used to get minimum edge from all edges to process.
"""
from Queue import PriorityQueue


class LazyPrim(object):
    def __init__(self, graph):
        self.graph = graph
        # mst: edges list of MST [(node_from, node_to, node_w), ...]
        self.mst = []  # list of edges in MST
        self.mst_weight = None

    def lazy_prim(self):
        """
        lazy prim to find MST, bfs based, but always minimum weight edge
        bfs + dfs?
        :return:
        """
        pq = PriorityQueue()
        processed = {}  # whether a node is processed or not

        start = 0  # node id of start
        # initialize priority queue,
        # put all edges connected with start node to priority queue
        neighbors = self.graph.graph[start]
        for edge in neighbors:
            # extract node info from edge
            node_from, node_to, node_w = edge.node_from(), edge.node_to(), edge.weight()
            # what to process is edge, so put edge info to queue
            pq.put((node_w, node_from, node_to))

        processed[start] = True

        while not pq.empty():
            cur_node_w, cur_node_from, cur_node_to = pq.get()
            """
            main logic is at here
            for an edge from priority queue(min heap based), 
            if the other node is not processed yet, it is an edge in MST
            
            always check the edge with minimum edge of all processed nodes,
            this is why priority queue is used
            """
            # if the other node is processed, continue
            if processed.get(cur_node_to) is True:
                continue
            # if the other node is not processed, append edge info into pq
            self.mst.append((cur_node_from, cur_node_to, cur_node_w))

            # process edges that connected to cur node
            neighbors = self.graph.graph[cur_node_to]
            for edge in neighbors:
                # extract node info from edge
                node_from, node_to, node_w = edge.node_from(), edge.node_to(), edge.weight()

                if not processed.get(node_to):
                    pq.put((node_w, node_from, node_to))

            processed[cur_node_to] = True

        self.mst_weight = self._calc_weight()

    def lazy_prim_simplified(self):
        """
        wrap a method visit() to make it more compact
        :param graph:
        :return:
        """
        processed = {}
        mst = []
        pq = PriorityQueue()
        # start from 0
        pq = self.visit(0, pq, processed)

        while not pq.empty():
            cur_node_w, cur_node_from, cur_node_to = pq.get()
            # if processed, do nothing
            if processed.get(cur_node_to) is True:
                continue
            # if not processed yet, it is one edge in MST
            self.mst.append((cur_node_from, cur_node_to, cur_node_w))
            # visit the other node in current minimum weight edge
            pq = self.visit(cur_node_to, pq, processed)

        self.mst_weight = self._calc_weight()

    def visit(self, node, pq, processed):
        """
        visit a node and put all edges that connected to this edge
        and not be processed yet to pq
        :param graph:
        :param node: id of node to visit
        :param pq:
        :param processed:
        :return:
        """
        # get all edges that connected to node
        conn_edges = self.graph.graph[node]
        for edge in conn_edges:
            node_from, node_to, node_w = edge.node_from(), edge.node_to(), edge.weight()

            # if the other node of this edge is not processed
            if not processed.get(node_to):
                # what to process is edge, so put edge info to queue
                pq.put((node_w, node_from, node_to))

        processed[node] = True

        return pq

    def _calc_weight(self):
        """
        get weight of mst
        mst: edges list of MST [(node_from, node_to, node_w), ...]
        :return:
        """
        if not self.mst:
            return None
        res = sum([item[2] for item in self.mst])

        return res


if __name__ == "__main__":
    from read_graph import read_graph

    filename = "/home/buxizhizhoum/1-Work/2-Codes/algorithm/graph/weighted_graph/test_graph.txt"

    graph = read_graph(filename)

    lazy_prim = LazyPrim(graph)

    # lazy_prim.lazy_prim()
    # print(lazy_prim.mst)
    # print(lazy_prim.mst_weight)

    lazy_prim.lazy_prim_simplified()

    print(lazy_prim.mst)
    print(lazy_prim.mst_weight)





