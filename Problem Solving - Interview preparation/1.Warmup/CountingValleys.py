#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:15:53 2020

@author: nenad
"""

def count_valleys(pattern):
    valley_no = 0
    height = 0
    for step in pattern:
        if step == 'U':
            height += 1
            prev = 'up'
        else:
            height -= 1
            prev = 'down'
        if prev == 'up' and height == 0:
            valley_no += 1
    return valley_no

n = 8
steps = 'UDDDUDUU'

print(count_valleys(steps))