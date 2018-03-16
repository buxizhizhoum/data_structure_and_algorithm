#!/usr/bin/python
# -*- coding: utf-8 -*-


class Queue(object):
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        if self.queue:
            return False
        else:
            return True

    def dequeue(self):
        return self.queue.pop()

    def enqueue(self, item):
        self.queue.insert(0, item)  # insert item at the beginning of list
