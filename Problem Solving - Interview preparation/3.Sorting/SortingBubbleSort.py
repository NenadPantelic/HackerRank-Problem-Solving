#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:10:36 2020

@author: nenad
"""


def count_swaps_in_bs(arr):
    num_of_swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                num_of_swaps += 1
    return num_of_swaps, arr[0], arr[-1]

swaps, minn, maxx = count_swaps_in_bs([6,4,1])
print('Array is sorted in {} swaps.'.format(swaps))
print('First Element: {}'.format(minn))
print('Last Element: {}'.format(maxx))