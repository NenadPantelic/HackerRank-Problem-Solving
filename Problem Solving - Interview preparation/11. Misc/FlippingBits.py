#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 22:04:45 2020

@author: nenad
"""


def flipping_bits(n):
    return 2 ** 32 - 1 - n


# Test 1
n = 2147483647
print(flipping_bits(n))
# Test 2
n = 1
print(flipping_bits(n))
# Test 3
n = 0
print(flipping_bits(n))
