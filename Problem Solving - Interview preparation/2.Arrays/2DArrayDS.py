#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:51:08 2020

@author: nenad
"""

def hourglass_sum(arr):
    max_hour_glass_sum = -63
    for i in range(4):
        for j in range(4):
            hour_glass_sum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if hour_glass_sum > max_hour_glass_sum:
                max_hour_glass_sum = hour_glass_sum
    return max_hour_glass_sum

arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], \
       [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    
print(hourglass_sum(arr))