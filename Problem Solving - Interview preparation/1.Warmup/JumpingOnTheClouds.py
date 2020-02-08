#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:29:58 2020

@author: nenad
"""


def jumping_on_clouds(clouds):
    position = 0
    jumps = 0
    num_of_clouds = len(clouds)
    while position < num_of_clouds-1:
        if position < num_of_clouds - 2 and clouds[position + 2] != 1:
            position += 2
        else:
            position += 1
        jumps += 1
    # final jump
    if position != num_of_clouds-1:
        jumps += 1
    return jumps

n = 6
clouds = [0,0,1,0,0,1, 0]
print(jumping_on_clouds(clouds))