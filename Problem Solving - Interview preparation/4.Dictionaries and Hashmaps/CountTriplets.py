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
    
# Test 1
#print(count_triplets([1,2,2,4],2))

# Test 2
#print(count_triplets([1,3, 9, 9, 27, 81],3))


# Test 3
arr = [1] * 100
print(count_triplets(arr, 1))

# Test 4
arr = read_file('input06.txt')
print(count_triplets(arr, 3))
