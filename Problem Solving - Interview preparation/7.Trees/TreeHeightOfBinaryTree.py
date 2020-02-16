#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:54:20 2020

@author: nenad
"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
vals = [3,2,5,1,4,6,7]
bst = BinarySearchTree()
for val in vals:
    bst.create(val)                

# count longest sequence of nodes and then just decrement 1 (no of edges for that sequence)                
def height_of_bst(root):
    if root is None:
        # annulate 
        return -1
    return 1 + max(height_of_bst(root.left), height_of_bst(root.right))

print(height_of_bst(bst.root))

# calculate height of root node
def height_of_bst(root):
    if root is None or (root.left is None and root.right is None):
        return 0
    return 1 + max(height_of_bst(root.left), height_of_bst(root.right))

print(height_of_bst(bst.root))
    