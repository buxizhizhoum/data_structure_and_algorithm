#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
exercise of BST, codes almost from:
https://github.com/facert/python-data-structure-cn/

all rights of the code from link above belongs to its original author
"""


class BinarySearchTree(object):
    """
    class of binary search tree
    """
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        """
        this is just reload [], which allows to modify data like dict
        :param key:
        :param value:
        :return:
        """
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        """
        reload in operation
        :param key:
        :return:
        """
        if self._get(key, self.root):
            return True
        else:
            return False

    def put(self, key, val):
        # if root is exist, put node after it
        if self.root:
            # start from root
            self._put(key, val, self.root)
        # if root node is None, set current node as root.
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):
        """
        less than key, to left, large than key to right, equal, cover.
        :param key:
        :param val:
        :param current_node:
        :return:
        """
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                # if no left child, then put it at the left child of this node
                current_node.left_child = TreeNode(key, val,
                                                   parent=current_node)
        elif key > current_node.key:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val,
                                                    parent=current_node)
        else:
            # if the key = current key, then cover value of current key
            current_node.payload = val

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif key == current_node.key:
            return current_node
        elif key < current_node.key:
            # if key less than current node's key, look in left tree
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        """
        delete node, before delete, node has to be searched
        :param key:
        :return:
        """
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, Tree is empty")

    def remove(self, current_node):
        """
        remove node
        if node is leaf, remove directly
        if node has two child, find successor, and replace with successor.
        if node has one child:
            if...
        :param current_node:
        :return:
        """
        # is the leaf node
        if current_node.is_leaf():
            # if it is leaf, delete directly
            if current_node.parent.left_child == current_node:
                # below if might be more simple
                # if current_node.is_left_child():
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        # has two child, find the successor and replace current node with it.
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload

        # has only one child, could replace with child node.
        # elif current_node.has_any_child() \
        #      and not current_node.has_both_child():
        else:
            # has only left child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    """
                            o
                          /  
                        oo  current node
                       /
                      o
                    """
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    """
                    o
                      \ 
                        oo  current node
                       /
                      o
                    """
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                # the node to remove is root
                else:
                    current_node.replace_node_data(
                        current_node.left_child.key,
                        current_node.left_child.payload,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child)
            # has only right child
            else:
                if current_node.is_left_child():
                    """
                            o
                          /  
                        oo  current node
                         \   
                          o 
                        
                    """
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    """
                    o
                      \ 
                        oo  current node
                         \ 
                          o
                    """
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                # the node to remove is root
                else:
                    current_node.replace_node_data(
                        current_node.right_child.key,
                        current_node.right_node.payload,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child)


class TreeNode(object):
    """
    class of tree node
    """
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        # if has parent, and the left child of parent is it self, then True
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        # if has parent, and the right child of parent is it self, then True
        return self.parent and self.parent.right_child == self

    def is_root(self):
        # if has no parent, it is root
        return not self.parent

    def is_leaf(self):
        # if its right child or left child is not None, it is not leaf
        # return not (self.right_child or self.left_child)
        return not self.has_any_children()

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        """
        if right child is exist, succ is the most left child of right sub tree
        if right child not exist:
            if the node is the left child,
                succ is the left child's parent
            if the node is the right child,
                look up until find one node whose n-1th
                ancestor is the left child of nth ancestor,
                the the successor is the nth ancestor, if not founded, the node
                is already the last one node, so there is no successor
        :return:
        """
        succ = None
        # right child is exist, succ is the most left child of right sub tree
        if self.has_right_child():
            succ = self.right_child.find_min()
        # right child not exist
        else:
            # if it is the left child, succ is the left child's parent
            if self.is_left_child():
                succ = self.parent
            # is the right child, look up until find one node whose n-1th
            # ancestor is the left child of nth ancestor,
            # the the successor is the nth ancestor, if not founded, the node
            # is already the last one node, so there is no successor
            else:
                self.parent.right_child = None
                succ = self.parent.find_successor()
                self.parent.right_child = self

        return succ

    def find_min(self):
        """
        find the most left child
        :return:
        """
        min_node = self
        while min_node.has_left_child():
            min_node = min_node.left_child()
        return min_node

    def splice_out(self):
        """
        delete successor node, successor node has at most one child, and could
        be deleted with delete method of deleting node which is leaf node or
        method that delete node that has only one child.
        :return:
        """
        # if is the leaf, remove directly
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    """
                            o
                          /
                        oo
                       /
                      o
                    """
                    self.parent.left_child = self.left_child
                    self.left_child.parent = self.parent
                else:
                    """
                            o
                          /
                        oo
                         \ 
                          o
                    """
                    self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent

            else:
                if self.has_right_child():
                    """
                    o
                      \ 
                        oo
                         \ 
                          o        
                    """
                    self.parent.left_child = self.right_child
                    self.right_child.parent = self.parent
                else:
                    """
                    o
                      \ 
                        oo
                       /
                      o
                    """
                    self.parent.right_child = self.right_child
                    self.right_child.parent = self.parent


if __name__ == "__main__":
    test_tree = BinarySearchTree()
    test_tree[3] = "red"
    test_tree[4] = "blue"
    test_tree[5] = "yellow"
    test_tree[6] = "green"
    test_tree[2] = "at"

    tmp = test_tree[3].payload
    print(test_tree[6].payload)
    print(test_tree[2].payload)
    print(test_tree)
    print(tmp)

