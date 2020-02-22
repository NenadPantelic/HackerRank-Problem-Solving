#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:50:16 2020

@author: nenad
"""


# def largest_rectangle(arr):
#     n = len(arr)
#     maxx = 0
#     # go over lengths
#     for i in range(n):
#         # traverse over elements - make subarrays
#         for j in range(i, n):
#             #print(arr[j-i:j+1])
#             dist = min(arr[j-i:j+1]) * (i+1)
#             if dist > maxx:
#                 maxx = dist
#     return maxx


'''

Basically, we're going to start with building 1, then compute all of the areas of each rectangle and choose the maximum from that. Notice that when we start with building 1, we have no idea when the end of it's rectangle will be (represented by a dashed arrow going to the right). The next thing you should notice is that if the next building goes up (higher than the previous), all active areas will remain active (i.e. we still haven't found the end of the area).

When building 5 is added, it definitely ends the previous building's area (or whatever area it was part of) and, in this case, that's it. Also notice that we need to extend building 5 back through building 4. How do you know to stop at building 4? Easy, the next active area (coming from building 3) has a height lower than building 5's, so that area is still active (in other words it will go through building 5).

Hopefully you're starting to see how a stack can be used here: when the next building is taller than the previous, add it to the stack (to be processsed later). When the next building is shorter: pop off stack until you find a starting area with a smaller height (than the current building) or you empty the stack (meaning it goes all the way back through the first building). Now push this building's height along with it's left position onto the stack.

When you pop off the stack, this means you've found the right side of an area, so compute its area and see if it's the maximum. Also when you find the "left wall" for the current building (meaning you found a smaller building in the stack or went all the way back to the first building), you need to remember that position in addition to the height of the current building so that when the current building is eventually popped off of the stack, you can properly compute it's area. Notice how building 6 extends both backwards and forwards, such that when I get to building 8, I have to know that building 6's height extended all the way back through building 2.

'''
def largestRectangle(h):
    
    stack = []
    h.append(0)
    n = len(h)
    # base case - all building's heights is 1
    maxx = n-1
    
    for i in range(n):
        begin_index = i
        # check all previously visited taller buildings - areas of blocks that current building 
        # forms with them
        while len(stack) > 0 and stack[-1][0] >= h[i]:
            # get the last element from stack
            building = stack.pop()
            begin_index = building[1]
            height = building[0]
            # block made by current building
            block_height = (i + 1 - begin_index) * h[i]
            # previous building block
            prev_block_height = height * (i-begin_index)
            # check last visited building blocks formed with previous taller buildings (until you reach lower building than current one)
            maxx = max(maxx, block_height)
            maxx = max(maxx, prev_block_height)
        # case when current building is taller than previous one   
        stack.append((h[i], begin_index))
    return maxx
# Test 1
arr = [2,3,2]
print(largest_rectangle(arr))

# Test 2
arr = [1,2,3,4,5]
print(largest_rectangle(arr))


# Test 3
arr = [5,4,3,2,1]
print(largest_rectangle(arr))


# Test 4
arr = [1,3,5,7,6,2,4,1]
print(largest_rectangle(arr))