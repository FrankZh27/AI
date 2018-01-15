#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:00:57 2018

@author: Jiawei Zhong
"""

import numpy as np

# Get user input
cellNum = int(input("Pliease enter the number of cells: "))
gens = int(input("Please enter the number of generations: "))

# Generate a random seeded array
cellBoolean = np.random.randint(2, size = cellNum-2)

# Genrate the parent string list
cell = []
cell.append('.')
for i in range(0, cellNum-2):
    if (cellBoolean[i] == 0):
        cell.append('.')
    else:
        cell.append('*')
cell.append('.')
print('Generation 1: ', cell)

# Generate all of the generations
# Use two array to generate the next array dynamically
isOdd = True;
cell_2 = np.zeros(cellNum, str)
cell_2[0] = '.'
cell_2[cellNum-1] = '.'

for i in range(1, gens):
    for j in range(1, cellNum-1):
        if isOdd:
            if cell[j] == '.' and (cell[j-1] == '*' or cell[j+1] == '*'):
                cell_2[j] = '*'
            else:
                cell_2[j] = '.'
        else:
            if cell_2[j] == '.' and (cell_2[j-1] == '*' or cell_2[j+1] == '*'):
                cell[j] = '*'
            else:
                cell[j] = '.'
    if isOdd:
        print('Generation', i+1,': ', cell_2)
    else:
        print('Generation', i+1,': ', cell)
    isOdd = not isOdd
