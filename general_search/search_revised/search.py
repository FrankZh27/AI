#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:11:31 2018

@author: jiaweizhong
"""

import tsp as domain
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
        
class LinkedNode:
    def __init__(self):
        self.val = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.curr = LinkedNode()
    
    def append(self, node):
        newNode = LinkedNode()
        newNode.val = node
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            print(self.head)
        else:
            if self.size == 1:
                print(self.head)
                self.head.next = newNode
                self.tail = newNode
            else:
                self.tail = newNode
        self.size = self.size + 1
        
        return
    
    def get(self, i):
        newNode = LinkedNode()
        newNode.next = self.head
        if i == 0:
            return self.head.val
        
        if i == 1:
            return self.head.next.val
        
        for x in range(0,i):
            newNode.next = newNode.next.next
        return newNode.next.val
        
    def insert(self, i, node):
        newNode = LinkedNode()
        newNode.val = node
        self.size = self.size + 1
        if i == self.size:
            self.append(node)
            return
        
        if i == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = self.head
            for x in range(0,i-1):
                newNode.next = newNode.next.next
            preNode = LinkedNode()
            preNode = newNode.next
            newNode.next = newNode.next.next
            preNode.next = newNode
        return
    
    def pop(self):
        node = self.head.val
        self.head = self.head.next
        return node
        
        
class PriorityQueue:
    def __init__(self):
        self.size = 0
        self.pq = LinkedList()
        return
    
    def offer(self, node):
        if self.size == 0:
            self.pq.append(node)
            self.size = self.size + 1
        else:
            i = 0
            while (i < self.size and
                (self.pq.get(i).cost+self.pq.get(i).heu) < (node.cost+node.heu)):
                i = i + 1
            self.pq.insert(i, node)
            self.size = self.size + 1
        return
    
    def pop(self):
        node = self.pq.pop()
        self.size = self.size - 1
        return node
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def isContain(self, node):
        for i in range(self.size):
            if node.name == self.pq[i].name:
                return True
        return False

        
def Breadth_First_Search(init, goal, vertices):
    initNode = domain.Node(0)
    initNode.name = list(init)[0]
    initNode.neighbors = vertices.get(initNode.name).neighbors
    initNode.visited.add(initNode.name)
    goalNode = domain.Node("inf")
    frontier = Queue()
    frontier.offer(initNode)
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    
    if len(init) == len(goal):
        print('Number of vertices expanded:', node_expended)
        print('Solution path', list(init)[0])
        print('Solution cost', path_cost)
        return

    isGoal = False
    ite = 0
    nodeId = 1
    while not frontier.isEmpty():
        ite = ite + 1
        if ite > 200000000:
            break
        if isGoal:
            break
        parentNode = frontier.pop()
        node_expended = node_expended + 1
        for i in range(0, len(parentNode.neighbors)):
            childNode = domain.Node(nodeId)
            nodeId = nodeId + 1
            print(nodeId)
            childNode.name = parentNode.neighbors[i].destination
            childNode.parent = parentNode
            childNode.neighbors = vertices.get(childNode.name).neighbors
            s = set(parentNode.visited)
            s.add(childNode.name)
            childNode.visited = s
            frontier.offer(childNode)
            print(childNode.visited)
            if len(childNode.visited) == len(goal):
                isGoal = True
                goalNode = childNode
                break
    if isGoal:
        node = goalNode
        while node.tag != 0:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of vertices expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of vertices expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

def Depth_First_Search(init, goal, vertices):
    initNode = domain.Node(0)
    initNode.name = list(init)[0]
    initNode.neighbors = vertices.get(initNode.name).neighbors
    initNode.visited.add(initNode.name)
    goalNode = domain.Node("inf")
    frontier = Stack()
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    
    if len(init) == len(goal):
        print('Number of vertices expanded:', node_expended)
        print('Solution path', list(init)[0])
        print('Solution cost', path_cost)
        return

    isGoal = False
    iteDepth = 10
    nodeId = 1
    frontier.push(initNode)
    initNode.depth = 0
    node_expended = 0
    while not frontier.isEmpty():
        if isGoal:
            break
        parentNode = frontier.pop()
        node_expended = node_expended + 1
        for i in range(0, len(parentNode.neighbors)):
            childNode = domain.Node(nodeId)
            nodeId = nodeId + 1
            print(nodeId)
            childNode.name = parentNode.neighbors[i].destination
            childNode.parent = parentNode
            childNode.neighbors = vertices.get(childNode.name).neighbors
            s = set(parentNode.visited)
            s.add(childNode.name)
            childNode.visited = s
            childNode.depth = parentNode.depth + 1
            print(childNode.visited)
            if childNode.depth <= iteDepth:
                frontier.push(childNode)
            if len(childNode.visited) == len(goal):
                isGoal = True
                goalNode = childNode
                break
    if isGoal:
        node = goalNode
        while node.tag != 0:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of vertices expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of vertices expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

def Iterative_Deepening_DFS(init, goal, vertices):
    initNode = domain.Node(0)
    initNode.name = list(init)[0]
    initNode.neighbors = vertices.get(initNode.name).neighbors
    initNode.visited.add(initNode.name)
    goalNode = domain.Node("inf")
    frontier = Stack()
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    
    if len(init) == len(goal):
        print('Number of vertices expanded:', node_expended)
        print('Solution path', list(init)[0])
        print('Solution cost', path_cost)
        return

    isGoal = False
    iteDepth = 0
    nodeId = 1
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
                childNode = domain.Node(nodeId)
                nodeId = nodeId + 1
                print(nodeId)
                childNode.name = parentNode.neighbors[i].destination
                childNode.parent = parentNode
                childNode.neighbors = vertices.get(childNode.name).neighbors
                s = set(parentNode.visited)
                s.add(childNode.name)
                childNode.visited = s
                childNode.depth = parentNode.depth + 1
                print(childNode.visited)
                if childNode.depth <= iteDepth:
                    frontier.push(childNode)
                if len(childNode.visited) == len(goal):
                    isGoal = True
                    goalNode = childNode
                    break
        iteDepth = iteDepth + 1
    if isGoal:
        node = goalNode
        while node.tag != 0:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of vertices expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of vertices expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

def Uniform_Cost_Search(init, goal):
    initNode = domain.Node(0)
    initNode.name = list(init)[0]
    initNode.neighbors = vertices.get(initNode.name).neighbors
    initNode.visited.add(initNode.name)
    initNode.cost = 0.0
    goalNode = domain.Node("inf")
    frontier = PriorityQueue()
    frontier.offer(initNode)
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    
    if len(init) == len(goal):
        print('Number of vertices expanded:', node_expended)
        print('Solution path', list(init)[0])
        print('Solution cost', path_cost)
        return

    isGoal = False
    ite = 0
    nodeId = 1
    while not frontier.isEmpty():
        ite = ite + 1
        if ite > 2000000:
            break

        parentNode = frontier.pop()
        node_expended = node_expended + 1
        print(parentNode.cost)
        
        if len(parentNode.visited) == len(goal):
            isGoal = True
            break
        for i in range(len(parentNode.neighbors)):
            childNode = domain.Node(nodeId)
            nodeId = nodeId + 1
            print(nodeId)
            childNode.name = parentNode.neighbors[i].destination
            childNode.parent = parentNode
            childNode.neighbors = vertices.get(childNode.name).neighbors
            currCost = parentNode.neighbors[i].distance + parentNode.cost
            childNode.cost = currCost
            s = set(parentNode.visited)
            s.add(childNode.name)
            childNode.visited = s
            
            frontier.offer(childNode)
            print(childNode.visited)

    if isGoal:
        node = goalNode
        while node.tag != 0:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of vertices expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of vertices expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

def A_Star_Search(init, goal):
    initNode = domain.Node(0)
    initNode.name = list(init)[0]
    initNode.neighbors = vertices.get(initNode.name).neighbors
    initNode.visited.add(initNode.name)
    initNode.cost = 0.0
    goalNode = domain.Node("inf")
    frontier = PriorityQueue()
    frontier.offer(initNode)
    path_cost = 0.0
    node_expended = 0
    path = Stack()
    
    
    li = list(goal)
    
    if len(init) == len(goal):
        print('Number of vertices expanded:', node_expended)
        print('Solution path', list(init)[0])
        print('Solution cost', path_cost)
        return

    isGoal = False
    ite = 0
    nodeId = 1
    while not frontier.isEmpty():
        ite = ite + 1
        if ite > 2000000:
            break

        parentNode = frontier.pop()
        node_expended = node_expended + 1
        print(parentNode.cost)
        
        if len(parentNode.visited) == len(goal):
            isGoal = True
            goalNode = parentNode
            break
        for i in range(len(parentNode.neighbors)):
            childNode = domain.Node(nodeId)
            nodeId = nodeId + 1
            print(nodeId)
            childNode.name = parentNode.neighbors[i].destination
            childNode.parent = parentNode
            childNode.neighbors = vertices.get(childNode.name).neighbors
            currCost = parentNode.neighbors[i].distance + parentNode.cost
            childNode.cost = currCost
            s = set(parentNode.visited)
            s.add(childNode.name)
            childNode.visited = s
            
            for j in range(len(goal)):
                if not li[j] in s:
                    childNode.heu = (childNode.heu 
                    + domain.cal_heu(vertices.get(childNode.name), vertices.get(li[j])))
                    break
            frontier.offer(childNode)
            print(childNode.visited)

    if isGoal:
        node = goalNode
        while node.tag != 0:
            path.push(node.name)
            stepCost = 0.0
            for x in range(len(node.neighbors)):
                if node.neighbors[x].destination == node.parent.name:
                    stepCost = node.neighbors[x].distance
                    break
            path_cost = path_cost + stepCost
            node = node.parent
        path.push(node.name)
        print('Number of vertices expanded:', node_expended)
        print('Solution path', path.stack)
        print('Solution cost', path_cost)
    else:
        print('Number of vertices expanded:', node_expended)
        print('Solution path: There is no solution')
        print('Solution cost', path_cost)
    return

# filename = 'route.txt'
filename = 'tsp.txt'

commands = list()

for line in open(filename):
    commands.append(line.strip())
if len(commands) == 3:    
    if commands[2] == 'B':
        Breadth_First_Search(commands[0], commands[1])
    elif commands[2] == 'D':
        Depth_First_Search(commands[0], commands[1])
    elif commands[2] == 'I':
        Iterative_Deepening_DFS(commands[0], commands[1])
    elif commands[2] == 'U':
        Uniform_Cost_Search(commands[0], commands[1])
    else:
        A_Star_Search(commands[0], commands[1])
else:
    vertices = domain.build_graph()
    goal = set(vertices)
    init = set()
    init.add(commands[0])
    if commands[1] == 'B':
        Breadth_First_Search(init, goal, vertices)
    elif commands[1] == 'D':
        Depth_First_Search(init, goal, vertices)
    elif commands[1] == 'I':
        Iterative_Deepening_DFS(init, goal, vertices)
    elif commands[1] == 'U':
        Uniform_Cost_Search(init, goal)
    else:
        A_Star_Search(init, goal)