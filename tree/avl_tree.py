#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
AVL tree implementation refer to imooc

height should be updated when insert, remove, rotate

after insert or remove node:
    1. update height
    2. maintain balance

there are 4 conditions that a node is not balanced
    1. LL  solve by right rotate
    2. RR           left rotate
    3. LR           left_rotate(node.left) right_rotate(node)
    4. RL           right_rotate(node.right) left_rotate(node)
"""
from Queue import Queue


class Node(object):
    def __init__(self, key, value):
        self.key = key  # this is different, it could be removed if key==value
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # the height of the Node


class BST(object):
    def __init__(self):
        self.root = None  # initialize an empty tree first
        self.size = 0  # todo: size is not maintained yet

    def tsize(self):
        """
        tree size
        :return:
        """
        return self.size

    def empty(self):
        return self.size == 0

    def _height(self, node):
        """
        get height of a node
        :param node:
        :return:
        """
        if node is None:
            return 0

        # return max(self._height(node.left), self._height(node.right)) + 1
        return node.height

    def _balance_factor(self, node):
        """
        get balance factor of a node

        the height difference between left node and right node
        :param node:
        :return:
        """
        if node is None:
            return 0

        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        """
        rotate a tree whose root is y towards right,
        and return the root of rotated tree

               y                                          x
              / \                                      /    \
             x   T4    rotate towards right (y)       z      y
            / \       - - - - - - - - - - - - - ->   / \    / \
           z   T3                                   T1  T2 T3 T4
          / \
        T1   T2
        :param y:
        :return:
        """
        # cache sub trees
        x = y.left
        t3 = x.right

        # rotate right
        x.right = y
        y.left = t3

        # update height
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1

        return x

    def _rotate_left(self, y):
        """
        rotate a tree whose root is y towards left,
        and return the root of rotated tree

           y                                        x
         /  \                                     /   \
        T1   x     rotate towards left (y)       y     z
            / \  - - - - - - - - - - - - - ->   / \   / \
          T2  z                                T1 T2 T3 T4
             / \
            T3 T4

        :param y:
        :return:
        """
        # cache sub trees
        x = y.right
        t2 = x.left

        # rotate left
        x.left = y
        y.right = t2

        # update height
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        # update x after y is updated
        x.height = max(self._height(x.left), self._height(x.right)) + 1

        return x

    def _insert(self, node, key, value):
        """
        insert (key, value) into a node recursively

        1. insert node
        2. update height
        3. maintain balance
            1. calculate balance factor
            2. rotate if necessary
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

        # update value, if key equals
        if key == node.key:
            node.value = value
            return node

        elif key < node.key:
            # todo: learn this return thought
            # insert into left tree of current node
            node.left = self._insert(node.left, key, value)
        else:  # key > node.key
            # insert into right tree of current node
            node.right = self._insert(node.right, key, value)

        node.height = max(self._height(node.left), self._height(node.right)) + 1

        return self._main_balance(node)

        # todo: attention return here, compare keys_and_rooms' return
        # todo: does this return necessary?
        # return node

    def insert(self, key, value):
        """
        public insert function, insert (key, value) into AVL tree
        :param key:
        :param value:
        :return:
        """
        self.root = self._insert(self.root, key, value)

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
        check whether a key is exist in AVL tree
        :param key:
        :return:
        """
        return self._contain(self.root, key)

    def _search(self, node, key):
        """
        search value of key in AVL tree whose root is node
        return None if not exist.
        :param node: search root of avl tree
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

        # if it is already the leftest node, it is minimum, return it
        if node.left is None:
            return node

        return self._minimum(node.left)

    def minimum(self):
        """
        get minimum node in a AVL tree
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
        get maximum node of a AVL tree
        :return:
        """
        return self._maximum(self.root)

    def _main_balance(self, node):
        """
        maintain balance of node
        :param node:
        :return:
        """
        # maintain balance
        balance_factor = self._height(node.left) - self._height(node.right)

        if balance_factor > 1:
            # todo: why == 0?
            if self._balance_factor(node.left) >= 0:
                # LL
                #     y
                #    /
                #   x
                #   /
                #  z
                return self._rotate_right(node)
            elif self._balance_factor(node.left) < 0:
                # LR
                #     y
                #    /
                #   x
                #    \
                #     z
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        elif balance_factor < -1:
            if self._balance_factor(node.right) <= 0:
                # RR
                #     y
                #      \
                #       x
                #        \
                #         z
                return self._rotate_left(node)
            elif self._balance_factor(node.right) > 0:
                # RL
                #     y
                #      \
                #       x
                #       /
                #      z
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        # finally return node if it is already balanced
        return node

    def _remove_min(self, node):
        if node is None:
            return

        if node.left is None:
            # if node.right is None:
            #     return None
            # else:
            #     return node.right
            # no matter whether node.right is None or not, node.right works
            self.size -= 1
            res_node = node.right
            # return node.right
        else:
            # todo: attention this recursion
            # minimum node has no left tree, if min node has a right tree,
            # its parent's left should point to to minimum node's right tree
            # usually it should stop recursion at the parent node of minimum node
            # and point right to minimum node's right tree
            # however, this recursion skillfully assign value of recursion to node.left
            # and when it encounter minimum node, just return its right node
            node.left = self._remove_min(node.left)
            res_node = node

        if res_node is None:
            return None

        # update height
        res_node.height = max(self._height(res_node.left), self._height(res_node.right)) + 1

        return self._main_balance(res_node)

    def remove_min(self):
        self.root = self._remove_min(self.root)

    def _remove_max(self, node):
        """
        remove max node of AVL tree whose root is node
        :param node:
        :return:
        """
        if node is None:
            return

        if node.right is None:
            self.size -= 1
            res_node = node.left
            # return node.left
        else:
            node.right = self._remove_max(node.right)
            res_node = node

        if res_node is None:
            return None

        res_node.height = max(self._height(res_node.left), self._height(res_node.right)) + 1

        return self._main_balance(res_node)

    def remove_max(self):
        """
        remove max node of whole AVL tree
        :return:
        """
        self.root = self._remove_max(self.root)

    def _remove(self, node, key):
        """
        delete a node in AVL tree whose root is node
        :param node:
        :param key:
        :return:
        """
        if node is None:
            return

        if node.key == key:
            # find the key, delete
            if node.left is None and node.right is None:
                self.size -= 1
                return None
            # if only have one sub tree, return the only sub tree
            elif node.left is None:
                self.size -= 1
                res_node = node.right
                # return node.right
            elif node.right is None:
                self.size -= 1
                res_node = node.left
                # return node.left
            # both of left and right is not None
            else:
                # find minimum in node.right
                # replace node with minimum in node.right
                # delete minimum node in node.right
                # node = (del(node.right, min))

                #
                #      node                  t2
                #      /   \                /  \
                #    t1     r              t1   r
                #          / \                   \
                #         t2  t3                 t3
                # t2 is successor of node
                successor = self._minimum(node.right)
                successor.right = self._remove_min(node.right)
                successor.left = node.left

                node.left = None
                node.right = None

                res_node = successor
                # return node

        elif key < node.key:
            node.left = self._remove(node.left, key)
            res_node = node
        else:  # key > node.key
            node.right = self._remove(node.right, key)
            res_node = node

        if res_node is None:
            return None

        res_node.height = max(self._height(res_node.left), self._height(res_node.right)) + 1

        return self._main_balance(res_node)

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

    test_data = list(set([random.randrange(1, 100) for _ in range(10)]))
    for item in test_data:
        bst.insert(item, item)

    print(bst.root)

    print(bst.search(test_data[0]))
    print("contain 100: %s" % bst.contain(100))

    bst.in_order()

    print("minimum:", bst.minimum())
    print("maximum:", bst.maximum())

    # bst.remove(46)

    for item in test_data:
        print("--"*100)
        print("remove: %s" % item)
        bst.remove(item)
        print("size: %s" % bst.tsize())
        bst.in_order()



