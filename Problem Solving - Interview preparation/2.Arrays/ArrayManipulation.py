#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:32:54 2020

@author: nenad
"""


def array_manipulation(n, queries):
    arr = [0] * (n+1)
    for query in queries:
        a,b,k = query
        arr[a-1] += k
        arr[b] -= k
    maxx = 0
    summation = 0
    for i in range(len(arr)):
        summation += arr[i]
        if summation > maxx:
            maxx = summation
    return maxx
                
print(array_manipulation(10, [(1,5,3), (4,8,7), (6,9,1)]))