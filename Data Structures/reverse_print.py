#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:05:07 2020

@author: nenad
"""
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

#

def reversePrint(head):
    new_head = None
    node = head
    prev_node = None
    
    while node.next:
        next_node = node.next
        node.next = None
        if prev_node:
            node.next = prev_node
        prev_node = node
        #prev_node.next = None
        node = next_node
    new_head = node
    if new_head:
        new_head.next = prev_node
    
    node = new_head
    while node:
        print(node.data)
        node = node.next
        


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        #llist = SinglyLinkedList()
        prev_node = None

        for _ in range(llist_count):
            llist_item = int(input())
            node = SinglyLinkedListNode(llist_item)
            if not prev_node:
                prev_node = node
                head = node
            else:
                prev_node.next = node 
            prev_node = node
            
            #llist.insert_node(llist_item)

        reversePrint(head)
        