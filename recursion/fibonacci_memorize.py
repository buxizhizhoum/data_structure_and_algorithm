#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
optimize recursion version fibonacci by memorization
"""


def fibonacci(n, memo):
    if n == 0:
        return 1
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    # calc and memorize
    res = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = res

    return res


if __name__ == "__main__":
    n = 5
    memo = [-1 for _ in range(n+1)]
    print(fibonacci(n, memo))


