#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:05:33 2020

@author: nenad
"""


def two_strings(s1, s2):
    chars_s1 = set(s1)
    chars_s2 = set(s2)
    if chars_s1.intersection(chars_s2) == set():
        return 'NO'
    return 'YES'

# Test 1
s1 = 'hello'
s2 = 'world'
print(two_strings(s1,s2))

# Test 2
s1 = 'hi'
s2 = 'world'
print(two_strings(s1, s2))