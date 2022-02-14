#! /usr/bin/env python3

import time
import random

import matplotlib.pyplot as plt

import binary_search

class SearchAlgorithmTestSet():
    def __init__(self, _start_n, _end_n, _repetition=100):
        self.start_n    = _start_n
        self.end_n      = _end_n
        self.repetition = _repetition

        self.data   = self.create_data()

    def create_test_list(self, n):
        a    = [random.sample(list(range(n)), n) for _ in range(self.repetition)]
        keys = [random.randrange(n) for _ in range(self.repetition)]
        return list(zip(keys, a))
    
    def create_data(self):
        return [self.create_test_list(n) for n in range(self.start_n, self.end_n)]


class SearchAlgorithmExecutionTime():
    def __init__(self, _functions, _start_n, _end_n, _repetition=100):
        self.functions  = _functions
        self.start_n    = _start_n
        self.end_n      = _end_n
        self.repetition = _repetition

        self.test_set   = SearchAlgorithmTestSet(_start_n, _end_n, _repetition)
        self.best_case_list, self.average_case_list, self.worst_case_list = self.create_data(_start_n, _end_n, _functions)

    def test_performance(self, _key, _a, _func):
        start = time.perf_counter()
        _func(_a, _key)
        end   = time.perf_counter()
        return end - start

    def list_performance(self, _list_of_keys_and_a, _func):
        best_case  = None
        average    = []
        worst_case = None

        for keys_and_a in _list_of_keys_and_a:
            time = self.test_performance(self, keys_and_a[0], keys_and_a[1], _func)
            if best_case is None or time < best_case:
                best_case = time
            if worst_case is None or time > worst_case:
                worst_case = time
            average.append(time)

        return best_case, sum(average) / self.repetition, worst_case

    def create_data(self, _start_n, _end_n, _func):
        best_case_list = []
        average_case_list = []
        worst_case_list = []

        print(self.test_set.data)

        for matrix in self.test_set.data:
            best_case, average, worst_case = self.list_performance(matrix, _func)
            best_case_list.append(best_case)
            average_case_list.append(average)
            worst_case_list.append(worst_case)

        print(best_case_list)

        return best_case_list, average_case_list, worst_case_list

    def plot(self):
        x_axis = range(self.start_n, self.end_n)
        print(self.best_case_list)
        plt.plot(x_axis, self.best_case_list)
        plt.plot(x_axis, self.average_case_list)
        plt.plot(x_axis, self.worst_case_list)
        plt.show()

def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

def main():
    # obj = SearchAlgorithmTestSet(10, 20, 3)
    # print(obj.list_of_keys_and_a(2))

    obj = SearchAlgorithmExecutionTime(10, 20, 3)
    obj.plot()
    

if __name__ == "__main__":
    main()
