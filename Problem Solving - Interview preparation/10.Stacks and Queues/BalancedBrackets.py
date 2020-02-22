#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:28:01 2020

@author: nenad
"""


def is_balanced(bracket_expr):
    stack = []
    mapping = {'(':')', '{':'}', '[':']'}
    for char in bracket_expr:
        if char in '([{':
            # push to stack opening bracket
            stack.append(char)
        else:
            # stack is empty and we have an enclosing bracket
            # if there is not any opening bracket in stack and we current char is enclosing bracket
            if len(stack) == 0:
                return 'NO'
            else:
                # if there is not match between opening and enclosing bracket
                last_el = stack.pop(-1)
                if mapping[last_el] != char:
                    return 'NO'
    # if there are still opening brackets in stack that do not have their enclosing match
    if len(stack) > 0:
        return 'NO'
    return 'YES'