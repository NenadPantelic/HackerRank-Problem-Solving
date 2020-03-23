#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:02:46 2020

@author: nenad
"""


#
# Complete the 'getMaxStreaks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY toss as parameter.
#

def getMaxStreaks(toss):
    # Return an array of two integers containing the maximum streak of heads and tails respectively
    maxHeads = maxTails = 0
    currHeads = currTails = 0
    n = len(toss)
    i = 0
    while i < n:
        val = toss[i]
        counter = 1
        while i < n-1 and val == toss[i+1]:
            counter += 1
            i += 1
        else:
            if val == "Heads":
                maxHeads = max(maxHeads, counter)
            else:
                maxTails = max(maxTails, counter)
        i += 1
                
    if val == "Heads":
        maxHeads = max(maxHeads, counter)
    else:
        maxTails = max(maxTails, counter)
    
    return maxHeads, maxTails

# Test 1
arr = ["Heads", "Tails", "Tails", "Tails", "Heads", "Heads", "Tails"]
print(getMaxStreaks(arr))
# Test 2
toss = ["Tails", "Tails", "Tails"]
print(getMaxStreaks(toss))    

# Test 3
toss = ["Heads", "Heads", "Heads", "Heads"]
print(' '.join(map(str, getMaxStreaks(toss))))               
            