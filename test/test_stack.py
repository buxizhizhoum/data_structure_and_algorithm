#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase

from basic.stack import Stack


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        # stack = Stack()
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(0, self.stack.size())

    def test_pop(self):
        # stack = Stack()
        self.stack.push(1)
        self.assertEqual(1, self.stack.pop())

    def test_top(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(2, self.stack.top())

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.pop())


if __name__ == "__main__":
    unittest.main()
