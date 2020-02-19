#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:47:57 2020

@author: nenad
"""
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    visited_nodes = set()
    node = head
    
    while node:
        node_id = id(node)
        # already visited - cycle detected
        if node_id in visited_nodes:
            return True
        visited_nodes.add(node_id)
        node = node.next
    
    return False


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
 
# Test 1       
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None

print(has_cycle(n1))

# Test 2
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

print(has_cycle(n1))
