#!/usr/bin/python
# -*- coding: utf-8 -*-


class Sum(object):
    def sum_original(self, data_list):
        res = 0
        for item in data_list:
            res += item
        return res

    def sum_recursion(self, data):
        if len(data) >= 2:
            # add the 2 item at the end of list
            return data[-1] + self.sum_recursion(data[:-1])
        else:
            return data[0]

    def sum_recursion_optimize(self, data):
        """
        more graceful
        :param data:
        :return:
        """
        if len(data) == 1:
            return data[0]
        else:
            sum_res = data[0] + self.sum_recursion_optimize(data[1:])
        return sum_res


if __name__ == "__main__":
    data_test = range(100)
    sum_obj = Sum()

    sum_1 = sum_obj.sum_original(data_test)
    sum_2 = sum_obj.sum_recursion(data_test)
    sum_3 = sum_obj.sum_recursion_optimize(data_test)

    print sum_1, sum_2, sum_3
