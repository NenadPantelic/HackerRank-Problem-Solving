#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:44:06 2020

@author: nenad
"""


def make_anagram(a,b):
    anagram_removals = 0
    map_a, map_b = {}, {}
    for char in a:
        map_a[char] = map_a.get(char, 0) + 1
    for char in b:
        map_b[char] = map_b.get(char, 0) + 1
    
    unique_chars = set(a+b)
    # for every char - number of removals for that char is difference between max and min value
    # off occurence in these two strings, e.g. char a appears x times (let's say 4), and in b y times (e.g.3)
    # So, num of deletions for that char is 4-3 = 1
    for char in unique_chars:
        anagram_removals += abs(map_a.get(char, 0) - map_b.get(char, 0))
    return anagram_removals
    

# Test 1
a = 'cde'
b = 'abc'
print(make_anagram(a,b))


# Test 2
a = 'cde'
b = 'dcf'
print(make_anagram(a,b))