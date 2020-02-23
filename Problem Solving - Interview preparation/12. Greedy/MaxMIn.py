#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 13:01:20 2020

@author: nenad
"""


def maxMin(k, arr):
    arr.sort()
    # max possible value of any element in arr
    minn = 10**9
    for i in range(len(arr)-k+1):
        value = arr[i+k-1] - arr[i]
        if value < minn:
            minn = value
    return minn

# Test 1
arr = [10,100,300,200,1000,20,30]
k = 3
    
print(maxMin(k, arr))


# Test 2
arr = [1,2,3,4,10,20,30,40,100,200]
k = 4
    
print(maxMin(k, arr))

# Test 3
arr = [100, 200, 300, 350, 400, 401, 402]
k = 3
print(maxMin(k, arr))