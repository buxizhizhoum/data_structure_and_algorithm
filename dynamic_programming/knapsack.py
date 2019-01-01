#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
w is an array stands for weight of products
v is an array stands for value of products
F(i, c) = max(F(i-1, c), v(i) + F(i-1, c-w(i)))
"""


class Knapsack(object):
    def basic(self, w, v, index, capacity):
        """
        basic recursion version
        :param w: array stores weight of products
        :param v: value of products
        :param index: choose from product [0, index]
        :param capacity: the capacity of package
        :return:
        """
        if index < 0 or capacity <= 0:
            return 0

        # do not choose product at index, consider next product
        res = self.basic(w, v, index - 1, capacity)
        # consider product at index
        if capacity >= w[index]:
            # if package have enough space, put it into package
            res = max(res, v[index] + self.basic(w, v, index-1, capacity-w[index]))

        return res

    def memorization(self, w, v, index, capacity, memo):
        if index < 0 or capacity <= 0:
            return 0

        if memo[index][capacity] != -1:
            return memo[index][capacity]

        # do not choose product at index, consider next product
        res = self.memorization(w, v, index - 1, capacity, memo)
        # consider product at index
        if capacity >= w[index]:
            # if package have enough space, put it into package
            res = max(res, v[index] + self.memorization(w, v, index-1, capacity-w[index], memo))

        memo[index][capacity] = res
        return res

    def dp(self, w, v, capacity):
        """
        dynamic programming
        :param w:
        :param v:
        :param capacity:
        :return:
        """
        length = len(w)
        if length == 0 or len(v) != length or capacity <= 0:
            return 0

        # length * (capacity + 1)
        memo = [[-1 for c in range(capacity + 1)] for _ in range(len(weights))]
        # initialize first row
        for j in range(capacity + 1):
            # consider product 0
            if weights[0] <= j:
                # if product could be put into package
                memo[0][j] = value[0]
            else:
                memo[0][j] = 0

        for i in range(1, length):  # start from 2nd row
            for j in range(capacity + 1):
                # do not consider product i
                memo[i][j] = memo[i-1][j]
                # if capacity is enough, consider product i
                if weights[i] <= j:
                    # max in consider and not consider
                    memo[i][j] = max(memo[i][j], value[i] + memo[i-1][j-weights[i]])

        return memo[length-1][capacity]


if __name__ == "__main__":
    weights = [2, 2, 4, 6, 3]
    value = [2, 2, 4, 6, 3]
    capacity = 9
    length = len(weights)

    print(Knapsack().basic(weights, value, length - 1, capacity))
    # todo: attention there are capacity + 1 column
    # stands for package whose capacity varies from 0 to capacity [0, capacity]
    memorization = [[-1 for c in range(capacity + 1)] for _ in range(length)]
    print(Knapsack().memorization(weights, value, len(weights)-1, capacity, memorization))

    print(Knapsack().dp(weights, value, capacity))

