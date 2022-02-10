#! /usr/bin/env python3

import time
#time.perf_counter()

import binary_search

class BinarySearchExecutionTime():

    @staticmethod
    def linear_search(a, key):
        for i in range(len(a)):
            if a[i] == key:
                return i
        return -1