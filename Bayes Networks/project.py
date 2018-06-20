# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import queue

# Read bn.txt and build the bayes net
def build_bn():
    bn = {}
    edges = []
    
    file = open("bn.txt")
    line = file.readline()
    line = file.readline()
    line = line.strip()
    nodes = line.split(", ")
    for node in nodes:
        bn[node] = [[],[],[]];

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
            temp_line = line[0].split('(')[1].split(')')
            print(temp_line)
            node = temp_line[0].split('=')[0]
            prob = temp_line[1].split('=')[1]
            bn[node] = [[],[prob],[]]
            print(bn)
        else:
            temp_line = line[0].split('(')[1].split(')')
            node = temp_line[0].split('=')[0]
            temp_line = line[1].split(')')[0].split(',')
            num = line[1].split(')')[1].split('=')[1]
            temp_parent = ""
            temp_bool = ""
            print(temp_line)
            for temp in temp_line:
                ba = temp.split('=')[0]
                bb = temp.split('=')[1]
                temp_parent += ba
                temp_bool += bb
            bn[node][0].append(temp_bool)
            bn[node][1].append(num)
            bn[node][2].append(temp_parent)
        line = file.readline()
    file.close()
    
    return bn, varss

def topological_sort(nodes, edges):
    indegree = {}
    sort_list = []
    for node in nodes:
        indegree[node] = 0
    
    for edge in edges:
        indegree[edge[1]] += 1
    
    que = queue.Queue()
    for node in nodes:
        if (indegree[node] == 0):
            que.put(node)
    
    while (not que.empty()):
        curr_node = que.get()
        sort_list.append(curr_node)
        for edge in edges:
            if edge[0] == curr_node:
                indegree[edge[1]] -= 1
                if indegree[edge[1]] == 0:
                    que.put(edge[1])
    
    return sort_list

def input_query():
    file = open("input.txt")
    line = file.readline()
    temp = line.strip().split("=")
    if (temp[1][0] == "T"):
        booleanval = True
    else:
        booleanval = False
    
    line = file.readline()
    variable = line.strip()
    
    print(variable)
    
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

def enumeration_ask(X, e, bn,varss):
    QX = {}
    for xi in [True, False]:
        e[X] = xi
        QX[xi] = enumerate_all(varss, e, bn)
        del e[X]
    return normalize(QX)

def enumerate_all(varss, e, bn):
    if len(varss) == 0:
        return 1.0
    Y = varss.pop()
    if Y in e:
        val = Pr(Y,e[Y],e,bn) * enumerate_all(varss,e,bn)
        varss.append(Y)
        return val
    else:
        total = 0
        e[Y] = True
        total += Pr(Y,True,e,bn) * enumerate_all(varss,e,bn)
        e[Y] = False
        total += Pr(Y,False,e,bn) * enumerate_all(varss,e,bn)
        del e[Y]
        varss.append(Y)
        return total

def normalize(QX):
    total = 0.0
    for val in QX.values():
        total += val
    for key in QX.keys():
        QX[key] /= total
    return QX

def Pr(var, val, e, bn):
    parents = bn[var][0]
    if len(parents) == 0:
        truePr = bn[var][1][None]
    else:
        parentVals = [e[parent] for parent in parents]
        truePr = bn[var][1][tuple(parentVals)]
    if val==True: return truePr
    else: return 1.0-truePr

def main():
    bn, varss = build_bn()
    variable, booleanval, evidence = input_query()
    total = enumeration_ask(variable, evidence, bn, varss)
    print(total)

if __name__ == "__main__":
    main()
