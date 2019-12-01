#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # case when all seven values are -9
    maxHourGlassSum = -63
    for i in range(4):
        for j in range(4):
            hourGlassSum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if hourGlassSum > maxHourGlassSum:
                maxHourGlassSum = hourGlassSum
    return maxHourGlassSum

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)

'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

   

    fptr.write(str(result) + '\n')

    fptr.close()
'''
