#!/usr/bin/python
# -*- coding: utf-8 -*-


class UnionFind(object):
    def __init__(self, size):
        # at beginning, every element point to its self
        self.parent = [i for i in range(size)]

    def find(self, p):
        """
        find root of an element
        :param p:
        :return:
        """
        # continue find parent element until find root
        while p != self.parent[p]:
            p = self.parent[p]
        return p

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
            return

        # point p's parent to q's parent
        self.parent[p_root] = q_root


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






