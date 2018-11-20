#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
binary search on sorted list
"""


def search(data, target, start=None, end=None):
    """
    binary search
    :param data: list to search
    :param target: which number to find
    :param start: start index
    :param end: end index
    :return: index of number if founded else None
    """
    if not data:
        return None

    start = 0 if start is None else start
    end = len(data) - 1 if end is None else end
    if start > end:
        return None

    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    if data[mid] > target:
        end = mid
    elif data[mid] < target:
        start = mid

    return search(data, target, start, end)


if __name__ == "__main__":
    test_data = range(100)
    print(search(test_data, 80))







