#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:23:18 2020

@author: nenad
"""
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
        return head
    
    node = head
    while node.next:
        node = node.next
    node.next = SinglyLinkedListNode(data)
    return head
        



llist_count = int(input())

#llist = SinglyLinkedList()
head = None
for i in range(llist_count):
    llist_item = int(input())
    llist_head = insertNodeAtTail(head, llist_item)
    head = llist_head

node = head
while node:
    print(node.data)
    node = node.next