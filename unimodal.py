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

    mode = False # this checks if we are going up or not; we start by going down

    # was not needed
    start_index = 0

    def last(i): return a[i - 1]
    def next(i): return a[i]

    for i in range(1, len(a)):

        # in the process of going up
        if last(i) <= next(i) and mode == True:
            current_length += 1
            mode = True

        # we were going down and here it ends
        elif last(i) < next(i) and mode == False:
            if max_length < current_length:
                max_length = current_length
                start_index = i - current_length
            current_length = 2
            mode = True
        
        # this is the tipping point
        elif last(i) > next(i) and mode == True:
            current_length += 1
            mode = False
        
        # in the process of going down
        elif last(i) >= next(i) and mode == False:
            current_length += 1
            mode = False



        # print("last = {}, next = {} | mode: {}, currently: {}".format(last(i), next(i), mode, current_length))
    

    if max_length < current_length:
        max_length = current_length
    return max_length, start_index

def main():
    import random
    def test_example(a=[random.randint(1, 10) for n in range(10)]):
        length, index = unimodal(a)
        print("Example list   : {}".format(a))
        print("Maximal length : {}".format(length))
        print("Sequence       : {}".format(a[index : index + length]))
        print()

    test_example()

    examples = [
        [10, 9, 8, 7],                    #4
        [4, 5, 3, 2, 1, 3, 6, 4, 7],      #5
        [10, 9, 8, 10, 6, 5, 4, 3, 2, 3], #7
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 3],   #9
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 3] #10
    ]

    for a in examples:
        test_example(a)

if __name__ == "__main__":
    main()
