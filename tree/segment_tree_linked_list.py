#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
segment tree implement with linked list
"""


class TreeNode(object):
    """
    segment tree node
    """
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.val = None
        self.left = None
        self.right = None


class SegmentTree(object):
    """
    segment tree
    """
    def __init__(self, data):
        self.data = data
        self.root = self.build_tree(0, len(self.data) - 1)

    def build_tree(self, l, r):
        if l > r:
            return

        root = TreeNode(l, r)
        mid = l + (r - l) // 2
        if l == r:
            # range size is 1, search node value in origin data
            root.val = self.data[l]  # or self.data[end]
        else:
            # build left sub tree
            root.left = self.build_tree(l, mid)
            # build right sub tree
            root.right = self.build_tree(mid+1, r)
            # update val of current node after left and right tree is built
            root.val = root.left.val + root.right.val

        return root

    def query(self, l, r):
        # todo: boundary chk
        return self._query(self.root, l, r)

    def _query(self, node, l, r):
        if l > r:
            return

        if node.l == l and node.r == r:
            # range meet, it is the node to find
            return node.val
        # todo: Attention: calculate mid of range this node stands for
        mid = node.l + (node.r - node.l) // 2
        # compare node range mid with query boundary
        if l >= mid+1:
            # query range is at right sub tree
            return self._query(node.right, l, r)
        elif r <= mid:
            # query range is at left sub tree
            return self._query(node.left, l, r)

        # query range spread in both left and right sub tree
        left_res = self._query(node.left, l, mid)
        right_res = self._query(node.right, mid+1, r)

        return left_res + right_res

    def update(self, arr_index, value):
        # todo: boundary chk
        self.data[arr_index] = value
        self._update(self.root, 0, len(self.data)-1, arr_index, value)

    def _update(self, node, l, r, arr_index, value):
        if node is None:
            return

        if l == r:
            node.val = value
            return

        # mid of node range
        mid = node.l + (node.r - node.l) // 2

        # arr_index is a point, it is either in left or right
        # it is different with query situation which query range many spread
        # in both left and right sub tree
        if arr_index >= mid + 1:
            self._update(node.right, mid+1, r, arr_index, value)
        else:  # arr_index <= mid:
            self._update(node.left, l, mid, arr_index, value)

        node.val = node.left.val + node.right.val


if __name__ == "__main__":
    test_nums = [-2, 0, 3, -5, 2, -1]
    segment_tree = SegmentTree(test_nums)

    print(segment_tree.query(0, len(test_nums) - 1))
    for i in range(len(test_nums)):
        segment_tree.update(i, i)
        print(segment_tree.query(0, len(test_nums) - 1), sum(test_nums))







