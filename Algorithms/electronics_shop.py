#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards.sort()
    drives.sort()
    maximum = 0
    i, j = len(keyboards) - 1, len(drives) - 1
    if(keyboards[0] + drives[0] > b):
        return -1
    while (i >= 0):
        j = len(drives) - 1
        while(j >= 0):
            if(keyboards[i] + drives[j] <= b and maximum < keyboards[i] + drives[j] ): 
               maximum = keyboards[i] + drives[j] 
            j -= 1
        i -= 1
    return maximum
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

