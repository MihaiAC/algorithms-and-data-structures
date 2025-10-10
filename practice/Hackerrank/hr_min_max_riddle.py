

#!/bin/python3

import math
import os
import random
import re
import sys

def construct_stack(arr,max_window,stack):
    stack.append([arr[0],1])

    for i in range(1,len(arr)):
        elem = arr[i]
        if(elem > stack[-1][0]):
            stack.append([elem,1])
        elif(elem == stack[-1][0]):
            stack[-1][1] += 1
        else:
            accum = 0
            while(len(stack) > 0 and elem < stack[-1][0]):
                stack_top = stack.pop()
                accum += stack_top[1]
                
                if(stack_top[0] in max_window):
                    max_window[stack_top[0]] = max(accum,max_window[stack_top[0]])
                else:
                    max_window[stack_top[0]] = accum
                
            if(len(stack) != 0 and elem == stack[-1][0]):
                stack[-1][1] += accum + 1
            else:
                stack.append([elem,accum+1])

# Called after the end of the list is reached in construct_stack.
def flush_stack(stack,max_window):
    accum = 0
    while(len(stack) != 0):
        elem = stack.pop()
        accum += elem[1]
        if(elem[0] in max_window):
            max_window[elem[0]] = max(accum,max_window[elem[0]])
        else:
            max_window[elem[0]] = accum

def invert_map(source_map):
    target_map = dict()
    for key in source_map.keys():
        window_size = source_map[key]
        if(window_size not in target_map or (window_size in target_map and target_map[window_size] < key)):
            target_map[window_size] = key
    return target_map

def build_result(size,elem_from_window):
    last_window_size = size
    result = [0] * size
    for window_size in range(size,0,-1):
        if(window_size not in elem_from_window):
            result[window_size-1] = elem_from_window[last_window_size]
        else:
            if(elem_from_window[window_size] < elem_from_window[last_window_size]):
                result[window_size-1] = elem_from_window[last_window_size]
            else:
                result[window_size-1] = elem_from_window[window_size]
                last_window_size = window_size
    return result
 

# Complete the riddle function below.
def riddle(arr):
    max_window = dict()
    stack = list()

    construct_stack(arr,max_window,stack)
    flush_stack(stack,max_window)
    elem_from_window = invert_map(max_window)
    return build_result(len(arr),elem_from_window)
        

if __name__ == '__main__':

    arr = []
    arr = [789168277, 694294362, 532144299, 20472621, 316665904, 59654039, 685958445, 925819184, 371690486, 285650353, 522515445, 
    624800694, 396417773, 467681822, 964079876, 355847868, 424895284, 50621903, 728094833, 535436067, 221600465, 832169804, 641711594,
    518285605, 235027997, 904664230, 223080251, 337085579, 5125280, 448775176, 831453463, 550142629, 822686012, 555190916, 911857735, 
    144603739, 751265137, 274554418, 450666269, 984349810, 716998518, 949717950, 313190920, 600769443, 140712186, 218387168, 416515873, 
    194487510, 149671312, 241556542, 575727819, 873823206]

    print([x // 10000000 for x in arr])


    res = riddle(arr)
    print(res)