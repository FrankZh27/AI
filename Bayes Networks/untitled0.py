#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 19:04:50 2018

@author: jiaweizhong
"""

import queue

# Read bn.txt and build the bayes net
def build_bn():
    """build bayes net"""
    bayesnet = {}
    edges = []
    file = open("bn.txt")
    line = file.readline()
    line = file.readline()
    line = line.strip()
    nodes = line.split(", ")
    for node in nodes:
        bayesnet[node] = [[], {}]

    line = file.readline()
    line = file.readline()
    while line[0] != "%":
        line = line.strip()
        line = line.split(", ")
        edges.append(line)
        line = file.readline()

    # call topological function to get varss
    varss = topological_sort(nodes, edges)

    line = file.readline()
    while line:
        line = line.strip().split("|")
        if len(line) == 1:
            temp_line = line[0].split("(")[1].split(")")
            node = temp_line[0].split("=")[0]
            prob = temp_line[1].split("=")[1]
            bayesnet[node][1][None] = prob
        else:
            temp_line = line[0].split("(")[1].split(")")
            node = temp_line[0].split("=")[0]
            temp_line = line[1].split(")")[0].split(",")
            num = line[1].split(")")[1].split("=")[1]
            temp_parent = []
            temp_bool = ()
            for temp in temp_line:
                curr_parent = temp.split("=")[0]
                if temp.split("=")[1] == "T":
                    tup = (True, )
                else:
                    tup = (False, )
                temp_bool = temp_bool + tup
                temp_parent.append(curr_parent)

            bayesnet[node][1][temp_bool] = num
            if len(bayesnet[node][0]) == 0:
                bayesnet[node][0] = temp_parent
        line = file.readline()
    file.close()
    return bayesnet, varss

def topological_sort(nodes, edges):
    """Use topological sort to get the node order"""
    indegree = {}
    sort_list = []
    for node in nodes:
        indegree[node] = 0

    for edge in edges:
        indegree[edge[1]] += 1

    que = queue.Queue()
    for node in nodes:
        if indegree[node] == 0:
            que.put(node)

    while not que.empty():
        curr_node = que.get()
        sort_list.append(curr_node)
        for edge in edges:
            if edge[0] == curr_node:
                indegree[edge[1]] -= 1
                if indegree[edge[1]] == 0:
                    que.put(edge[1])

    return sort_list[::-1]

def input_query():
    """readin input.txt and get the query information"""
    file = open("input.txt")
    line = file.readline()
    temp = line.strip().split("=")
    if temp[1][0] == "T":
        booleanval = True
    else:
        booleanval = False

    line = file.readline()
    variable = line.strip()
    evidence = {}
    line = file.readline()
    line = file.readline()
    str1 = line.strip().split(", ")
    for evi in str1:
        temp = evi.split("=")
        if temp[1] == "T":
            evidence[temp[0]] = True
        else:
            evidence[temp[0]] = False
    file.close()
    return variable, booleanval, evidence

def enumeration_ask(variable, evidence, bayesnet, varss):
    """this function is used to query something"""
    query = {}
    for bool_val in [True, False]:
        evidence[variable] = bool_val
        query[bool_val] = enumerate_all(varss, evidence, bayesnet)
        del evidence[variable]
    return normalize(query)

def enumerate_all(varss, evidence, bayesnet):
    """calculate the total probability"""
    if len(varss) == 0:
        return 1.0
    variable = varss.pop()
    if variable in evidence:
        val = probability(variable, evidence[variable], evidence, bayesnet)\
        * enumerate_all(varss, evidence, bayesnet)
        varss.append(variable)
        return val
    total = 0
    evidence[variable] = True
    total += probability(variable, True, evidence, bayesnet)\
    * enumerate_all(varss, evidence, bayesnet)
    evidence[variable] = False
    total += probability(variable, False, evidence, bayesnet)\
    * enumerate_all(varss, evidence, bayesnet)
    del evidence[variable]
    varss.append(variable)
    return total

def normalize(query):
    """used for normalize the probability in conditional probability"""
    total = 0.0
    for val in query.values():
        total += val
    for key in query.keys():
        query[key] = query[key] / total
    return query

def probability(variable, value, evidence, bayesnet):
    """find the conditional probability in CPT"""
    parents = bayesnet[variable][0]
    if len(parents) == 0:
        probability_true = bayesnet[variable][1][None]
    else:
        parent_values = [evidence[parent] for parent in parents]
        probability_true = bayesnet[variable][1][tuple(parent_values)]
    if value:
        return float(probability_true)
    return 1.0 - float(probability_true)

def main():
    """main function"""
    bayesnet, varss = build_bn()
    variable, booleanval, evidence = input_query()
    total = enumeration_ask(variable, evidence, bayesnet, varss)
    print(total[booleanval])

if __name__ == "__main__":
    main()
