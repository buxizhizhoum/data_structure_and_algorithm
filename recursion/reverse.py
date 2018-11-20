#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
reverse a sequence
"""

def reverse(data, start, stop):
    if not data:
        return None

    if start > stop:
        return None

    if start == stop:
        return

    if start < stop:
        data[start], data[stop] = data[stop], data[start]
        reverse(data, start + 1, stop - 1)
    return data


if __name__ == "__main__":
    test_sequence = range(100)
    print(reverse(test_sequence, 0, len(test_sequence) - 1))



