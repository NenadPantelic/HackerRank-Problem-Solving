#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:56:01 2020

@author: nenad
"""


# Complete the 'getStrength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING password
#  2. INTEGER weight_a
#

from string import ascii_lowercase

def getStrength(password, weight_a):
    # Complete the function
    chars = ascii_lowercase
    charMap = {}
    for i in range(len(chars)):
        charMap[chars[i]] = (weight_a + i) % 26
    totalWeight = 0
    for char in password:
        totalWeight += charMap[char]
    return totalWeight

# Test 1
s = "hackerrank"
w = 10
print(getStrength(s,w))

# Test 2
s = "hellomrz"
w = 2
print(getStrength(s,w))