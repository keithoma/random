#! /usr/bin/env python3

"""
"""

def unimodal(a):
    """
    a (list)
    """
    if len(a) == 0: return 0

    max_length = 0
    current_length = 1

    # modes
    # None  : Current length is 0 and looking for the first bump.
    # True  : 
    # False :
    mode = None

    def last(i): return a[i - 1]
    def next(i): return a[i]

    for i in range(1, len(a)):

        print("currently: {}".format(current_length))

        # current_length is 0 and we find an element that is going up
        if last(i) <= next(i) and mode == None:
            current_length += 1
            mode = True
    
        # in the process of going up
        elif last(i) <= next(i) and mode == True:
            current_length += 1

        # we were going down and here it ends
        elif last(i) <= next(i) and mode == False:
            if max_length < current_length:
                max_length = current_length
            current_length = 1
            mode = None

        # current_length is 0, so we don't care about this
        elif last(i) > next(i) and mode == None:
            pass
        
        # this is the tipping point
        elif last(i) > next(i) and mode == True:
            current_length += 1
            mode = False
        
        # in the process of going down
        elif last(i) > next(i) and mode == False:
            current_length += 1

    
    return max_length

def main():
    examples = [
        [9],                             #1
        [8, 7],                          #2
        [4, 5, 3, 2, 1, 3, 6, 4, 7],     #5
        [10, 9, 8, 10, 6, 5, 4, 3, 2, 3] #7
    ]

    print("hi")

    for a in examples:
        print(unimodal(a))

if __name__ == "__main__":
    main()
