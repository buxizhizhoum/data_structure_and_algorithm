#!/usr/bin/python
# -*- coding: utf-8 -*-
"""A stack with maximum size, if not specified, it is infinite"""


class StackEmptyError(Exception):
    """stack empty error"""
    pass


class StackFullError(Exception):
    """Stack full error"""
    pass


class Length(object):
    """
    A descriptor used to describe the length of a stack
    """
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
        the value could be None or int
        :param instance: an instance of the class where this descriptor is used
        :param value: the value of this descriptor
        """
        if value is not None and not isinstance(value, int):
            raise ValueError("int expected!")
        instance.__dict__[self.name] = value


class Stack(object):
    """
    A stack with size, a descriptor is used to describe the length of
    the stack, it is not necessary, remove the descriptor is fine.

    The reason that descriptor is used here is just an exercise
    """
    # descriptor
    length = Length("length")

    def __init__(self, length=None):
        self._data = []
        self.length = length

    def __len__(self):
        return len(self._data)

    def size(self):
        """
        get the size of stack
        :return:
        """
        return len(self._data)

    def is_full(self):
        """
        Judge whether the stack is full or not

        if the length of size when initializing is None,
        stack will never be full
        """
        if self.length is None:
            return False  # when length is None, inf
        return self.size() == self.length

    def is_empty(self):
        """Judge whether the stack is empty or not"""
        return self.size() == 0

    def push(self, data):
        """
        push a element to stack
        :param data: the element to be pushed into stack
        """
        if self.is_full():
            raise StackFullError
        self._data.append(data)

    def pop(self):
        """
        get the element at the top of the stack
        :return: the element at the top of the stack
        """
        if self.is_empty():
            raise StackEmptyError
        return self._data.pop()

    def top(self):
        """
        get the value of the element at the top of the stack without delete
        it from stack
        :return: the value of the top element
        """
        if self.is_empty():
            raise StackEmptyError
        return self._data[-1]


if __name__ == "__main__":
    stack = Stack()
    # stack.length = 2
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    stack.push(3)
    stack.push(4)



