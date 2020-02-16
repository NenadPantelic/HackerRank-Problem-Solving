#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:50:26 2020

@author: nenad
"""


def special_substr_count(n, s):
    special_substr_map = {}
    next_char_for_special = {}
    
    special_substr_count = 0
    for i in range(n):
        substr = ''
        prev_substr = None
        for j in range(i,n):
            substr = substr + s[j]
            if j==i:
                special_substr_count += 1
                next_char_for_special[substr] = s[j]
                #prev_substr = s[j]
            else:
                # case when conditions are met
                if next_char_for_special[prev_substr] == s[j]:
                    special_substr_count += 1
                    next_char_for_special[substr] = prev_substr[::-1]
                else:
                    prev_suffix = next_char_for_special.get(prev_substr, None)
                    # case when our substring is two char long
                    if prev_suffix is None:
                        next_char_for_special[substr] =  prev_substr
                    else:
                        if s[j] == prev_suffix[0]:
                            next_char_for_special[substr] =  prev_suffix[1:]
                        #else:
                        #    next_char_for_special[substr] = prev_substr[::-1]
           
            prev_substr = substr
    return special_substr_count
    
    
# Test 1
s = 'mnonopoo'        
n = 8

print(special_substr_count(n, s))
            
# Test 2
s = 'abcbaba'
n = 7
print(special_substr_count(n, s))
                    