#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
heap sort

1. heapify locally by sift each element that is not leaf down
2. swap top element and last element in array, largest element is already at end
    sift down current top element down to maintain max heap
"""


class HeapSort(object):
    def __init__(self, data):
        self.data = data

    def sift_down(self, index, size):
        """
        sift smaller element down
        :param index:
        :return:
        """
        left = 2 * index + 1
        right = 2 * index + 2

        while left < size:
            # get the max in left and right
            max_child = left
            if right < size and self.data[right] > self.data[left]:
                max_child = right

            if self.data[index] >= self.data[max_child]:
                break
            # if current value < max child, sift current element down
            self.data[index], self.data[max_child] = self.data[max_child], self.data[index]

            index = max_child
            left = 2 * index + 1
            right = 2 * index + 2

    def sort(self):
        """
        leaf element is already a sub max heap
        at first sift up all element that is not leaf element to heapify

        always swap the element at top to end and maintain the max heap until
        there is only one element which is the smallest element
        :return:
        """
        self.heapify()
        # after sift down of each element that is not leaf,
        # smaller elements have already squeeze larger element to go upward
        # the max value is already at top
        size = len(self.data)
        j = size - 1
        while j > 0:
            # swap the top element to end one by one
            self.data[0], self.data[j] = self.data[j], self.data[0]
            # after swap, the top element is not largest,
            # sift down to maintain max heap with self.data[:j]
            self.sift_down(0, j)

            j -= 1

    def heapify(self):
        """
        to make self.data satisfy properties of max heap
        :return:
        """
        size = len(self.data)
        # heapify
        # the last element that is not leaf is (size - 1) // 2
        # sift it down, and then the element before it...
        for i in range((size - 1) // 2, -1, -1):
            # sift element that is not leaf down, from end to beginning
            self.sift_down(i, size)


if __name__ == "__main__":
    import random
    import time

    random.seed(666)
    test_data = [random.randrange(0, 199) for _ in range(100000)]

    max_heap = HeapSort(test_data[:])
    t0 = time.time()
    max_heap.sort()
    t1 = time.time()
    print(t1 - t0)
    test_data.sort()
    t2 = time.time()
    print(t2 - t1)
    # assert sorted(test_data) == max_heap.data
    #
    # print(max_heap.data)



