#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
build graph according to word file
"""

from graph import Graph


def build_graph(word_file):
    """
    buckets = {"bucket": [word1, word2]}
    bucket is the key, in the bucket there is a list, that store the words.
    :param word_file:
    :return:
    """
    buckets = {}
    graph = Graph()
    with open(word_file) as f:
        for line in f:
            word = line[:-1]  # remove /n
            for i in range(len(word)):
                # replace different letter of word with "_"
                bucket = word[:-i] + "_" + word[-i+1:]
                # if bucket is exist, append the word to list
                if bucket in buckets:
                    buckets[bucket].append(word)
                # if bucket is not exist, create a list, then append word
                else:
                    # buckets[bucket] = [word]  # simple way
                    buckets[bucket] = []
                    buckets[bucket].append(word)

    # for bucket in buckets.keys():
    #     for word_1 in buckets[bucket]:
    #         for word_2 in buckets[bucket]:
    #             if word_1 != word_2:
    #                 graph.add_edge(word_1, word_2)

    for k, v in buckets.items():
        for word_1 in v:
            for word_2 in v:
                if word_1 != word_2:
                    graph.add_edge(word_1, word_2)

    return graph


if __name__ == "__main__":

    word_file = "./word_file.txt"
    graph = build_graph(word_file)
    print graph

    for k in graph.get_vertices():
        v = graph.get_vertex(k)
        for w in v.get_connected_to():
            # print w, v
            print w.get_id(), v.get_id()
