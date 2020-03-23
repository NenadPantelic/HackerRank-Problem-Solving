#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:26:26 2020

@author: nenad
"""

"""
Problem description: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

"""
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    stack = []
    node = head
    # push to stack all values in list - space complexity O(n)
    while node:
        stack.append(node.data)
        node = node.next
    # pop k-1 element from stack (our target value is kth element)
    for i in range(positionFromTail):
        stack.pop(-1)
    return stack.pop(-1)

