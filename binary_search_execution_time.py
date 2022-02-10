#! /usr/bin/env python3

import binary_search

class BinarySearchAlgorithmicEfficiency():

    @staticmethod
    def linear_search(a, key):
        for i in range(len(a)):
            if a[i] == key:
                return i
        return -1