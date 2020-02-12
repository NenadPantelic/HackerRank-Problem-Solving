#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:17:20 2020

@author: nenad
"""


def maximum_toys(prices, k):
    prices.sort()
    i = 0
    num_of_toys = 0
    while prices[i] < k and i < len(prices):
        num_of_toys  += 1
        k -= prices[i]
        i += 1
    return num_of_toys

print(maximum_toys([1,12, 5, 111, 200, 1000, 10], 50))