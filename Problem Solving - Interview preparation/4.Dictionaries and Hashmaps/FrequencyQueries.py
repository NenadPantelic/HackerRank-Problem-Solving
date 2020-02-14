#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:03:11 2020

@author: nenad
"""


def freq_query(queries):
    # value:occurence
    freq_map = {}
    # occurence:number of elements
    freq_count = {}
    ans = []
    for code, value in queries:
        if code == 1:
            freq = freq_map.get(value, 0)
            # increment freq of value
            freq_map[value] = freq + 1
            # update state in counting map
            if freq != 0:
                freq_count[freq] -= 1    
            freq_count[freq+1] = freq_count.get(freq+1, 0) + 1
                
        elif code == 2:
            freq = freq_map.get(value, 0)
            if freq != 0:
                # decrement occurence no
                freq_map[value] -= 1
                # update occurence map - decrement old, increment new
                freq_count[freq] -= 1
                freq_count[freq-1] = freq_count.get(freq-1,0 ) + 1 
        else:
            val = freq_count.get(value, 0)
            if val != 0:
               ans.append(1)
            else:
                ans.append(0)
                
    return ans
            

n = 10
queries = [(1,3), (2,3), (3,2), (1, 4), (1,5), (1, 5), (1,4),(3,2), (2,4),(3,2)]
#queries = [(1,5), (1, 6),(3,2), (1, 10), (1,10), (1, 6), (2, 5), (3, 2)]
print(freq_query(queries))