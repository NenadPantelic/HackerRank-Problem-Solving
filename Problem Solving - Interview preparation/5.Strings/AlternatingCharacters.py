#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:44:18 2020

@author: nenad
"""


def alternating_characters(s):
    # current_index
    i = 0
    # moving index - seeks for next element different from the current one
    j = 1
    char = s[i]
    next_char = s[j]
    alter_no = 0
    while i < len(s):
        while char == next_char:
            j += 1
            if j == len(s):
                break
            next_char = s[j]
        # number of the same elements that should be removed
        alter_no += (j-i-1)
        i = j
        char = next_char
    return alter_no
        

# Test 1
s = 'AAAA'
print(alternating_characters(s))


# Test 2
s= 'ABABABAB'
print(alternating_characters(s))
            
# Test 3
s = 'BABABA'
print(alternating_characters(s))

# Test 4
s = 'AAABBB'
print(alternating_characters(s))