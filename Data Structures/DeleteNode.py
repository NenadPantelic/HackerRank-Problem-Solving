#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:32:54 2020

@author: nenad
"""


def deleteNode(head, position):
    if position == 0:
        # new head node
        if head:
            head = head.next
        return head
    i = 0
    node = head
    prev_node = head
    # until we find the element or reach the end
    while node and i < position:
        prev_node = node
        node = node.next
        
        i += 1
    if i != position:
        return head
    # remove reference to the element we want to remove
    prev_node.next = node.next
    return head
    
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
position = int(input())

llist1 = deleteNode(head, position)    
node = head
while node:
    print(node.data)
    node = node.next