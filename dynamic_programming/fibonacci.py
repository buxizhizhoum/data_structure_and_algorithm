#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
dynamic programming to solve fibonacci
"""


def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    memo = [-1 for _ in range(n+1)]
    memo[0] = 1
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


if __name__ == "__main__":
    print(fibonacci(100))

