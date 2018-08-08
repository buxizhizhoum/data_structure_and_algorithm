#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
a stack, also an adapter of python list
"""


class StackEmptyError(Exception):
    """
    stack empty error
    """
    pass


class Stack(object):
    def __init__(self):
        self._data = []

    def __len__(self):
        """
        when __len__ is implemented, len(obj) could be used to get the length
        of obj
        :return: length
        """
        return len(self._data)

    def pop(self):
        if self.is_empty():
            raise StackEmptyError
        return self._data.pop()  # call the pop() method of list

    def push(self, data):
        self._data.append(data)  # append() method of list

    def is_empty(self):
        if len(self._data) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self._data)

    def top(self):
        if self.is_empty():
            raise StackEmptyError
        # get the last element of list, which is the top of stack
        return self._data[-1]


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    print(stack.top())

