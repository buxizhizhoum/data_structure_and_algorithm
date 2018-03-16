#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
shell sort, optimized based on the insert sort algorithm, it slice the data
into different group and then apply insert sort method on the grouped data
"""


class ShellSort(object):
    """
    class of shell sort
    """
    def shell_sort(self, data):
        """
        shell sort
        :param data: the data to sort
        :return:
        """
        length = len(data)
        h = 1
        # calculate maximum allowed h, shell increase step
        while h < length/3:
            h = 3 * h + 1

        # the final step, h should be equal to 1
        while h >= 1:
            for l in range(h):

                # get grouped data in step of h
                for i in range(l, length, h):

                    # do insert sort based on the grouped data in step of h
                    for j in range(l, i, h):
                        if data[i] < data[j]:
                            tmp = data[i]
                            # move data to right, start from rightest item
                            for k in range(i-h, j-1, -h):
                                # the interval to move is h
                                data[k+h] = data[k]
                            data[j] = tmp
                    # print data

            h = h / 3
        return data


if __name__ == "__main__":
    from random_list_generater import RandomListGenerator

    test_data = RandomListGenerator.random_list(100, 100)

    print("test data")
    print(test_data)

    shell_sort = ShellSort()
    sorted_data = shell_sort.shell_sort(test_data)

    print("result")
    print(sorted_data)

