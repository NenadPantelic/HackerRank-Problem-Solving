#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:53:50 2020

@author: nenad
"""


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test 1
n = 1
print(fibonacci(n))

# Test 2
n = 3
print(fibonacci(n))


# Test 3
n = 10
print(fibonacci(n))

# Test 4
n = 30
print(fibonacci(n))