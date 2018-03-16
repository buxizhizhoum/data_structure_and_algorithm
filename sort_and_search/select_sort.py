#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Select sort, compare and select the item before get the data to move

O(N^2)
the cpu time has no related to whether the data is sorted or not.
the time of moving the data is the smallest.

python 2.7 tested
"""


class SelectionSort(object):
    def __int__(self):
        pass

    def select_sort(self, data):
        """
        select sort, this version only implement increasing sort
        :param data: data to be sorted
        :return: sorted data
        """
        # check data type
        if not all(type(value) in (int, float, str) for value in data):
            print("the input data should be a list of int, float or str")
            raise ValueError

        for i in range(len(data) - 1):

            min_index = i  # initialize min_index
            min_item = data[i]  # initialize min_item to data[i]
            for j in range(i, len(data)):
                # this loop find the index of min item in data[i:]
                if data[j] < min_item:
                    min_item = data[j]  # update min item
                    min_index = j  # update min index
            if min_index != i:
                # swap data[i] and the min item of data[i:]
                data[i], data[min_index] = data[min_index], data[i]
        return data

    """
    def min_index(self, i, data):
        index = i
        min_item = data[i]
        for j in range(i, len(data)):
            if data[j] < min_item:
                min_item = data[j]
                index = j
        return index
    """

    def is_sorted(self, data, decrease=False):
        """
        check whether data is sorted.
        :param data: list to be checked
        :param decrease: flag
        :return:
        """
        if decrease is False:
            # increasing
            for i in range(len(data) - 1):
                if data[i] > data[i+1]:
                    return False

            return True

        elif decrease is True:
            # decreasing
            for i in range(len(data) - 1):
                if data[i] < data[i + 1]:
                    return False

            return True

        else:
            print("wrong type of decrease parameter, %s" % decrease)
            raise ValueError


if __name__ == "__main__":
    # import class used to generate test data.
    from random_list_generater import RandomListGenerator

    test_data = RandomListGenerator.random_list(10, 10)

    print("test data")
    print(test_data)

    select_sort = SelectionSort()
    sorted_data = select_sort.select_sort(test_data)
    assert select_sort.is_sorted(sorted_data)

    print("result")
    print(sorted_data)
