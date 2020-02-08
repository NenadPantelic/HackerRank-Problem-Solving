#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:03:51 2020

@author: nenad
"""


def sock_merchant(ar):
    socks = {}
    for sock in ar:
        if sock in socks:
            socks[sock] += 1
        else:
            socks[sock] = 1
    num_of_pairs = 0
    for sock_no in socks.values():
        num_of_pairs += sock_no // 2
    return num_of_pairs


#n = int(input())
#arr = list(map(int, input().split(' ')))

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20] 
print(sock_merchant(ar))        