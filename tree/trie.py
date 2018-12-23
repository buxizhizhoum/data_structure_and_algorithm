#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, isword=False):
        self.isword = isword  # whether this node is a word or not
        self.next = {}  # the next node {char: Node, ...}


class Trie(object):
    def __init__(self):
        # self.root = None
        # it is better to initialize root as a Node
        # the root node contains a map which is the gate of trie,
        # different char to different branch
        self.root = Node()
        self.size = 0

    def add(self, word):
        """
        add word to trie
        :param word:
        :return:
        """
        cur = self.root  # start from root, search step by step
        for char in word:
            # if char not in trie
            if cur.next.get(char) is None:
                # new a node
                cur.next[char] = Node()
                # cur = cur.next[char]
            # else:
            #     cur = cur.next[char]

            # update loop variable
            cur = cur.next[char]

        if cur.isword is False:
            cur.isword = True
            self.size += 1

    def contains(self, word):
        """
        check whether word is in trie
        :param word:
        :return:
        """
        cur = self.root  # start from root, search step by step
        for char in word:
            # if char not exist, means word not exist, return
            if cur.next.get(char) is None:
                return False
            cur = cur.next[char]

        # check whether the char is marked is end of word
        if cur.isword is True:
            return True
        return False

    def is_prefix(self, prefix):
        """
        check whether there is a word which starts with prefix
        :param prefix:
        :return:
        """
        cur = self.root
        for char in prefix:
            if cur.next.get(char) is None:
                return False
            cur = cur.next[char]

        return True


if __name__ == "__main__":
    trie = Trie()

    word_list = ["cat", "dog", "tom", "jerry", "caterpillar"]
    for item in word_list:
        print(trie.add(item))

    for item in word_list:
        print(trie.contains(item))

    print(trie.is_prefix("cat"))

