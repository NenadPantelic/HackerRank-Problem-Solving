#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:55:06 2020

@author: nenad
"""
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def printLinkedList(head):
    node = head
    while node:
        print(node.data)
        node = node.next
    
