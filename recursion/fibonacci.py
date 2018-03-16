#!/usr/bin/python
# -*- coding: utf-8 -*-


def fibonacci(step):
    if step == 0:
        return 0
    elif step == 1:
        return 1
    else:
        return fibonacci(step - 1) + fibonacci(step - 2)


if __name__ == "__main__":
    res = fibonacci(4)
    print res
