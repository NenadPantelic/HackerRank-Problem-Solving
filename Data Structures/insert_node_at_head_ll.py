#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:29:54 2020

@author: nenad
"""
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedListNode(data)
    node.next = llist
    return node

llist_count = int(input())

#llist = SinglyLinkedList()
head = None
for i in range(llist_count):
    llist_item = int(input())
    llist_head = insertNodeAtHead(head, llist_item)
    head = llist_head

node = head
while node:
    print(node.data)
    node = node.next