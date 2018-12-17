#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
union find optimized with rank and path compress
"""


class UnionFind(object):
    def __init__(self, size):
        # at beginning, every element point to its self
        self.parent = [i for i in range(size)]
        # rank[i] means the height of tree which i is in
        self.rank = [1 for _ in range(size)]

    def find(self, p):
        """
        find root of an element
        :param p:
        :return:
        """
        # continue find parent element until find root
        # while p != self.parent[p]:
        #     p = self.parent[p]
        # return p

        # path compress version
        if p != self.parent[p]:
            # recursion to compress path
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def is_connected(self, p, q):
        """
        check whether two element is connected or not
        :param p:
        :param q:
        :return:
        """
        return self.find(p) == self.find(q)

    def union_(self, p, q):
        """
        union two element
        :param p:
        :param q:
        :return:
        """
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            # already connected, return
            return

        # point p's parent to q's parent
        if self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        elif self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        else:  # p_root = q_root
            self.parent[p_root] = q_root
            # maintain rank only when the two sub tree have the same length
            # p_root points to q_root,
            # the rank of tree whose root is p should increase by 1
            self.rank[p_root] += 1


if __name__ == "__main__":
    import random

    random.seed(666)

    test_size = 10
    union_find = UnionFind(test_size)
    for i in range(test_size//2):
        a = random.randrange(0, test_size)
        b = random.randrange(0, test_size)

        union_find.union_(a, b)
        print(a, b)
        print(union_find.parent)

    for i in range(test_size):
        a = random.randrange(0, test_size)
        b = random.randrange(0, test_size)

        union_find.is_connected(a, b)

    print(union_find.parent)






