#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Quick sort, split data to be sort into two parts each time, one part is
less than than the key item and the other part is large than the item,
apply quick sort on the splited two part, until the who list is in order.

during the sort process, slice the list by transfer different head and
tail index to do auick on different parts until all the item are in order.
"""


class QuickSort(object):
    """
    Quick sort class
    """
    def quick_sort(self, data, start=None, end=None):
        """
        quick sort, only the item whose index is between
        start and end will be sorted.
        :param data: data to be sort, in type of list
        :param start: start index of data to be sort
        :param end: end index of data to be sort
        :return:
        """
        if start is None and end is None:
            start, end = 0, len(data)

        if start >= end:
            return

        length = len(data[start:end])
        if length <= 1:
            return

        if length == 2:
            # if there are only two item and they are in order, return
            if data[start] <= data[start+1]:
                return
        key = data[start:end][0]  # the item used to split data to two part
        head, tail = start, end - 1  # the index of head and tail

        while head != tail:
            # if move head first, head should be used to split data,
            # if move tail first, tail should be used.

            while tail > head:
                # move tail backward, until find one item that is less than key
                if data[tail] < key:
                    data[head], data[tail] = data[tail], data[head]
                    break
                else:
                    tail -= 1

            while head < tail:
                # move head forward, until find one item that is less than key
                if data[head] > key:
                    data[head], data[tail] = data[tail], data[head]
                    break
                else:
                    head += 1
        # if head and tail meet at the first element,
        # this means the first element is the smallest item in this slice.
        # Move the start index to the next element
        if head == start and tail == start:
            start += 1
            head = start
            tail = end  # update tail

        # the key item used to split data could not be include,
        # it location will not change no matter whether include or not.
        self.quick_sort(data, start, tail)
        self.quick_sort(data, tail+1, end)

        return data


if __name__ == "__main__":
    from copy import deepcopy
    from random_list_generater import RandomListGenerator

    i = 0
    while i < 10000:
        i += 1

        test_data = RandomListGenerator.random_list(10, 10)

        test_data_sort = deepcopy(test_data)
        test_data_sort.sort()
        # test_data = [955, 785, 441, 878, 911, 967]
        # test_data = [7, 54, 7, 41, 8, 95]
        # test_data = [58, 91, 9, 63, 78, 61]
        # test_data = [66, 98, 49, 58, 93, 25]

        print("test data")
        print(test_data)

        quick_sort = QuickSort()
        sorted_data = quick_sort.quick_sort(test_data)

        assert test_data_sort == sorted_data

        print("result")
        print(sorted_data)
