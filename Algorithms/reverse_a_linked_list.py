#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:30:12 2020

@author: nenad
"""
"""
https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
"""

def reverse(head, prev = None):
    if not head:
        return prev
    
    nextNode = head.next
    head.next = prev
    return reverse(nextNode, head)
    

