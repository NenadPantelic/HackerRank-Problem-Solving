#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:13:30 2020

@author: nenad
"""


def superReducedString(s):
    def reduceString(s):
        reducedChars = []
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                i += 2
            else:
                reducedChars.append(s[i])
                i += 1
        if i == len(s)-1:
            reducedChars.append(s[i])
        if len(reducedChars) == 0:
            return -1
        else:
            return "".join(reducedChars)
    string = reduceString(s)
    if string == -1:
        return "Empty String"
    redString = reduceString(string)
    while string != redString:
        if redString == -1:
            return "Empty String"
        string = redString
        redString = reduceString(redString)
        
    return redString
        

# Test 1
s = "aaabccddd"
print(superReducedString(s))

# Test 2
s = "aaabccdd"
print(superReducedString(s))

# Test 3
s = "aa"
print(superReducedString(s))


# Test 4
s = "baabccb"
print(superReducedString(s))

# Test 4
s = "baab"
print(superReducedString(s))