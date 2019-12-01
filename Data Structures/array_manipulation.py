#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0 for i in range(n)]
    print(array)
    for query in queries:
        a,b, k = query
        print(a,b,k)
        array[a-1:b] = [x + k for x in array[a-1:b]]
        #arr = list(map(lambda x:x + k, arr))
    return max(array)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
