#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets_r1(arr):
    count_numbers = dict()

    count = 0
    for elem in arr:
        if(elem in count_numbers):
            if(count_numbers[elem] >= 2):
                count += count_numbers[elem] * (count_numbers[elem]-1) // 2
            count_numbers[elem] += 1
        else:
            count_numbers[elem] = 1
    return count

def countTriplets(arr, r):
    if(r == 1):
        return countTriplets_r1(arr)
    
    r_square = r ** 2

    number_counts = dict()
    accum = dict()
    
    count = 0

    for elem in arr:
        if(elem % r_square == 0):
            if(elem // r in accum):
                count += accum[elem//r]
        if(elem % r == 0):
            if(elem // r in number_counts):
                if(elem in accum):
                    accum[elem] += number_counts[elem//r]
                else:
                    accum[elem] = number_counts[elem//r]
        if(elem in number_counts):
            number_counts[elem] += 1
        else:
            number_counts[elem] = 1
    return count
            
if __name__ == '__main__':    

    f = open("input06.txt", "r")
    nr = f.read()
    nr = nr.rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, nr[2:]))

    ans = countTriplets(arr, r)

    print(str(ans))
