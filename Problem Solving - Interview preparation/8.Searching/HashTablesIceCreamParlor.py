#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:23:36 2020

@author: nenad
"""


def what_flavors(cost, money):
    n  = len(cost)
    cost_map = {}
    for index, val in enumerate(cost):
        if val not in cost_map:
            cost_map[val] = [index]
        else:
            cost_map[val].append(index)
    for val in cost_map:
        pair_index = cost_map.get(money-val, -1)
        #print(pair_index)
        if pair_index != -1:
            if val == money-val:
                if len(pair_index) > 1:
                    val_index, pair_index = pair_index
                else:
                    val_index = None
            else:
                val_index = cost_map[val][0]
                pair_index = pair_index[0]
            if val_index is not None:
                print(val_index + 1, end=" ")
                print(pair_index + 1)
                return
        
# Test 1
cost = [1,4,5,3,2]
money = 4
what_flavors(cost, money)
        

# Test 2
cost = [4,3,2,5,7]
money = 8
what_flavors(cost, money)

# Test 3
money =  4
cost = [2, 2, 4, 3]
what_flavors(cost, money)