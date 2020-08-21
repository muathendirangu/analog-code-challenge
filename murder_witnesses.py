import math
"""
    uses -ve infinity to take care of -ve heights
    reverses lists to save an extra iteration
    
"""


def witnesses(heights):
    no_of_witnesses = 0
    max_height = -math.inf
    for i in range(len(heights)-1, -1, -1):
        if heights[i] > max_height:
            no_of_witnesses += 1
            max_height = heights[i]
    return no_of_witnesses


if __name__ == "__main__":
    print(witnesses([3, 6, 3, 4, 1]))
