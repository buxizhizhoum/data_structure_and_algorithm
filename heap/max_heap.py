#!/usr/bin/python
# -*- coding: utf-8 -*-


class MaxHeap(object):
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def empty(self):
        return self.size() == 0

    def parent(self, index):
        if index == 0:
            print("index 0 has no parent")
            return None
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def put(self, element):
        """
        add element to heap
        :param element:
        :return:
        """
        self.heap.append(element)
        # sift up the element append before
        self.sift_up(self.size() - 1)

    def get(self):
        """
        pop the max element from heap
        :return:
        """
        size = self.size()
        if size < 0:
            return None
        res = self.heap[0]
        self.heap[0], self.heap[size - 1] = self.heap[size - 1], self.heap[0]
        self.heap.pop()
        self.sift_down(0)
        return res

    def peek_up(self):
        """
        get max element with out delete
        :return:
        """
        return self.heap[0]

    def sift_up(self, index):
        """
        sift up element at index
        :param index:
        :return:
        """
        if self.size() == 1:
            return
        parent_index = self.parent(index)
        # sift up if it is larger than its parent
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # update index
            index = parent_index
            parent_index = self.parent(index)

    def sift_down(self, index):
        """
        sift down element
        :param index:
        :return:
        """
        if self.size() == 0:
            return

        left = self.left_child(index)
        right = self.right_child(index)

        while left < self.size():
            # get the index of max child
            max_child_index = left
            # if right exist, compare left with right and get the larger one
            if right < self.size() and self.heap[right] > self.heap[left]:
                # todo: what if ==?
                max_child_index = right

            # get the larger child and then compare with parent to decided
            # whether to continue
            if self.heap[index] >= self.heap[max_child_index]:
                # parent already larger than left and right child
                break
            # sift down, swap with max child
            self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]

            # update index
            index = max_child_index
            left = self.left_child(max_child_index)
            right = self.right_child(max_child_index)

    def sift_down_recursion(self, index):
        """
        sift down recursion version
        :param index:
        :return:
        """
        if self.size() == 0:
            return

        left = self.left_child(index)
        right = self.right_child(index)
        # if the element is leaf
        if left >= self.size():
            return

        max_child_index = left
        if right < self.size():
            if self.heap[right] > self.heap[left]:
                max_child_index = right

        # if already max heap, return
        if self.heap[index] >= self.heap[max_child_index]:
            return

        self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]

        index = max_child_index
        self.sift_down_recursion(index)


if __name__ == "__main__":
    import random
    test_data = [random.randint(0, 100) for i in range(10)]
    # test_data = [0, 16, 1, 7, 86, 96, 26, 21, 37, 98]
    print(test_data)

    max_heap = MaxHeap()
    for item in test_data:
        max_heap.put(item)

    test_res = [max_heap.get() for i in range(max_heap.size())]
    assert test_res == sorted(test_data, reverse=True)

