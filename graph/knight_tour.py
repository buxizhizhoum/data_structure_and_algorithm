#!/usr/bin/python
# -*- coding: utf-8 -*-


from graph import Graph
from graph import Vertex


class KnightTour(object):
    def __init__(self, bd_size):
        self.bd_size = bd_size

    def knight_graph(self):
        """
        generate knight tour graph
        :return:
        """
        k_graph = Graph()

        for row in range(self.bd_size):
            for col in range(self.bd_size):
                node_id = self.pos_to_node_id(row, col)
                # get possible move point of current point
                new_positions = self.get_legal_moves(row, col)
                for position in new_positions:
                    # transfer point to node id
                    new_id = self.pos_to_node_id(position[0], position[1])
                    k_graph.add_edge(node_id, new_id)

        # self.print_graph(k_graph)

        return k_graph

    def pos_to_node_id(self, row, col):
        """
        transfer row, col and board_size to node id in int.
        :param row:
        :param col:
        :return:
        """
        res = row * self.bd_size + col
        return res

    def get_legal_moves(self, x, y):
        """
        search the possible moves of certain point
        :param x:
        :param y:
        :return:
        """
        new_moves = []
        moves_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                         (1, -2), (1, 2), (2, -1), (2, 1)]
        for move in moves_offsets:
            tmp_x = x + move[0]
            tmp_y = y + move[1]
            if self.legal_coord(tmp_x, tmp_y):
                new_moves.append((tmp_x, tmp_y))

        return new_moves

    def legal_coord(self, x, y):
        """
        check whether the new point is in board
        :param x:
        :param y:
        :return:
        """
        if 0 <= x < self.bd_size and 0 <= y < self.bd_size:
            return True
        else:
            return False

    def print_graph(self, graph):
        for k in graph.get_vertices():
            v = graph.get_vertex(k)
            for w in v.get_connected_to():
                # print w, v
                print w.get_id(), v.get_id()

    def knight_tour(self, n, path, current_vertex, limit):
        """
        dfs, to find the route that contains 63 edge.
        :param n: depth of current search
        :param path: the list of vertexes that have been searched
        :param current_vertex: the vertex to search this time
        :param limit: num of vertexes of route
        :return:
        """
        current_vertex.set_color("gray")
        path.append(current_vertex)
        if n < limit:
            # nbr_list = list(current_vertex.get_connected_to())
            nbr_list = self.order_by_available(current_vertex)
            i = 0
            done = False
            while i < len(nbr_list) and done is False:
                # the vertex should appear only once.
                if nbr_list[i].get_color() == "white":
                    # deep first
                    done = self.knight_tour(n+1, path, nbr_list[i], limit)
                    i += 1
            # trace back
            if done is False:
                path.pop()
                current_vertex.set_color("white")
        else:
            done = True
            print path

        return done

    def order_by_available(self, vertex):
        """
        optimize to let knight choose position at side on priority
        :param vertex:
        :return:
        """
        res_list = []
        for v in vertex.get_connected_to():
            c = 0
            for w in v.get_connected_to():
                if w.get_color() == "white":
                    c += 1
            res_list.append((c, v))
            res_list.sort(key=lambda x: x[0])
        res = [y[1] for y in res_list]
        return res


if __name__ == "__main__":
    kn_graph_obj = KnightTour(8)  # size 8 * 8
    graph = kn_graph_obj.knight_graph()
    print graph

    start = graph.vertex_dict[0]
    kn_graph_obj.knight_tour(0, [], start, 63)


