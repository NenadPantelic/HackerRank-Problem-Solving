#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:58:45 2020

@author: nenad
"""

# easy
# Time complexity O(n), Aux Space O(n)
def rot_left(arr, d):
    rotated_arr = arr[:]
    for i in range(len(arr)-1, -1, -1):
        rotated_arr[i-d] = arr[i]
    return rotated_arr

d = 4
arr = list(range(1,6))
print(rot_left(arr, d))