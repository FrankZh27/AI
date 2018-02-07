#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:12:32 2018

@author: jiaweizhong
"""
import math
# build_graph function can build the graph
class Edge:
    def __init__(self, na, di):
        self.destination = na
        self.distance = di
        
class Node:
    def __init__(self, num):
        self.tag = num
        self.name = ""
        self.parent = "null"
        self.state = "null"
        self.neighbors = list()
        self.depth = 0
        self.heu = 0
        self.cost = float("inf")
        self.lat = 0.0
        self.lon = 0.0
        self.visited = set()

class State:
    def __init__(self, na):
        self.name = na
        self.neighbors = list()
        self.depth = "null"
        self.heu = 0
        self.cost = float("inf")
        self.lat = 0.0
        self.lon = 0.0
        self.visited = set()
        
class Vertex:
    def __init__(self, na):
        self.name = na
        self.parent = "null"
        self.name = na
        self.neighbors = list()
        self.depth = "null"
        self.heu = 0
        self.cost = float("inf")
        self.lat = 0.0
        self.lon = 0.0
        
def cal_heu(initNode, goalNode):
    R = 3959
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
    return heu   

def build_graph():
    f = open("michigan_graph.txt")
    #arr = []
    vertices = {}
    for line in f.readlines():
        line = line.strip()
        temp = line.split(", ")
        if not temp[0] in vertices:
            edge = Edge(temp[1], float(temp[2]))
            vertex = Vertex(temp[0])
            vertex.neighbors.append(edge)
            vertices[temp[0]] = vertex
        else:
            edge = Edge(temp[1], float(temp[2]))
            vertices.get(temp[0]).neighbors.append(edge)
        if not temp[1] in vertices:
            edge = Edge(temp[0], float(temp[2]))
            vertex = Vertex(temp[1])
            vertex.neighbors.append(edge)
            vertices[temp[1]] = vertex
        else:
            edge = Edge(temp[0], float(temp[2]))
            vertices.get(temp[1]).neighbors.append(edge)
            
        #arr.append(temp)
    f.close()
    
    f = open("michigan_cor.txt")
    for line in f.readlines():
        line = line.strip()
        temp = line.split(", ")
        vertices.get(temp[0]).lat = float(temp[1])
        vertices.get(temp[0]).lon = float(temp[2])
    f.close()
    
    return vertices

vertices = build_graph()