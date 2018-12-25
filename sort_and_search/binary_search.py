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


def binary_search_1(nums, target):
    l = 0
    r = len(nums) - 1  # [l, r]

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            l = mid + 1
        else:  # nums[mid] > target
            r = mid - 1

    return False


def binary_search_2(nums, target):
    # todo: compare the boundary condition with function before
    l = 0
    r = len(nums)   # [l, r)

    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            l = mid + 1
        else:  # nums[mid] > target
            r = mid

    return False


if __name__ == "__main__":
    test_list = range(10)
    item_to_find = 6
    print binary_search(test_list, item_to_find)
    print binary_search_1(test_list, item_to_find)
    print binary_search_2(test_list, item_to_find)
