#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:47:49 2020

@author: nenad
"""


def pairs(k, arr):
    arr.sort()
    
    

def find_pairs(arr, i, j, k, n):
    if arr[i] -  arr[j] == k:
        return 1
    for i in range(n-1):
        for j in range(i+1, n):
            