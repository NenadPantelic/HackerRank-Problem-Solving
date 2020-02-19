#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:16:05 2020

@author: nenad
"""

#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, file):
    while node:
        file.write(str(node.data) + ' ')
        node = node.next
# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    
    node = DoublyLinkedListNode(data)
    # empty list
    if head is None:
        return node
    # replace head (smaller than head data)
    if node.data < head.data:
        node.next = head
        head.prev = node
        #head = node
        return node
    
    curr_node = head
    while curr_node.next is not None and node.data > curr_node.next.data:
        curr_node = curr_node.next
        
    next_node = curr_node.next          
    
    # tail case
    if next_node is None:
        curr_node.next = node
        node.prev = curr_node
    else:
        # connect new node and next one
        node.next = next_node
        next_node.prev = node
        # connect new node and previous one
        curr_node.next = node
        node.prev = curr_node
    return head



f = open('test.txt', 'r')
out = open('out.txt','a')
t = int(f.readline())
for t_itr in range(t):
       llist_count = int(f.readline())
       llist = DoublyLinkedList()

       for _ in range(llist_count):
           try:
               llist_item = int(f.readline())
               #print(llist_item)
               llist.insert_node(llist_item)
           except:
               continue
       data = int(f.readline())
       #print(data)
       llist1 = sortedInsert(llist.head, data)
       print_doubly_linked_list(llist1, out)
       #fptr.write('\n')
       out.write('\n')
       
f.close()
out.close()       
        

    

