#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
refer java code of "Play With Algorithm" on imooc

only implement sum
"""


class SegmentTree(object):
    def __init__(self, data):
        self.data = data
        self.tree = [None for _ in range(4*len(self.data))]
        self.build(0, 0, len(self.data) - 1)

    def build(self, index, l, r):
        """
        build segment tree at index from top to bottom,
        the tree whose root is index stands for range [l, r]
        :param index: where to start
        :param l:
        :param r:
        :return:
        """
        if l == r:
            self.tree[index] = self.data[l]  # so is self.data[r]
            return

        left_index = self.left_index(index)
        right_index = self.right_index(index)

        # todo: think about boundary condition
        mid = l + (r - l) // 2
        self.build(left_index, l, mid)
        self.build(right_index, mid+1, r)

        # todo: if to extends function of segment tree, modify here
        self.tree[index] = self.tree[left_index] + self.tree[right_index]

    def left_index(self, index):
        """
        get left index of a node in segment tree which is described with array
        :param index: the node of segment tree to get left child node index
        :return:
        """
        return 2 * index + 1

    def right_index(self, index):
        """
        get right index of a node in segment tree which is described with array
        :param index: the node of segment tree to get right child node index
        :return:
        """
        return 2 * index + 2

    def query(self, query_l, query_r):
        if query_l < 0 or query_l >= len(self.data) \
                or query_r < 0 or query_r >= len(self.data) \
                or query_l > query_r:
            raise IndexError("Illegal index range")
        return self._query(0, 0, len(self.data)-1, query_l, query_r)

    def _query(self, index, l, r, query_l, query_r):
        """
        query in segment tree whose root is index range is [l, r],
        query value of range [query_l, query_r]
        :param index:
        :param l:
        :param r:
        :param query_l:
        :param query_r:
        :return:
        """
        if l == query_l and r == query_r:
            # if the query range is perfectly meet node range in segment tree
            return self.tree[index]

        # split segment tree whose node is index to two part
        # [l, mid] and [mid + 1, r]
        mid = l + (r - l) // 2
        left_index = self.left_index(index)
        right_index = self.right_index(index)

        if query_l >= mid + 1:
            # find only in right child tree
            return self._query(right_index, mid+1, r, query_l, query_r)
        elif query_r <= mid:
            # find only in left child tree
            return self._query(left_index, l, mid, query_l, query_r)

        # find result in left child tree and right child tree separately
        left_res = self._query(left_index, l, mid, query_l, mid)
        right_res = self._query(right_index, mid+1, r, mid+1, query_r)

        # merge result of left child tree and right child tree
        # todo: extend function of segment tree
        return left_res + right_res

    def update(self, index, value):
        if index < 0 or index >= len(self.data):
            raise IndexError("Illegal index parameter")
        self.data[index] = value
        self._update(0, 0, len(self.data)-1, index, value)

    def _update(self, tree_index, l, r, index, value):
        """
        update the value at index in segment tree whose root is tree_index
        :param tree_index:
        :param l:
        :param r:
        :param index:
        :param value:
        :return:
        """
        if l == r:
            self.tree[tree_index] = value
            return

        mid = l + (r - l) // 2
        left_index = self.left_index(tree_index)
        right_index = self.right_index(tree_index)

        if index >= mid + 1:
            self._update(right_index, mid+1, r, index, value)
        elif index <= mid:
            self._update(left_index, l, mid, index, value)

        # todo: extend tree function
        self.tree[tree_index] = self.tree[left_index] + self.tree[right_index]


if __name__ == "__main__":
    test_nums = [-2, 0, 3, -5, 2, -1]
    segment_tree = SegmentTree(test_nums)

    print(segment_tree.query(0, len(test_nums)-1))
    for i in range(len(test_nums)):
        segment_tree.update(i, i)
        print(segment_tree.query(0, len(test_nums)-1), sum(test_nums))




