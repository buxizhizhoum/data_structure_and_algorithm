#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
quick sort comparison with partition element should start from the second element in list
"""
import random

random.seed(666)


class QuickSort(object):
    def sort(self, data):
        self._sort(data, 0, len(data)-1)

    def _sort(self, data, start, end):
        if start >= end:
            return

        # lt, gt = self._partition(data, start, end)
        lt, gt = self._partition_1(data, start, end)
        self._sort(data, start, lt)
        self._sort(data, gt, end)

    def _partition(self, data, start, end):
        # generate random index and choose an element to split data to 2 parts
        random_index = random.randrange(start, end+1)
        # swap the random element choosed to start position
        data[start], data[random_index] = data[random_index], data[start]

        p = data[start]  # partition element

        # less than p
        lt = start  # [start:lt) stores elements < p  ?? [start + 1, lt)
        # greater than p
        gt = end  # (gt, end] stores elements > p

        i = start + 1
        # start <= element_index < lt contains element < p
        # lt =< element_index <= gt contains element == p
        # gt < element_index <= end contains element > p
        while i <= gt:
            if data[i] < p:
                # in this boundary condition data[lt] stores element == p
                data[i], data[lt] = data[lt], data[i]
                lt += 1
                i += 1

            elif data[i] > p:
                # in this boundary condition data[gt] stores element == p
                data[i], data[gt] = data[gt], data[i]
                gt -= 1

            else:  # data[i] == p
                i += 1

        # after partition, data[start] == p, swap to middle range,
        # where element == p should be placed
        data[start], data[lt] = data[lt], data[start]
        # lt -= 1

        return lt-1, gt+1

    def _partition_1(self, data, start, end):
        # generate random index and choose an element to split data to 2 parts
        random_index = random.randrange(start, end+1)
        # swap the random element choosed to start position
        data[start], data[random_index] = data[random_index], data[start]

        p = data[start]  # partition element

        # less than p
        lt = start
        # greater than p
        gt = end + 1

        i = start + 1

        """
        at beginning, 
        less than p part is [start + 1, lt],
        equal part is (lt, gt)
        greater part is [gt, end]
        
        before loop both less than part and greater part range are invalid,
        equal part contains all element
        
        during loop the range of equal part is shrink and the range at
        two sides are increasing
        
        after loop, swap first element to equal range with data[lt], 
        and decr lt by 1 to contain newly swapped element to equal range
        
        and finally:
        
        start <= element_index <= lt contains element < p
        lt < element_index < gt contains element == p
        gt <= element_index <= end contains element > p
        """
        # when i == gt, data[i] == data[gt], already finished,
        # no need to go one more step
        while i < gt:
            if data[i] < p:
                # in this boundary condition, data[lt] stores element < p,
                # swap with element after it
                data[i], data[lt + 1] = data[lt + 1], data[i]
                lt += 1
                i += 1

            elif data[i] > p:
                # in this boundary condition, data[gt] stores element > p,
                # swap with element before it
                data[i], data[gt - 1] = data[gt - 1], data[i]
                gt -= 1

            else:  # data[i] == p
                i += 1

        # after partition, data[start] == p, swap to middle range,
        # where element == p should be placed
        data[start], data[lt] = data[lt], data[start]
        # after swap, data[lt] == p, lt should decrease 1
        lt -= 1

        return lt, gt


if __name__ == "__main__":
    from random_list_generater import RandomListGenerator

    test_data = RandomListGenerator.random_list(100, 10)

    print("test data")
    print(test_data)

    quick_sort = QuickSort()
    quick_sort.sort(test_data)

    print("result")
    print(test_data)

