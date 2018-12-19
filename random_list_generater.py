#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
random.seed(666)


class RandomListGenerator(object):
    def __int__(self):
        pass

    @classmethod
    def random_list(cls, max_value=10, length=10):
        """
        generate list with random itme
        :param max_value:
        :param length:
        :return:
        """
        res = []
        for i in range(length):
            res.append(random.randrange(max_value))
        return res


if __name__ == "__main__":
    random_list = RandomListGenerator.random_list()
    print random_list
