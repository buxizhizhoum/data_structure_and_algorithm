#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
算法图解快排
"""


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        head = array[0]
        less = [i for i in array[1:] if i < head]
        greater = [i for i in array[1:] if i >= head]
        res = quick_sort(less) + [head] + quick_sort(greater)
    return res


if __name__ == "__main__":
    a = [1, 3, 5, 3, 29, 0, 6, 5, 9]
    print(quick_sort(a))
