#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
calculate sum of a sequence by recursively call sum function on left part and right part
"""


def calc_sum(sequence, start, stop):
    if start > stop:
        return None
    if start == stop:
        return sequence[start]

    if start < stop:
        mid = (start + stop) // 2

        return calc_sum(sequence, start, mid) + calc_sum(sequence, mid + 1, stop)


if __name__ == "__main__":
    test_data = range(100)
    print(calc_sum(test_data, 0, 99))
