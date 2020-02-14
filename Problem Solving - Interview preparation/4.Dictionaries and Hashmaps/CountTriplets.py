#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:15:30 2020

@author: nenad
"""
def read_file(path):
    f = open(path, 'r')
    items = list(map(int, f.read().split()))
    f.close()
    return items

def find_first_greater(arr, el):
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] > el:
            return i
        i += 1
    
    # mid = (low+high) // 2
    # if arr[mid] > el:
    #     # in prev step element was greater than mid element
    #     if sign in (1, None):
    #         return mid
    #     return find_first_greater(arr, el, low, mid, -1)
    # else:
    #     if sign in (-1, None):
    #         return mid+1
    #     return find_first_greater(arr, el, mid+1, high, 1)
    
    
# arr = [2,5,8,11,13]
# print(find_first_greater(arr, 3, 0, 4))
# print(find_first_greater(arr, 7, 0, 4))
# print(find_first_greater(arr, 6, 0, 4))
# print(find_first_greater(arr, 12, 0, 4))
#arr = [3]
#print(find_first_greater(arr, 2, 0, 0))


 
    
def count_triplets(arr, r):
    n = len(arr)
    #freq_dict = {}
    # holds positions of every element
    position_map = {}
    # contains index bounds for every element
    index_map = {}
    num_of_triplets = 0
    for i in range(n):
        val = arr[i]
        if val not in position_map:
            position_map[val] = []
            # first occurence, last occurence, num of occurence
            index_map[val] = [i,-1,0]
        position_map[val].append(i)
        index_map[val][1] = i
        index_map[val][2] += 1
       
    #print(position_map)
    #print(index_map)

    for i in range(n-2):
        val = arr[i]
        # second number in progression
        next_val = val * r
        positions_next = position_map.get(next_val, 0)
        if positions_next == 0:
            continue
        # third number in progression
        next_next_val = next_val * r
        positions_next_next = position_map.get(next_next_val, 0)
        if positions_next_next == 0:
            continue
        
        next_val_indices = index_map[next_val]
        next_next_val_indices = index_map[next_next_val]
        
        # case 1 - every index of second element in progression is greater than i
        if i < next_val_indices[0]:
            next_positions = position_map[next_val]
        # case 2 - j < i for all i,j
        elif i > next_val_indices[1]:
            continue
        else:
            #next_positions = positions_next[find_first_greater(positions_next, i, 0, next_val_indices[2]-1):]
            next_positions = positions_next[find_first_greater(positions_next, i):]
            #print(next_positions)
        for j in next_positions:
            #next_next_position = find_first_greater(positions_next_next, j, 0, next_next_val_indices[2]-1)
            next_next_position = find_first_greater(positions_next_next, j)
            if next_next_position is not None:
                num_of_triplets += next_next_val_indices[2] - next_next_position
           
    
    return int(num_of_triplets)

# Test 1
#print(count_triplets([1,2,2,4],2))

# Test 2
#print(count_triplets([1,3, 9, 9, 27, 81],3))


# Test 3
arr = [1] * 100
print(count_triplets(arr, 1))

# Test 4
arr = read_file('input06.txt')
print(count_triplets(arr, 3))
