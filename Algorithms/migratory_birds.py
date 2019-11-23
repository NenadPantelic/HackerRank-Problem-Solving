#!/bin/python3

import sys

def migratoryBirds(n, ar):
    ar.sort()
    # Complete this function
    max = 1
    maxIndex = 0
    counting = dict([val,0] for val in ar)
    for val in ar:
        counting[val] += 1
        if counting[val] > max:
            max = counting[val]
            maxIndex = val
    return maxIndex
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

