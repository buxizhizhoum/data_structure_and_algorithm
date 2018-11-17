#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
n!
"""


def func(x):
    if x == 1:
        return 1
    else:
        return x * func(x-1)


if __name__ == "__main__":
    print(func(3))
