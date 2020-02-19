#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:17:40 2020

@author: nenad
"""

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data) 
    index = 0
    curr_node = head
    prev_node = None
    while index < position:
        prev_node = curr_node
        curr_node = curr_node.next
        index += 1
    
    # set next node 
    node.next = curr_node
    # for previous node set next node 
    if prev_node is not None:
        prev_node.next = node
    else:
        # head node case
        head = node
    return head
        
