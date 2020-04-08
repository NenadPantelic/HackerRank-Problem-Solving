#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:53:03 2020

@author: nenad
"""

def countNonZero(val):
    count = 0
    for c in val:
        if c != "0":
            count += 1
    return count

def acmTeam(topic):
    participants = len(topic)
    topicNo = len(topic[0])
    #topMap = defaultdict(int)
    topicMap = {i:0 for i in range(topicNo+1)}
    topic.sort()
    for i in range(participants-1):
        for j in range(i+1, participants):
            val = countNonZero(str(int(topic[i]) + int(topic[j])))
            topicMap[val] += 1
    for i in range(topicNo, -1,-1):
        if topicMap[i]:
            return (i, topicMap[i])
   
        
    
topics = ["10101", "11100", "11010", "00101"]
print(acmTeam(topics))

topics = ["100", "010", "001"]
print(acmTeam(topics))
                
                
            
            
        
        