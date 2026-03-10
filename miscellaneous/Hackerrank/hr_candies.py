import math
import os
import random
import re
import sys

# Assumes there are at least 2 elements in arr => handle 1 len array
def create_monotonicity(arr):
    monotonicity = []
    for i in range(len(arr)-1):
        if(arr[i] < arr[i+1]):
            monotonicity.append(-1)
        elif(arr[i] > arr[i+1]):
            monotonicity.append(1)
        else:
            monotonicity.append(0)
    return monotonicity

# Assumes there are at least 3 elements in arr => handle 2 len array
def find_troughs(monotonicity):
    troughs_positions = []
    for i in range(1,len(monotonicity)):
        if(monotonicity[i] == -1 and monotonicity[i-1] == 1):
            troughs_positions.append(i)
        elif(monotonicity[i] == 0):
            troughs_positions.append(i)
            if(i+1 < len(monotonicity) and monotonicity[i+1] != 0):
                troughs_positions.append(i+1)
    return troughs_positions

def parse_right_from(start_index, arr, candies):

    if(start_index == len(arr)-1):
        return
        
    if(start_index == 0 and candies[start_index] == 0):
        candies[start_index] = 1
    
    if(arr[start_index] == arr[start_index+1]):
        if(start_index > 0 and arr[start_index] == arr[start_index-1]):
            candies[start_index] = 1
        elif(start_index == 0):
            candies[start_index] = 1
        return

    if(arr[start_index] < arr[start_index+1]):
        candies[start_index] = 1
        curr_index = start_index

        while(curr_index < len(arr)-1 and arr[curr_index] < arr[curr_index+1]):
            candies[curr_index+1] = candies[curr_index] + 1
            curr_index += 1
    return

def parse_left_from(start_index, arr, candies):
    if(start_index == 0):
        return
    
    if(arr[start_index] == arr[start_index-1]):
        if(start_index == len(arr) - 1):
            candies[start_index] = 1
        return
    
    if(start_index == len(arr) - 1 and candies[start_index] == 0):
        candies[start_index] = 1
    
    if(arr[start_index] < arr[start_index-1]):
        candies[start_index] = 1
        curr_index = start_index

        while(curr_index > 0 and arr[curr_index] < arr[curr_index-1]):
            if(candies[curr_index-1] > 0):
                candies[curr_index-1] = max(candies[curr_index-1], candies[curr_index]+1)
                return
            else:
                candies[curr_index-1] = candies[curr_index] + 1
                curr_index -= 1
        return

# Complete the candies function below.
def candies(n, arr):

    if(n == 1):
        return 1
    elif(n == 2):
        if(arr[1] != arr[0]):
            return 2
        else:
            return 3

    monotonicity = create_monotonicity(arr)
    troughs_positions = find_troughs(monotonicity)

    troughs_positions.append(n-1)
    troughs_positions = [0] + troughs_positions

    candies = [0] * n
    candies[0] = 1

    for trough in troughs_positions:
        #print("Trough: " + str(trough))
        parse_left_from(trough,arr,candies)
        #print("PL:" + str(candies))
        parse_right_from(trough,arr,candies)
        #print("PR: " + str(candies))
    
    total_candies = 0
    for elem in candies:
        total_candies += elem

    for index,elem in enumerate(candies):
        if(elem == 0):
            print(str(index))
            print(str(arr[index]))
    return total_candies

if __name__ == '__main__':
    f = open("input03.txt", "r")

    nr = f.read()
    nr = nr.rstrip().split()
    
    n = int(nr[0])
    arr = list(map(int, nr[1:]))

    print(candies(n,arr))

    f.close()
