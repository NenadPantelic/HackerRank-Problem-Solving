#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:42:12 2020

@author: nenad
"""
"""
https://www.hackerrank.com/challenges/is-binary-search-tree/problem
"""

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root, min_val = float("-inf"), max_val = float("inf")):
    
    if root is None:
        return True
    if not(min_val < root.data < max_val):
        return False
    return check_binary_search_tree_(root.left, min_val, root.data) and \
        check_binary_search_tree_(root.right, root.data, max_val)

    
