
import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here

    lastAnswer = 0
    seqList = [[] for i in range(n)]

    for i in range(len(queries)):
        q = queries[i]
        seqIndex = (q[1] ^ lastAnswer) % n

        seq = seqList[seqIndex]
        if q[0] == 1:
            seq.append(q[2])
        else:
            lastAnswer = seq[q[2] % len(seq)]
            print(lastAnswer)
        

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
q = int(first_multiple_input[1])
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
result = dynamicArray(n, queries)



