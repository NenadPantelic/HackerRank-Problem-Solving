#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:15:30 2020

@author: nenad
"""
def read_file(path):
    f = open(path, 'r')
    items = list(map(int, f.read().split()))
    f.close()
    return items

def count_triplets(arr, r):
    n = len(arr)
    freq_dict = {}
    position_map = {}
    num_of_triplets = 0
    for i in range(n):
        val = arr[i]
        if val not in freq_dict:
            freq_dict[val] = 0
            position_map[val] = []
        freq_dict[val] += 1
        position_map[val].append(i)
        
    for i in range(n):
        if r != 1:
            val = arr[i]
            # second number in progression
            next_val = val * r
            freq_map = position_map.get(next_val, [])
            freq_next = 0
            j = k = -1
            if len(freq_map) != 0:
                 j = 0
                 while j < n and freq_map[j] < i: 
                     j += 1
                 freq_next = len(freq_map) - j
            # third number in progression
            next_next_val = next_val * r
            freq_map = position_map.get(next_next_val, [])
            freq_next_next = 0
            if len(freq_map) != 0:
                 k = 0
                 while k < n and freq_map[k] < j: 
                     k += 1
                 freq_next_next = len(freq_map) - k
            
            if i < j < k:
                num_of_triplets += freq_next * freq_next_next
        # case when r is 1
        else:
            freq = freq_dict.get(val,0) 
            
            num_of_triplets += freq * (freq-1) * (freq-2) / 6
    return int(num_of_triplets)

# Test 1
print(count_triplets([1,2,2,4],2))

# Test 2
print(count_triplets([1,3, 9, 9, 27, 81],3))


# Test 3
arr = [1] * 100
print(count_triplets(arr, 1))

# Test 4
arr = read_file('input06.txt')
print(count_triplets(arr, 3))