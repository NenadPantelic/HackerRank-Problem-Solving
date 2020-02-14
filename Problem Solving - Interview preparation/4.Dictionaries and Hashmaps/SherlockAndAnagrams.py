#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:09:27 2020

@author: nenad
"""


def sherlock_and_anagrams(s):
    n = len(s)
    num_of_anagrams = 0
    substr_map = {}
    # we're getting all substrings
    # loop over whole string
    for i in range(n):
        substr = ''
        # all substrings that start with i-character
        for j in range(i, n):
            # create sorted string made from characters that appear in this substring
            # so, we're creating 'base' string for every substring - base substring is sorted version
            # of some substring. Number of permutations of base string that appear in our string as a substring
            #we  keep in substr_map[substr]
            substr = ''.join(sorted(substr+s[j]))
            if substr not in substr_map:
                substr_map[substr] = 0
            substr_map[substr] += 1
    num_of_anagrams = sum([freq*(freq-1)//2 for freq in substr_map.values()])
    return num_of_anagrams            
            

# Test 1
s = 'ifailuhkqq'
print(sherlock_and_anagrams(s))

# Test 2
s = 'kkkk'
print(sherlock_and_anagrams(s))

# Test 3
s = 'xyyx'
print(sherlock_and_anagrams(s))