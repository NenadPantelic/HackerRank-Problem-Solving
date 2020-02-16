#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:27:59 2020

@author: nenad
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_bst(root, minn=float("-inf"), maxx=float("inf")):
    if root is None:
        return True
    value = root.data
    if value <= minn or value >= maxx:
        return False
    return check_bst(root.left, minn, value) and check_bst(root.right, value, maxx)
    





root = Node(4)
n1 = Node(2)
n2 = Node(6)
root.left = n1
root.righ = n2
n3 = Node(7)
n3.left = n3.right = None
n4 = Node(5)
n4.left = n4.right = None
n2.right = n3
n2.left = n4
n5 = Node(1)
n5.left = n5.right = None
n6 = Node(3)
n1.left = n5
n1.right=n6
n6.left = n6.right = None
print(check_bst(root))