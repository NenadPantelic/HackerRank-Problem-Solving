#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:45:15 2020

@author: nenad
"""


from collections import OrderedDict
def solve(charms, generosities, n, k):
    #
    # Write your code here.
    #
    position_map = {}
    charms.sort(key=lambda x:sum(x)/len(x))
    generosities.sort(key=lambda x:sum(x)/len(x))
    #sum = [sum(arr) for arr in charms]
    student_visits = {}
    cum_visits = {}
    for i in range(len(charms)):
        charms[i].sort()
        for j in range(n):
            student_visits[i*n+j] = k
        cum_visits[i] = n*k
        
    best_sponsors = None
    most_charming = None
    gr_position = None
    fund = 0
    while len(generosities):

        # all charms used - but there is still tables to serve
        #charms.sort(key=lambda x:sum(x)/len(x))

        if len(charms) == 0:
            return -1
        #if most_charming == []:
        most_charming = charms[-1]
        if best_sponsors is None:
            best_sponsors = generosities[-1]
        # table cannot be served by one group
        if len(best_sponsors) > n * k:
            return -1
        if gr_position is None or cum_visits[gr_position] < len(best_sponsors):
            gr_position = len(charms)-1 
        while gr_position > -1 and cum_visits[gr_position] < len(best_sponsors):
            if charms[gr_position] == []:
                pass
            gr_position -= 1
        # there is no group that can serve this table
        if gr_position == -1:
            return -1
        else:
            most_charming = charms[gr_position]
        best_student = most_charming[-1]
        st_position = len(most_charming)-1
        
        visits_rem = student_visits[gr_position*n+st_position]
        while visits_rem and len(best_sponsors):
            fund += best_student * best_sponsors[-1]
            best_sponsors.pop(-1)
            visits_rem -= 1
            cum_visits[gr_position] -= 1
        #charms[gr_position] = most_charming
        student_visits[gr_position*n+st_position] = visits_rem
        if visits_rem == 0:
            most_charming.pop(-1)
            #sum[gr_position] -= best_student
            charms[gr_position] = most_charming
            if len(most_charming) == 0:
                most_charming = []
                #charms[gr_position] = mos
                gr_position = None
            
        
        if len(best_sponsors) == 0:
            generosities.pop(-1)
            best_sponsors = None
        charms.sort(key=lambda x:sum(x)/len(x) if len(x) else 0)
        #print(charms)

    #print(charms)
    return fund
        
        
        
# m = n = t = 3
# k = 1
# charms = [[1,2,3],[4,5,6],[7,8,9]]
# generosities = [[100,200],[500],[30,30]]    
# print(solve(charms,generosities,n,k))


# m = n = t = 3
# k = 3
# charms = [[1,2,3],[4,5,6],[7,8,9]]
# generosities = [[10,20, 30],[40,50,60],[70,80,90]]    
# print(solve(charms,generosities,n,k))


# m = n = t = 3
# k = 1
# charms = [[1,2,3],[4,5,6],[7,8,9]]
# generosities = [[200],[500,500],[30,30,30,30]]    
# print(solve(charms,generosities,n,k))


# m = n = t = 3
# k = 3
# charms = [[1,2,3],[4,5,6],[7,8,9]]
# generosities = [[200,200,200,200,200,200,200,200,200],[500,500],[30,30,30]]    
# print(solve(charms,generosities,n,k))         


m = 3
n = 3
t = 4 
charms = [[90,1,1],[80,1,1],[70,1,1]]    
generosities = [[1000],[1000],[1000],[1,1,1]]
k = 1 
print(solve(charms,generosities,n,k))         