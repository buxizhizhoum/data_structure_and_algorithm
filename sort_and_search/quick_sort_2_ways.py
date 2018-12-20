#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
quick sort refer from imooc
"""
import random


class QuickSort(object):
    def sort(self, data):
        if not data:
            return

        self._sort(data, 0, len(data)-1)

    def _sort(self, data, l, r):
        if l >= r:
            return

        # p = self._partition(data, l, r)
        p = self._partition_2(data, l, r)
        self._sort(data, l, p - 1)
        self._sort(data, p + 1, r)

    def _partition(self, data, l, r):
        """
        choose an partition element, split data to 2 part,
        the part at left is elements less than partition element
        the part at right is elements larger than it
        :param data:
        :param l:
        :param r:
        :return:
        """
        p = data[l]

        j = l  # the index that split data to 2 part
        for i in range(l+1, r+1):
            # if data[i] > p, it is already at right side of j,
            # continue to chk next element
            if data[i] > p:
                continue
            # if data[i] < p, it should be swapped to the left part
            else:  # data[i] <= p
                # swap data[i] that is less than p with the first element in right part,
                # then the less than p part and larger p part is continue,
                data[i], data[j+1] = data[j+1], data[i]
                # j += 1 to contain the swapped less element
                j += 1

        data[l], data[j] = data[j], data[l]
        return j

    def _partition_2(self, data, l, r):
        """
        in this version of partition, at the beginning,
        the element less than partition element is put at the leftest part of the list, [l, i)
        and the data that larger than partition element is putat the rightest part of the list, (j, r]
        the element in middle is element that is not checked

        in this version, the problem that time complexity becomes to O(n^2)
        when there are many duplicated items is solved, because the items that equals to partition element
        is distributed in both side that <= and >= partition element, which will make the partition more balance
        :param data:
        :param l:
        :param r:
        :return:
        """
        # todo: Attention, these 2 lines is to randomly choose an element to split data
        # if there is no these 2 lines, the data[l] will be choosed as the element to split data,
        # and in this case, when the data is already sorted, it will be O(n^2)
        random_index = random.randrange(l, r + 1)
        # swap the randomly choose element to left
        data[l], data[random_index] = data[random_index], data[l]

        p = data[l]  # partition element

        i = l + 1  # [l, i) is elements that are less than partition element
        j = r  # (j, r] is elements that are larger than partition element
        # [i:j] is element that is not checked, [i:j] is in the middle of list
        while i <= j:
            # find the element that is larger than p
            # if data[i] == p, swap has no means, so find the data[i] > p
            # lever item == p at its original place, to make left part
            # contains element <= p, right part contains element >= p
            while i <= r and data[i] < p:
                i += 1
            # find the element that is less than p
            while j >= l + 1 and data[j] > p:
                j -= 1

            if i > j:
                break
            # data[i] is larger than p, data[j] is less than p, swap them
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

        data[l], data[j] = data[j], data[l]

        return j


if __name__ == "__main__":
    from random_list_generater import RandomListGenerator

    test_data = RandomListGenerator.random_list(100, 10)

    print("test data")
    print(test_data)

    quick_sort = QuickSort()
    quick_sort.sort(test_data)

    print("result")
    print(test_data)


