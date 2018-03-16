#!/usr/bin/python
# -*- coding: utf-8 -*-
stack = []


def to_str(number, base):
    """
    convert a number to string according to base
    :param number:
    :param base:
    :return:
    """
    convert_string = "0123456789ABCDEF"
    if number < base:
        return convert_string[number]
    else:
        return to_str(number // base, base) + convert_string[number % base]


def to_str_stack(number, base):
    convert_string = "0123456789ABCDEF"
    if number < base:
        stack.append(convert_string[number])
    else:
        stack.append(convert_string[number % base])
        to_str_stack(number // base, base)

    return stack


if __name__ == "__main__":
    res = to_str(10, 2)
    print res

    res_stack = to_str_stack(10, 2)
    print res_stack
