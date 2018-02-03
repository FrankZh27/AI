#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:36:20 2018

@author: jiaweizhong
"""

class Queue:
    size = 0
    queue = list()
    def insert(self, node):
        self.queue.append(node)
        
    

filename = 'route.txt'
# filename = 'tsp.txt'
commands = list()

for line in open(filename):
    commands.append(line.strip())