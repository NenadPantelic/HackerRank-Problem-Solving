#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:41:33 2020

@author: nenad
"""


def count_a(string, n):
    # e.g. 'aba', 10 -> abaabaaba + a -> len(aba) = 3 and a occurs in 'aba' 2 
    # times, 3 * 2 + a in 'a' = 7
    # full pattern search
    occurence_no = string.count('a') * (n // len(string)) 
    # the rest of the pattern up to length of n
    additional_string = string[:(n % len(string))]
    return occurence_no + additional_string.count('a')

print(count_a('aba', 10))
        
    