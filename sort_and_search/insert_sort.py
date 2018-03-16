#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
insert sort, get an item and then calculate where to insert the item.

O(N^2)
if the data is already in order, the time to move data will be zero, and there
will be only compare, this is the best situation, otherwise if the data is in
desc order, data move is need in every loop, this is the worst situation.
"""


class InsertSort(object):
    """
    class of insert sort
    """
    def insert_sort(self, data):
        """
        insert sort
        :param data: data to be sort
        :return:
        """
        # start from the 2nd item in data
        for i in range(1, len(data)):
            # data[:i-1] is the left part that is already in order,
            # the thought is to find a place in data[:i-1] to insert data[i]
            for j in range(i):
                # data[i] is to get the data from rest,
                # find the place to insert data
                # = will compatible situation item is not unique
                if data[i] <= data[j]:
                    # insert data[i] to the place of data[j]

                    # buffer data[i], since it would be covered
                    # when move data to right
                    tmp = data[i]
                    # move data[j:i-1] to right,
                    # to make room for item to insert

                    # move the rightest one first
                    for k in range(i - 1, j - 1, -1):
                        # print k
                        data[k+1] = data[k]
                    data[j] = tmp

        return data


if __name__ == "__main__":
    from random_list_generater import RandomListGenerator

    test_data = RandomListGenerator.random_list(100, 10)

    print("test data")
    print(test_data)

    insert_sort = InsertSort()
    sorted_data = insert_sort.insert_sort(test_data)

    print("result")
    print(sorted_data)

    # todo: update to make it usable in shell sort, add step h.