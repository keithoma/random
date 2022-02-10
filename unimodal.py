#! /usr/bin/env python3

"""
Authors:
Tanmay Sule
Kei Thoma
"""

def unimodal(a):
    """
    a (list)
    """
    if len(a) == 0: return 0

    current_length = 1
    max_length     = 0
    going_up       = None # this checks if we are going up or not; we start by going down
    start_index    = 0    # was not needed for the assignment

    def last(i): return a[i - 1]
    def nxt(i): return a[i]

    for i in range(1, len(a)):

        # at the beginning, we have to find out if we are going up or not
        if last(i) == nxt(i) and going_up is None:
            current_length += 1

        elif last(i) < nxt(i) and going_up is None:
            current_length += 1
            going_up = True

        elif last(i) > nxt(i) and going_up is None:
            current_length += 1
            going_up = False

        # in the process of going up
        elif last(i) <= nxt(i) and going_up is True:
            current_length += 1
            going_up = True

        # we were going down and here it ends
        elif last(i) < nxt(i) and going_up is False:
            if max_length < current_length:
                max_length = current_length
                start_index = i - current_length
            current_length = 2
            going_up = True

        # this is the tipping point
        elif last(i) > nxt(i) and going_up is True:
            current_length += 1
            going_up = False

        # in the process of going down
        elif last(i) >= nxt(i) and going_up is False:
            current_length += 1
            going_up = False

    if max_length < current_length:
        max_length = current_length
        start_index = len(a) - current_length
    return max_length, start_index

def main():
    import random
    import matplotlib.pyplot as plt

    def test_example(a):
        length, index = unimodal(a)
        print("Example list   : {}".format(a))
        print("Maximal length : {}".format(length))
        print("Sequence       : {}".format(a[index : index + length]))
        print()
        plt.plot(range(len(a)), a)
        plt.plot(range(index, index + length), a[index : index + length])
        plt.show()

    examples = [
        [0],
        [1],
        [1, 1, 1, 1, 2, 2],
        [-1, -1, -1, -1, 10],
        [1, 1, 2, 2, 2, 2, 1, 1, 1, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2],
        [2, 1, 1, 1, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 3, 2, 2],
        [1, 1, 3, 2, 2],
    ]

    for a in examples:
        test_example(a)

    for _ in range(10):
        test_example([random.randint(1, 10) for n in range(10)])

if __name__ == "__main__":
    main()
