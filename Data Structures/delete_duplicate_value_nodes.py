#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:26:06 2020

@author: nenad
"""


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def removeDuplicates(head):
    if not head:
        return head
    slow_pointer = head
    fast_pointer = slow_pointer.next
    # Runner method
    while fast_pointer:
        if slow_pointer.data != fast_pointer.data:
            slow_pointer.next = fast_pointer
            slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
    # create tail
    slow_pointer.next = None
    
    return head
    
# n1 = SinglyLinkedListNode(1)
# n2 = SinglyLinkedListNode(2)
# n3 = SinglyLinkedListNode(2)
# n4 = SinglyLinkedListNode(3)
# n5 = SinglyLinkedListNode(4)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5



# head = removeDuplicates(n1)
# node = head
# while node:
#     print(node.data)
#     node = node.next
    
    
n1 = SinglyLinkedListNode(3)
n2 = SinglyLinkedListNode(3)
n3 = SinglyLinkedListNode(3)
n4 = SinglyLinkedListNode(4)
n5 = SinglyLinkedListNode(5)
n6 = SinglyLinkedListNode(5)


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6



head = removeDuplicates(n1)
node = head
while node:
    print(node.data)
    node = node.next