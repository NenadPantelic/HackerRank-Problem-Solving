#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:31:34 2020

@author: nenad
"""
# medium
#check two things: 
#1. Has this person moved more than two positions forward?
# 2. How many times has this person been bribed?
def minimum_bribes(arr):
    total_bribes = 0
    for i, value in enumerate(arr):
         # correct position - i-1, e.g. for 1, it's 0
         # maximum offset - i - 1 + 2 = 1+1
         if value - i - 1> 2:
             return 'Too chaotic'
         # check who is ahead of element
         # from correct position to the current one
         for j in range(max(value - 2, 0), i):
             # if greater element is in front of it
             if arr[j] > value:
                 total_bribes += 1
    return total_bribes
                    
            
            
            
            
            
            
        
            
print(minimum_bribes([2,1,5,3,4]))
print(minimum_bribes([2,5,1,3,4]))