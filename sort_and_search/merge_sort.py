#!/usr/bin/python
# -*- coding: utf-8 -*-


class MergeSort(object):
    def __init__(self, data):
        self.data = data

    def sort(self):
        self._sort(0, len(self.data) - 1)

    def _sort(self, l, r):
        """
        sort item in [l, r]

        sort left, sort right and then merge left and right
        :param l:
        :param r:
        :return:
        """
        if l >= r:
            return l

        mid = l + (r - l) // 2
        left = self._sort(l, mid)
        right = self._sort(mid + 1, r)

        cache = self.data[l: r + 1]
        # merge left and right
        k = l
        while k <= r and left <= mid and right <= r:
            # todo: Attention, cache is start from 0, index should be align with it
            if cache[left-l] < cache[right-l]:
                self.data[k] = cache[left-l]
                left += 1
            else:
                self.data[k] = cache[right-l]
                right += 1
            k += 1

        # if one of left or right is still not append to self.data
        while k <= r:
            # if left part is exhausted
            if left > mid:
                # for item in cache[right:r+1] consider cache is start from 0,
                # modify index
                for item in cache[right-l: r-l+1]:
                    self.data[k] = item
                    k += 1

            # if right part is exhausted
            if right > r:
                # for item in cache[l:mid+1]:
                # the left part in left
                for item in cache[left-l: mid-l+1]:
                    self.data[k] = item
                    k += 1
        return l


if __name__ == "__main__":
    from random_list_generater import RandomListGenerator

    test_data = RandomListGenerator.random_list(100, 100)

    print("test data")
    print(test_data)

    merge_sort = MergeSort(test_data)
    merge_sort.sort()

    print("result")
    print(test_data)



