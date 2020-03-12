#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:22:21 2020

@author: nenad
"""

from collections import deque
def pickingNumbers(a):
    # Write your code here
    a.sort()
    n = len(a)
    # queue of possibly starting element of next subarray
    q = deque()
    # start position of the current subarray
    start_pos = 0
    # state of comparison - 0 (previous and current element are the same), 1 - this element is greater than previous one
    prev = 0
    # default value
    maxlen =  1
    i = 1
    while i < n:
        diff = a[i] - a[i-1]
        # breaks the subarray, constraint violation
        if diff > 1:
            prev = 1
            # update max counter
            maxlen = max(maxlen, i-start_pos)
            # determine element that can be new subarray  starting element
            while len(q):
                val = q.popleft()
                # follows the constraint
                if a[i] - a[val] < 2:
                    start_pos = val
            # there is no element that follows the constraint, so current element is also starting element
            # of new subarray
            else:
                start_pos = i
                # reset the state
                prev = 0
        # go further - everyithing is ok 
        elif diff == 0:
            pass
        else:
            # check two cases - 1 2 2 (OK) and 1 2 3 (NOT OK)
            # add this element to queue for later check (it can be starting element of new subarray)
            q.append(i)
            # previous state shows that prepredecessor is the same as predecessor, so constraint is not violated
            if prev == 0:
                prev = 1
                pass
            else:
                # constraint is violated - search for new starting position
                # update max counter
                maxlen = max(maxlen, i-start_pos)
                while len(q):
                    val = q.popleft()
                    if a[i] - a[val] < 2:
                        start_pos = val
                else:
                    start_pos = i
                    prev = 0
        i += 1   
    maxlen = max(maxlen, i-start_pos)
    return maxlen


# Test 1
a = [1,1,2,2,4,4,5,5,5]
print(pickingNumbers(a))

# Test 2
a = [4,6, 5, 3, 3, 1]
print(pickingNumbers(a))

# Test 3
a = [1,2,2,3,1,2,4,4,4,3,3]
print(pickingNumbers(a))
        