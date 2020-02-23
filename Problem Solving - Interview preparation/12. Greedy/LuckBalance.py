#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:31:01 2020

@author: nenad
"""


def luckBalance(k, contests):
    luck_balance = 0
    n = len(contests)
    important_contests = []
    for i in range(n):
        if contests[i][1] == 0:
            luck_balance += contests[i][0]
        else:
            important_contests.append(contests[i][0])
    important_contests.sort()
    counter = 0
    for i in range(len(important_contests)-1, -1, -1):
        counter += 1
        if counter <= k:
            luck_balance += important_contests[i]
        else:
            luck_balance -= important_contests[i]
        
    return luck_balance


# Test 1
k = 3
contests = [[5, 1], [2, 1], [1,1], [8,1], [10, 0], [5,0]]
print(luckBalance(k, contests))