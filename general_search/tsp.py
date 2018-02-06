#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:12:32 2018

@author: jiaweizhong
"""

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