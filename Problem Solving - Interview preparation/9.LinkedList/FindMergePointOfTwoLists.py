#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:59:15 2020

@author: nenad
"""


# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
from collections import defaultdict
def findMergeNode(head1, head2):
    visited_nodes = defaultdict(int)
    node1 = head1
    node2 = head2
    
    while node1 or node2:
        if node1:
            id1 = id(node1)
            # already visited - merge point
            if id1 in visited_nodes:
                return visited_nodes[id1] 
            visited_nodes[id1] = node1.data
            node1 = node1.next
        if node2:
            id2 = id(node2)
            if id2 in visited_nodes:
                # already visited - merge point
                return visited_nodes[id2] 
            visited_nodes[id2] = node2.data
            node2 = node2.next
    
        