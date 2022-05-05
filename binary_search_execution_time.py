#! /usr/bin/env python3

import time
import random

import matplotlib.pyplot as plt

import binary_search

class SearchAlgorithmExecutionTime():
    def __init__(self, _start_n, _end_n, _functions, _repetition=100):
        self.start_n    = _start_n
        self.end_n      = _end_n
        self.functions  = _functions
        self.repetition = _repetition

        self.test_set   = self.create_test_set() # 3-dimensional matrix
        self.best_case_list, self.average_case_list, self.worst_case_list = self.performance_data(_start_n, _end_n, _functions)

    # TEST SET GENERATION
    def create_test_matrix(self, n):
        a    = [random.sample(list(range(n)), n) for _ in range(self.repetition)]
        keys = [random.randrange(n) for _ in range(self.repetition)]
        return list(zip(keys, a))
    
    def create_test_set(self):
        return [self.create_test_matrix(n) for n in range(self.start_n, self.end_n)]

    # PERFORMANCE SET GENERATION
    def test_performance(self, _key, _a, _func):
        start = time.perf_counter()
        _func(_a, _key)
        end   = time.perf_counter()
        return end - start

    def list_performance(self, matrix, _func):
        best_case  = None
        average    = []
        worst_case = None

        for keys_and_a in matrix:
            time = self.test_performance(keys_and_a[0], keys_and_a[1], _func)
            if best_case is None or time < best_case:
                best_case = time
            if worst_case is None or time > worst_case:
                worst_case = time
            average.append(time)

        return best_case, sum(average) / self.repetition, worst_case

    def performance_data(self, _start_n, _end_n, _func):
        best_case_list = []
        average_case_list = []
        worst_case_list = []

        # print(self.test_set)

        for matrix in self.test_set:
            best_case, average, worst_case = self.list_performance(matrix, _func)
            best_case_list.append(best_case)
            average_case_list.append(average)
            worst_case_list.append(worst_case)

        # print(best_case_list)

        return best_case_list, average_case_list, worst_case_list

    def plot(self):
        x_axis = range(self.start_n, self.end_n)
        print(self.best_case_list)
        plt.plot(x_axis, self.best_case_list, label="Best Case")
        plt.plot(x_axis, self.average_case_list, label="Average Case")
        plt.plot(x_axis, self.worst_case_list, label="Worst Case")
        plt.legend()
        plt.show()

def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

def main():
    # obj = SearchAlgorithmTestSet(10, 20, 3)
    # print(obj.list_of_keys_and_a(2))

    obj = SearchAlgorithmExecutionTime(100, 1100, linear_search, 500)
    obj.plot()
    

if __name__ == "__main__":
    main()
