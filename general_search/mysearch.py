#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:36:20 2018

@author: jiaweizhong
"""

#import rp as rp

# slef-def class
class Queue:
    size = 0
    queue = list()
    
    def offer(self, node):
        self.queue.append(node)
        self.size = self.size + 1
        return
        
    def pop(self):
        node = self.queue.pop(0)
        self.size = self.size - 1
        return node
        
    def getSize(self):
        return self.size;
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

class Stack:
    size = 0
    stack = list()
    
    def push(self, node):
        self.stack.insert(0, node)
        self.size = self.size + 1
        return
    
    def pop(self):
        node = self.stack.pop(0)
        self.size = self.size - 1
        return node
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        
def Breadth_First_Search(inti, goal):
    frontier = Queue()
    frontier.offer(inti)
    path_cost = 0
    node_expended = 0
    path = list()
    path.append(goal.state)
    
    if inti.state == goal.state:
        return(node_expended, goal.state, path_cost)
    
    while not frontier.isEmpty():
        parent = frontier.pop()
        

filename = 'route.txt'
# filename = 'tsp.txt'
commands = list()

for line in open(filename):
    commands.append(line.strip())