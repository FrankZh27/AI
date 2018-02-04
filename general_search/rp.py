#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 19:24:08 2018

@author: jiaweizhong
"""
class Edge:
    def __init__(self, na, di):
        self.destination = na
        self.distance = di
        
class Node:
    def __init__(self, na):
        self.name = na
        self.neighbors = list()
        self.lat = 0.0
        self.lon = 0.0

def build_graph():
    f = open("michigan_graph.txt")
    arr = []
    nodes = {}
    for line in f.readlines():
        line = line.strip()
        temp = line.split(", ")
        if not temp[0] in nodes:
            edge = Edge(temp[1], temp[2])
            node = Node(temp[0])
            node.neighbors.append(edge)
            nodes[temp[0]] = node
        else:
            edge = Edge(temp[1], temp[2])
            nodes.get(temp[0]).neighbors.append(edge)
        if not temp[1] in nodes:
            edge = Edge(temp[0], temp[2])
            node = Node(temp[1])
            node.neighbors.append(edge)
            nodes[temp[1]] = node
        else:
            edge = Edge(temp[0], temp[2])
            nodes.get(temp[1]).neighbors.append(edge)
            
        arr.append(temp)
    f.close()
    
    # Initialize an adjacent matrix and number of edges
    # matrix_adj = np.zeros([size, size], dtype = int)

    return nodes
