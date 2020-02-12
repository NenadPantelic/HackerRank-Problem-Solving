#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:47:11 2020

@author: nenad
"""
MAXX_EL = 201
freq = [0] * MAXX_EL
def counting_sort_and_median(n):
    #global freq
    count_freq = freq[:]
    
    for i in range(1, MAXX_EL):
        count_freq[i] += count_freq[i-1]
    start = end = 0
    
    i = 0
    # median - middle element and element next to him 
    if n % 2 == 0:
        start = n // 2
        end = start + 1
    # middle element
    else:
        start = n//2 + 1
        end = start
    
    # find first element that makes median - search for element that holds position >= than start
    # e.g. start = 2 (n is even) , we 're seeking for second element in ordering, so it's counting value
    # shoulld be at least 2
    while i < MAXX_EL:
        if start <= count_freq[i]:
            start = i
            break
        i += 1
   # continue from the same position (where we found a), and search for b - it can happen that both of values
   # are the same - e.g. 2 4 in counting array (e.g. start =3, then end is 3 or 4 (depends if n is even or odd))
    while i < MAXX_EL:
        if end <= count_freq[i]:
            end = i
            break
        i += 1
    # double value of median
    return start + end

    
def activity_notifications(expenditure, d):
    global freq
    notification_no = 0

    # first d positions
    for i in range(d):    
        freq[expenditure[i]] += 1
    for i in range(d, len(expenditure)):
        # previous d values
        median = counting_sort_and_median(d)
        if expenditure[i] >= median:
            notification_no += 1
        # update counts
        freq[expenditure[i]] += 1
        freq[expenditure[i-d]] -= 1

    return notification_no   

       
arr = [2,3,4,2,3,6,8,4,5]
d = 5

#arr = [1,2,3,4,4]
# = 4

arr = list(range(10, 51, 10))
d = 3


#d = 10000
#arr = list(map(int, input().split()))
print(activity_notifications(arr, d))