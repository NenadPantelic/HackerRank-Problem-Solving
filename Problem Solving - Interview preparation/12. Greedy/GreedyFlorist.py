#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 13:11:53 2020

@author: nenad
"""

# k - number of friends
# c - cost array
def getMinimumCost(k, c):
    n = len(c)
    cost = 0
    counter = 0
    c.sort()
    # go from backside - first take the most expensive flowers
    for i in range(n-1, -1, -1):
        # update cost with number of previously bought flowers for that customer
        cost += (counter //k + 1) * c[i]
        counter += 1
    return cost
# Test 1
k = 3
c = [2,5,6]
print(getMinimumCost(k, c))

# Test 2
k = 2
c = [2,5,6]
print(getMinimumCost(k, c))

k = 3
c = [1, 3, 5, 7, 9]
print(getMinimumCost(k, c))