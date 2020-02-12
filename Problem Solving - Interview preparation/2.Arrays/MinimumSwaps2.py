#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:58:46 2020

@author: nenad
"""

# Medium O(nlog(n)), Aux memory - O(n)
def count_swaps(arr):
    num_of_swaps = 0
    positions = list(enumerate(arr))
    positions.sort(key=lambda value:value[1])
    print(positions)
    visited = {i:False for i in range(len(arr))}
    for i in range(len(arr)):
        # node is already visited or it is on right place
        if visited[i] or positions[i][0] == i:
            continue
        j = i
        cycle_len = 0
        while not visited[j]:
            visited[j] = True
            j = positions[j][0]
            print(j)
            cycle_len += 1
        
        if cycle_len > 0:
            num_of_swaps += cycle_len - 1
           
        
    return num_of_swaps
        


print(count_swaps([7,1,3,2,4,5,6]))