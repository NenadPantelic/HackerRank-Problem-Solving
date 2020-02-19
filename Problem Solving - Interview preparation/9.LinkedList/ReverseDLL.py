#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:09:35 2020

@author: nenad
"""


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
# reverse DLL
# one traversal - complexity O(n)
def reverse(head):
    # empty list
    if head is None:
        return None
    # only head element in list
    if head.next is None:
        return head
    
    node = head
    next_node = None
    next_next_node = None
    while True:
        # get next element if we iterate for the first time, else use next node determined in prev iteration
        next_node = node.next if next_next_node is None else next_next_node
        next_next_node = next_node.next
        # connect node and next next one in reversed order
        # n1 <-> n2
        # n2 <-> n1
        # next_node is actually the node that should be placed in front of the reversed dll
        node.prev = next_node
        # node was the tail of reversed dll so far
        next_node.next = node
        # set node to head of reversed dll again
        node = next_node 
        if next_next_node is None or node is None:
            break
    # regular order's head element becomes tail
    head.next = None
    # last element in regular order is now head element in reversed order
    next_node.prev = None
    return next_node

n1 = DoublyLinkedListNode(1)
n2 = DoublyLinkedListNode(2)
n3 = DoublyLinkedListNode(3)
n4 = DoublyLinkedListNode(4)
        
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n1

def print_dll(head):
    node = head
    while node is not None:
        print(node.data)
        node = node.next
        
def print_doubly_linked_list(node, file):
    while node:
        file.write(str(node.data) + ' ')
        node = node.next
        
print_dll(n1)
new_head = reverse(n1)
print_dll(new_head)


f = open('test1.txt', 'r')
out = open('out1.txt','a')
t = int(f.readline())
for t_itr in range(t):
       #print(t_itr)
       llist_count = int(f.readline())
       llist = DoublyLinkedList()

       for _ in range(llist_count):
           try:
               llist_item = int(f.readline())
               #print(llist_item)
               llist.insert_node(llist_item)
           except:
               continue
       new_head = reverse(llist.head)
       print_doubly_linked_list(new_head, out)
       #fptr.write('\n')
       out.write('\n')
       
f.close()
out.close()       