#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
binary search
"""


def binary_search(alist, item):
    start = 0
    end = len(alist) - 1

    while start < end:
        middle = (start + end) // 2
        if item > alist[middle]:
            start = middle + 1
        elif item < alist[middle]:
            end = middle
        else:
            start = middle
            end = middle
    return start


if __name__ == "__main__":
    test_list = range(10)
    item_to_find = 6
    print binary_search(test_list, item_to_find)
