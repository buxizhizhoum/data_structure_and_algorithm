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
        end = mid - 1
    elif data[mid] < target:
        start = mid + 1

    return search(data, target, start, end)


def search_1(data, target):
    """
    binary search
    :param data: list to search
    :param target: which number to find
    :return: index of number if founded else None
    """
    if not data:
        return None

    start = 0
    end = len(data) - 1

    return _search(data, target, start, end)


def _search(data, target, start, end):
    """
    recursion binary search
    :param data:
    :param target:
    :param start:
    :param end:
    :return:
    """
    if start > end:
        return
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    if data[mid] > target:
        end = mid - 1
    elif data[mid] < target:
        start = mid + 1
    return _search(data, target, start, end)


if __name__ == "__main__":
    test_data = range(100)
    print(search(test_data, 80))
    print(search_1(test_data, 80))







