#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:14:08 2020

@author: nenad
"""

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        

def compare_lists(llist1, llist2):
    node_1 = llist1
    node_2 = llist2
    
    # one heads of them is NULL - check if other one is NULL
    if node_1 is None:
        return node_2 is None
    if node_2 is None:
        return node_1 is None
    # until at least one them reach end - compare values of coresponding nodes
    while node_1 and node_2:
        # values are not equal - lists are not the same
        if node_1.data != node_2.data:
            return False
        node_1 = node_1.next
        node_2 = node_2.next
    # one list is longer than other - False
    if node_1 or node_2:
        return False
    # else they're the same
    return True



        
        
