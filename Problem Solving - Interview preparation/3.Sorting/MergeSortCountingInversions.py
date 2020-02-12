#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:28:06 2020

@author: nenad
"""

inversions = 0

# one test case fails due timeout
def merge_sort_swaps(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left_arr = merge_sort_swaps(arr[:mid])
    right_arr = merge_sort_swaps(arr[mid:])
    return merge(left_arr, right_arr)

# faster version
def merge_sort_swaps(arr, left, right):
    if right-left < 1:
        return arr[left:right+1]
    mid = left + (right-left) // 2
    left_arr = merge_sort_swaps(arr, left,mid)
    right_arr = merge_sort_swaps(arr, mid+1, right)
    return merge(left_arr, right_arr)
    
def merge(left, right):
    global inversions
    i = j = 0 
    sorted_arr = []
    len_l = len(left); len_r = len(right)
    while i < len_l and j < len_r:
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            # update inversions
            inversions += len_l - i
            j += 1
    while i < len_l:
        sorted_arr.append(left[i])
        i += 1
    while j < len_r:
        sorted_arr.append(right[j])
        j += 1
    return sorted_arr
        
a = [1,1,1,2,2]
arr = merge_sort_swaps(a, 0 ,len(a)-1)
#print(arr)
print(inversions)
arr = [2,1,3,1,2]
arr = merge_sort_swaps(arr, 0 ,len(arr)-1)
#arr = [2,1,3,1,2]
print(inversions)
print(arr)