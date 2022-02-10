#! /usr/bin/env python3

"""
Author: Kei Thoma
"""

def binary_search(a, key, index=0, iteration=0):
    """
    a (list) : a sorted list
    """
    if len(a) == 1 and a[0] != key:
        return -1

    m = len(a) // 2 # m for middle of the array
    if   a[m] == key: return index + m
    elif a[m] >  key: return binary_search(a[0:m], key, index, iteration + 1)
    elif a[m] <  key: return binary_search(a[m:], key, index + m, iteration + 1)

def main():
    import random

    max_n    = 10
    summands = [random.randint(0, 5) for n in range(max_n)]
    a        = [sum(summands[0:n]) for n in range(len(summands))]
    index    = random.randrange(0, max_n)
    key      = a[index]

    solution = binary_search(a, key)
    element  = a[solution]

    print("List  : {}".format(a))
    print("Index : {} | Key : {}".format(index, key))
    print()
    print("Solution index : {}".format(solution))
    print("Solution key   : {}".format(element))

if __name__ == "__main__":
    main()