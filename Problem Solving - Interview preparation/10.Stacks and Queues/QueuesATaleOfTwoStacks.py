#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:19:02 2020

@author: nenad
"""

# stack - append and pop(-1)
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def transfer_data(self):
        if len(self.stack2) == 0:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop(-1))
    
    def peek(self):
        self.transfer_data()
        return self.stack2[-1]
        
    def pop(self):
        self.transfer_data()
        #return 
        self.stack2.pop(-1)
        
        
    def put(self, value):
        self.stack1.append(value) 
        
# Test 1
mq = MyQueue()
mq.put(42)       
mq.pop()
mq.put(14)       
print(mq.peek())
mq.put(28)       
print(mq.peek())
mq.put(60)       
mq.put(78)
mq.pop()
mq.pop()

