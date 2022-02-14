#! /usr/bin/env python3

import time
import random

import matplotlib.pyplot as plt

import binary_search

class SearchAlgorithmData():
    def __init__(self, _settings, _data):
        self.start_n    = _settings["start_n"]
        self.end_n      = _settings["end_n"]
        self.repetition = _settings["repetition"]

        self.best_case_list    = _data["best_case_list"]
        self.average_case_list = _data["average_case_list"]
        self.worst_case_list   = _data["worst_case_list"]

class SearchAlgorithmExecutionTime():
    def __init__(self, _functions, _n=100, _repetition=100):
        self.n          = _n
        self.repetition = _repetition
        self.functions  = _functions
    
        self.create_test_lists(self.n)

    def create_test_lists(self, n):
        a    = [random.shuffle(list(range(n))) for _ in range(self.repetition)]
        keys = [random.randrange(n) for _ in range(self.repetition)]
        self.test_set = zip(a, keys)
        return self.test_set

    def test_performance(self, _a, _key, _func):
        start = time.perf_counter()
        _func(_a, _key)
        end   = time.perf_counter()
        return end - start

    def list_performance(self, _func):
        best_case  = None
        average    = []
        worst_case = None
        for a in self.test_set:
            time = self.test_performance(a[0], a[1], _func)
            if best_case is None or time < best_case:
                best_case = time
            if worst_case is None or time > worst_case:
                worst_case = time
            average.append(time)
        return best_case, sum(average) / self.repetition, worst_case

    def create_data(self, _func, _start_n, _end_n):
        data = {
            "best_case_list"    : [],
            "average_case_list" : [],
            "worst_case_list"   : []
        }

        for n in range(_start_n, _end_n):
            self.create_test_lists(n)
            best_case, average, worst_case = self.list_performance(_func)
            data["best_case_list"].append(best_case)
            data["average_case_list"].append(average)
            data["worst_case_list"].append(worst_case)

        settings = {
            "start_n"    : _start_n,
            "end_n"      : _end_n,
            "repetition" : self.repetition
        }

        return SearchAlgorithmData(settings, data)

    def plot(self, _data):
        x_axis = range(_data.start_n, _data.end_n)
        plt.plot(x_axis, _data.best_case_list)
        plt.plot(x_axis, _data.average_case_list)
        plt.plot(x_axis, _data.worst_case_list)
        plt.show()


def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

def main():
    SAET = SearchAlgorithmExecutionTime(binary_search.binary_search)

if __name__ == "__main__":
    main()
