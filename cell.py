#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:00:57 2018
Note: Run in Python verison other than 2.7.5 may cause unexpected problems
@author: Jiawei Zhong
"""

import random

# Get user input
cellNum = int(input("Pliease enter the number of cells: "))
gens = int(input("Please enter the number of generations: "))

# Genrate the random string list
cell = []
cell.append('.')
print(cell[0]),
for i in range(0, cellNum-2):
    if (random.randint(0,1) == 0):
        cell.append('.')
        print(cell[i+1]),
    else:
        cell.append('*')
        print(cell[i+1]),
cell.append('.')
print(cell[cellNum-1])

# Generate all of the generations
# Use two array to generate the next array dynamically
isOdd = True;
cell_2 = ['.']*cellNum
cell_2[0] = '.'
cell_2[cellNum-1] = '.'

for i in range(1, gens+1):
    for j in range(1, cellNum-1):
        if isOdd:
            if cell[j] == '.' and ((cell[j-1] == '*' and cell[j+1] == '.' ) or (cell[j-1] == '.' and cell[j+1] == '*')):
                cell_2[j] = '*'
            else:
                cell_2[j] = '.'
        else:
            if cell_2[j] == '.' and ((cell_2[j-1] == '*' and cell_2[j+1] == '.') or (cell_2[j-1] == '.' and cell_2[j+1] == '*')):
                cell[j] = '*'
            else:
                cell[j] = '.'
    if isOdd:
        for k in range(0, cellNum-1):
            print(cell_2[k]),
        print(cell_2[k+1])
    else:
        for k in range(0, cellNum-1):
            print(cell[k]),
        print(cell[k+1])
    isOdd = not isOdd