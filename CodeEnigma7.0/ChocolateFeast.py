#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:55:42 2020

@author: nenad
"""


def count_chocolates(money, cost, repl):
    bars = money // cost
    count = bars
    wrappers = bars

    while wrappers // repl > 0:
        #bars = money//cost
        #wrappers += bars
        #count += bars
        #money = money % cost
        bars = wrappers//repl
        wrappers %= repl
        count += bars
        wrappers += bars
    return count


# Test 1
print(count_chocolates(16,3,2))

# Test 2
print(count_chocolates(10,2,5))


# Test 3
print(count_chocolates(12,4,4))


# Test 4
print(count_chocolates(6,2,2))