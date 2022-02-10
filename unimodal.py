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

    going_up = None # this checks if we are going up or not; we start by going down

    # was not needed
    start_index = 0

    def last(i): return a[i - 1]
    def next(i): return a[i]

    for i in range(1, len(a)):

        if last(i) == next(i) and going_up is None:
            current_length += 1

        elif last(i) < next(i) and going_up is None:
            current_length += 1
            going_up = True

        elif last(i) > next(i) and going_up is None:
            current_length += 1
            going_up = False

        # in the process of going up
        elif last(i) <= next(i) and going_up == True:
            current_length += 1
            going_up = True

        # we were going down and here it ends
        elif last(i) < next(i) and going_up == False:
            if max_length < current_length:
                max_length = current_length
                start_index = i - current_length
            current_length = 2
            going_up = True
        
        # this is the tipping point
        elif last(i) > next(i) and going_up == True:
            current_length += 1
            going_up = False
        
        # in the process of going down
        elif last(i) >= next(i) and going_up == False:
            current_length += 1
            going_up = False

        print("last: {} | next: {} | going_up: {} | current: {}".format(last(i), next(i), going_up, current_length))

    if max_length < current_length:
        max_length = current_length
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
        plt.plot([x for x in range(len(a))], a)
        plt.plot([x for x in range(index, index + length)], a[index : index + length])
        plt.show()

    examples1 = [
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

    for a in examples1:
        test_example(a)


    for n in range(10):
        test_example([random.randint(1, 10) for n in range(10)])


if __name__ == "__main__":
    main()
