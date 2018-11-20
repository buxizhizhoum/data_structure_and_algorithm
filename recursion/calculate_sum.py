#!/usr/bin/python
# -*- coding: utf-8 -*-


def calc_sum(data):
    if not data:
        return None

    if len(data) == 1:
        return data[0]

    return data[0] + calc_sum(data[1:])


if __name__ == "__main__":
    test_data = range(100)
    print(calc_sum(test_data))

