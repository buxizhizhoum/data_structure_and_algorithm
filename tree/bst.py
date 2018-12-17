#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
binary search tree implementation.
"""
from Queue import Queue


class Node(object):
    def __init__(self, key, value):
        self.key = key  # this is different, it could be removed if key==value
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.size = 0  # todo: size is not maintained yet
        self.root = None  # an empty tree

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def _insert(self, node, key, value):
        """
        insert (key, value) into a node recursively
        :param node: node to insert key, value
        :param key: key to insert
        :param value: value to insert
        :return:
        """
        if node is None:
            self.size += 1
            # if node is None, new a node and return it
            # the recursion that call this function will receive this return
            # node and assign it to its left or right node.
            return Node(key, value)

        if node.key == key:
            node.value = value
            return node

        if key < node.key:
            # todo: learn this return thought
            # if key < node.key, insert into left tree of current node
            node.left = self._insert(node.left, key, value)
        else:
            # if key > node.key, insert into right tree of current node
            node.right = self._insert(node.right, key, value)

        # todo: attention return here, compare keys_and_rooms' return
        # todo: does this return necessary?
        return node

    def _insert_1(self, node, key, value):
        """
        another recursion thought, if node is leaf version
        :param node:
        :param key:
        :param value:
        :return:
        """
        if node is None:
            # return Node(key, value)
            self.root = Node(key, value)
            return
        # todo: compare return
        # in this method, modification is linked, no need to return
        # when a node is leaf, judge whether to update or insert to left or right
        if node.left is None and node.right is None:
            if node.key == key:
                node.value = value
                return

            if key < node.key:
                node.left = Node(key, value)
            else:
                node.right = Node(key, value)
            return
            # return node

        if node.key == key:
            node.value = value
            return

        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
                return
            self._insert_1(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key, value)
                return
            self._insert_1(node.right, key, value)

        # return node

    def _insert_2(self, node, key, value):
        """
        loop version
        insert a node(key, value) into a tree.
        :param node: the node stands for the tree to insert
        :param key:
        :param value:
        :return:
        """
        # if the tree is empty at beginning
        if node is None:
            node = Node(key, value)
            self.root = node
            return

        cur = node
        while cur is not None:
            if key == cur.key:
                # update value
                cur.value = value
                break

            if key < cur.key:
                if cur.left is None:
                    # if left is None, insert at left of cur node
                    cur.left = Node(key, value)
                    break
                # if left is not None, update pointer
                cur = cur.left
            else:
                if cur.right is None:
                    # if right is None, insert at right of cur node
                    cur.right = Node(key, value)
                    break
                # update pointer
                cur = cur.right

    def insert(self, key, value):
        """
        public insert function, insert (key, value) into BST
        :param key:
        :param value:
        :return:
        """
        self.root = self._insert(self.root, key, value)
        # self._insert_1(self.root, key, value)
        # self._insert_2(self.root, key, value)

    def _contain(self, node, key):
        """
        check whether key is exist in a bst whose root is node
        :param node:
        :param key:
        :return:
        """
        if node is None:
            return False

        if node.key == key:
            return True
        elif key < node.key:
            # check in left tree
            # todo: Attention return
            # in this problem, when the result is founded, return immediately
            return self._contain(node.left, key)
        else:
            # check in right tree
            return self._contain(node.right, key)

    def contain(self, key):
        """
        check whether a key is exist in bst
        :param key:
        :return:
        """
        return self._contain(self.root, key)

    def _search(self, node, key):
        """
        search value of key in bst whose root is node
        return None if not exist.
        :param node: search root of bst
        :param key: key to search
        :return:
        """
        if node is None:
            # if not exist, return None
            return None

        if node.key == key:
            return node.value
        elif key < node.key:
            # todo: attention return
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def search(self, key):
        """
        search value of key in bst
        :param key:
        :return: value of key if exist, None if not exist
        """
        return self._search(self.root, key)

    def _pre_order(self, node):
        if node is None:
            return

        print(node.value)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def pre_order(self):
        """
        pre order traverse
        :return:
        """
        self._pre_order(self.root)

    def _in_order(self, node):
        if node is None:
            return

        self._in_order(node.left)
        print(node.value)
        self._in_order(node.right)

    def in_order(self):
        """
        in order traverse
        :return:
        """
        self._in_order(self.root)

    def _post_order(self, node):
        if node is None:
            return

        self._post_order(node.left)
        self._post_order(node.right)
        print(node.value)

    def post_order(self):
        """
        post order traverse
        :return:
        """
        self._post_order(self.root)

    def _destroy(self, node):
        """
        post pre order traverse to destroy a tree
        :param node:
        :return:
        """
        if node is None:
            return

        self._destroy(node.left)
        self._destroy(node.right)
        del node

    def destroy(self):
        """
        destroy a tree
        :return:
        """
        self._destroy(self.root)

    def _level_order(self, node):
        if node is None:
            return

        queue = Queue()
        queue.put(node)

        while not queue.empty():
            cur = queue.get()
            print(cur.value)

            if cur.left is not None:
                queue.put(cur.left)
            if cur.right is not None:
                queue.put(cur.right)

    def level_order(self):
        """
        level order traverse
        :return:
        """
        self._level_order(self.root)

    def _minimum(self, node):
        if node is None:
            return

        # if it is already the leftest node, it is minimum, return its value
        if node.left is None:
            return node.value

        return self._minimum(node.left)

    def minimum(self):
        """
        get minimum node in a binary search tree
        :return:
        """
        return self._minimum(self.root)

    def _maximum(self, node):
        if node is None:
            return

        # if it is already the rightest node, return its value
        if node.right is None:
            return node.value

        return self._maximum(node.right)

    def maximum(self):
        """
        get maximum node of a BST
        :return:
        """
        return self._maximum(self.root)

    def _remove_min(self, node):
        if node is None:
            return

        if node.left is None:
            # if node.right is None:
            #     return None
            # else:
            #     return node.right
            # no matter whether node.right is None or not, node.right works
            return node.right
        # todo: attention this recursion
        # minimum node has no left tree, if min node has a right tree,
        # its parent's left should point to to minimum node's right tree
        # usually it should stop recursion at the parent node of minimum node
        # and point right to minimum node's right tree
        # however, this recursion skillfully assign value of recursion to node.left
        # and when it encounter minimum node, just return its right node
        node.left = self._remove_min(node.left)
        return node

    def remove_min(self):
        self.root = self._remove_min(self.root)

    def _remove_max(self, node):
        """
        remove max node of BST whose root is node
        :param node:
        :return:
        """
        if node is None:
            return

        if node.right is None:
            return node.left

        node.right = self._remove_max(node.right)
        return node

    def remove_max(self):
        """
        remove max node of whole BST
        :return:
        """
        self.root = self._remove_max(self.root)

    def _remove(self, node, key):
        """
        delete a node in BST whose root is node
        :param node:
        :param key:
        :return:
        """
        if node is None:
            return

        if node.key == key:
            # find the key, delete
            if node.left is None and node.right is None:
                return None
            # if only have one sub tree, return the only sub tree
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # both of left and right is not None
            else:
                # find minimum in node.right
                # replace node with minimum in node.right
                # delete minimum node in node.right
                # node = (del(node.right, min))

                node.value = self._minimum(node.right)
                node.right = self._remove_min(node.right)
                return node

        if key < node.key:
            node.left = self._remove(node.left, key)
        else:
            node.right = self._remove(node.right, key)

        return node

    def remove(self, key):
        """
        remove a node whose root is self.root
        :param key:
        :return:
        """
        self.root = self._remove(self.root, key)

    def successor(self, node):
        """
        the successor node value
        :param node:
        :return:
        """
        if node.right is not None:
            return self._minimum(node.right)
        return None

    def predecessor(self, node):
        """
        the predecessor node value
        :param node:
        :return:
        """
        if node.left is not None:
            return self._maximum(node.left)
        return None


if __name__ == "__main__":
    import random
    random.seed(666)

    bst = BST()

    test_data = [random.randrange(1, 100) for _ in range(10)]
    for item in test_data:
        bst.insert(item, item)

    print(bst.root)

    print(bst.search(test_data[0]))
    print(bst.contain(100))

    bst.in_order()

    print("minimum:", bst.minimum())
    print("maximum:", bst.maximum())

    bst.remove(46)
    print("--"*100)
    bst.in_order()



