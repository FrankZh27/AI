#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:36:20 2018

@author: jiaweizhong
"""

import rp
import math

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
    def __init__(self):
        self.size = 0
        self.stack = list()
    
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
        
class PriorityQueue:
    def __init__(self):
        self.size = 0
        self.pq = list()
        return
    
    def offer(self, node):
        if self.size == 0:
            self.pq.append(node)
            self.size = self.size + 1
        else:
            i = 0
            while (i < self.size and
                (self.pq[i].cost+self.pq[i].heu) < (node.cost+node.heu)):
                i = i + 1
            self.pq.insert(i, node)
            self.size = self.size + 1
        return
    
    def pop(self):
        node = self.pq.pop(0)
        self.size = self.size - 1
        return node
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        
        
        
        
        
def Breadth_First_Search(init, goal):
    nodes = rp.build_graph()
    initNode = nodes.get(init)
    goalNode = nodes.get(goal)
    frontier = Queue()
    frontier.offer(initNode)
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    
    if initNode.name == goalNode.name:
        print('Number of nodes expanded:', node_expended)
        print('Solution path', goal)
        print('Solution cost', path_cost)
        return
    
    isGoal = False
    ite = 0
    while not frontier.isEmpty():
        ite = ite + 1
        if ite > 20:
            break
        if isGoal:
            break
        parentNode = frontier.pop()
        node_expended = node_expended + 1
        for i in range(0, len(parentNode.neighbors)):
            childNode = nodes.get(parentNode.neighbors[i].destination)
            childNode.parent = parentNode
            frontier.offer(childNode)
            if childNode.name == goal:
                isGoal = True
                break
    if isGoal:
        node = goalNode
        while node.name != init:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of nodes expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of nodes expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

def Depth_First_Search(init, goal):
    nodes = rp.build_graph()
    initNode = nodes.get(init)
    goalNode = nodes.get(goal)
    frontier = Stack()
    frontier.push(initNode)
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    if initNode.name == goalNode.name:
        print('Number of nodes expanded:', node_expended)
        print('Solution path', goal)
        print('Solution cost', path_cost)
        return
    
    isGoal = False
    while not frontier.isEmpty():
        if isGoal:
            break
        parentNode = frontier.pop()
        node_expended = node_expended + 1
        for i in range(0, len(parentNode.neighbors)):
            childNode = nodes.get(parentNode.neighbors[i].destination)
            childNode.parent = parentNode
            childNode.depth = parentNode.depth + 1
            if childNode.depth <= 10:
                frontier.push(childNode)
            if childNode.name == goal:
                isGoal = True
                break
    if isGoal:
        node = goalNode
        while node.name != init:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of nodes expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of nodes expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

def Iterative_Deepening_DFS(init, goal):
    nodes = rp.build_graph()
    initNode = nodes.get(init)
    goalNode = nodes.get(goal)
    frontier = Stack()
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    if initNode.name == goalNode.name:
        print('Number of nodes expanded:', node_expended)
        print('Solution path', goal)
        print('Solution cost', path_cost)
        return
    
    isGoal = False
    iteDepth = 0
    while not isGoal:
        frontier.push(initNode)
        initNode.depth = 0
        node_expended = 0
        while not frontier.isEmpty():
            if isGoal:
                break
            parentNode = frontier.pop()
            node_expended = node_expended + 1
            for i in range(0, len(parentNode.neighbors)):
                childNode = nodes.get(parentNode.neighbors[i].destination)
                childNode.parent = parentNode
                childNode.depth = parentNode.depth + 1
                if childNode.depth <= iteDepth:
                    frontier.push(childNode)
                if childNode.name == goal:
                    isGoal = True
                    break
        iteDepth = iteDepth + 1
    if isGoal:
        node = goalNode
        while node.name != init:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of nodes expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of nodes expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

def Uniform_Cost_Search(init, goal):
    nodes = rp.build_graph()
    initNode = nodes.get(init)
    initNode.cost = 0.0
    goalNode = nodes.get(goal)
    frontier = PriorityQueue()
    frontier.offer(initNode)
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    closeList = {}
    
    if initNode.name == goalNode.name:
        print('Number of nodes expanded:', node_expended)
        print('Solution path', goal)
        print('Solution cost', path_cost)
        return
    
    isGoal = False
    ite = 0
    while not frontier.isEmpty():
        ite = ite + 1
        if ite > 20:
            break
        if isGoal:
            break
        parentNode = frontier.pop()
        closeList[parentNode.name] = parentNode
        node_expended = node_expended + 1
        if parentNode.name == goalNode.name:
            isGoal = True
            break
        
        for i in range(len(parentNode.neighbors)):
            childNode = nodes.get(parentNode.neighbors[i].destination)
            if not childNode.name in closeList:
                frontier.offer(childNode)
                currCost = parentNode.neighbors[i].distance + parentNode.cost
                if currCost < childNode.cost:
                    childNode.cost = currCost
                    childNode.parent = parentNode
            
    if isGoal:
        node = goalNode
        while node.name != init:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of nodes expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of nodes expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

def A_Star_Search(init, goal):
    R = 3959
    nodes = rp.build_graph()
    initNode = nodes.get(init)
    initNode.cost = 0.0
    goalNode = nodes.get(goal)
    phi_init = initNode.lat*math.pi/180
    theta_init = initNode.lon*math.pi/180
    init_x = math.cos(phi_init) * math.cos(theta_init) * R
    init_y = math.cos(phi_init) * math.sin(theta_init) * R
    init_z = math.sin(phi_init) * R
    
    phi_goal = goalNode.lat*math.pi/180
    theta_goal = goalNode.lon*math.pi/180
    goal_x = math.cos(phi_goal) * math.cos(theta_goal) * R
    goal_y = math.cos(phi_goal) * math.sin(theta_goal) * R
    goal_z = math.sin(phi_goal) * R
    
    heu = math.sqrt(math.pow(goal_x-init_x,2)
        +math.pow(goal_y-init_y,2)+math.pow(goal_z-init_z,2))
    initNode.heu = heu
    
    frontier = PriorityQueue()
    frontier.offer(initNode)
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    closeList = {}
    
    if initNode.name == goalNode.name:
        print('Number of nodes expanded:', node_expended)
        print('Solution path', goal)
        print('Solution cost', path_cost)
        return
    
    isGoal = False
    ite = 0
    while not frontier.isEmpty():
        ite = ite + 1
        if ite > 20:
            break
        if isGoal:
            break
        parentNode = frontier.pop()
        closeList[parentNode.name] = parentNode
        node_expended = node_expended + 1
        if parentNode.name == goalNode.name:
            isGoal = True
            break
        
        for i in range(len(parentNode.neighbors)):
            childNode = nodes.get(parentNode.neighbors[i].destination)
            if not childNode.name in closeList:
                frontier.offer(childNode)
                currCost = parentNode.neighbors[i].distance + parentNode.cost
                if currCost < childNode.cost:
                    childNode.cost = currCost
                    childNode.parent = parentNode
            
    if isGoal:
        node = goalNode
        while node.name != init:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of nodes expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of nodes expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

filename = 'route.txt'
# filename = 'tsp.txt'

commands = list()

for line in open(filename):
    commands.append(line.strip())
    
Uniform_Cost_Search('Ann Arbor', 'Detroit')