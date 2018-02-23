#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:08:54 2018

@author: jiaweizhong
"""
import csv
import copy

# Apply k consistency to (i,j) and return its domain
def k_consistency(sudoku, d, i, j):
    row = d[i][j]
    for k in range(9):
        if not k == j:
            if (not sudoku[i][k] == 0) and (sudoku[i][k] in row):  
                row.remove(sudoku[i][k])
    
    for k in range(9):
        if not k == i:
            if (not sudoku[k][j] == 0) and (sudoku[k][j] in row):
                row.remove(sudoku[k][j])
    
    grid_x = i//3*3
    grid_y = j//3*3
    
    for m in range(grid_x, grid_x+3):
        for n in range(grid_y, grid_y+3):
            if not(m == i and n == j):
                if (not sudoku[m][n] == 0) and (sudoku[m][n] in row):
                    row.remove(sudoku[m][n])
    
    return row

def find_mindomain(sudoku, d):
    minLen = 9
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 and len(d[i][j]) <= minLen:
                row = i
                col = j
                minLen = len(d[i][j])
    return minLen, row, col

def is_valid_insert(sudoku, element, row, col):
    for k in range(9):
        if not k == col:
            if sudoku[row][k] == element:
                return False
    
    for k in range(9):
        if not k == row:
            if sudoku[k][col] == element:
                return False
    
    grid_x = i//3*3
    grid_y = j//3*3
    
    for m in range(grid_x, grid_x+3):
        for n in range(grid_y, grid_y+3):
            if not(m == i and n == j):
                if sudoku[m][n] == element:
                    return False
    return True

def easy_fill(sudoku, d, remain):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 and len(d[i][j]) == 1:
                s = list(d[i][j])
                if is_valid_insert(sudoku, s[0], i, j):
                    sudoku[i][j] = s[0]
                    d[i][j].remove(s[0])
                    remain -= 1
                else:
                    return sudoku, d, remain, False
    return sudoku, d, remain, True

def insert_sudoku(sudoku, d, row, col, remain):
    domain_list = list(d[row][col])
    
    for element in domain_list:
        if is_valid_insert(sudoku, element, row, col):
            
            sudoku_copy = copy.deepcopy(sudoku)
            d_copy = copy.deepcopy(d)
            
            sudoku_copy[row][col] = element
            d_copy[row][col].remove(element)
            
            if (remain-1 == 0):
                print(sudoku_copy)
                return sudoku_copy, d_copy
            
            minLen, next_row, next_col = find_mindomain(sudoku_copy, d_copy)
            sudoku_copy, d_copy = insert_sudoku(sudoku_copy, d_copy, next_row, next_col, remain-1)
        else:
            continue
    return sudoku, d

def play_sudoku(sudoku, empty_num):

    d = [['-']*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            d[i][j] = set({1,2,3,4,5,6,7,8,9})
            if not sudoku[i][j] == 0:
                d[i][j].clear()
    
    if empty_num == 0:
        print(sudoku)
        return sudoku, d, 0
    
    remain = -1
    curr_remain = 81
    valid = True
    while (not curr_remain == remain) and valid:
        remain = curr_remain
        for i in range(9):
            for j in range(9):
                d[i][j] = k_consistency(sudoku, d, i, j)
        sudoku, d, curr_remain, valid = easy_fill(sudoku, d, remain)
    
    empty_num = remain
    
    if not valid:
        return sudoku, d, empty_num
    else:
        if empty_num == 0:
            return sudoku, d, empty_num
    
    minLen, row, col = find_mindomain(sudoku, d)
    l = list(d[row][col])
    for element in l:
        sudoku_copy = copy.deepcopy(sudoku)
        if is_valid_insert(sudoku_copy, element, row, col):
            sudoku_copy[row][col] = element
            sudoku_copy, d, empty_num = play_sudoku(sudoku_copy, empty_num-1)
        else:
            continue
    

f = open('suinput.csv', 'r')
csv_file = csv.reader(f)
sudoku = []
for s in csv_file:
    for i in range(9):
        s[i] = int(s[i])
    sudoku.append(s)
f.close()


# for all loc, use a set to store the domain
d = [['-']*9 for i in range(9)]
for i in range(9):
    for j in range(9):
      d[i][j] = set({1,2,3,4,5,6,7,8,9})
      if not sudoku[i][j] == 0:
          d[i][j].clear()

remain = -1
curr_remain = 81
while not curr_remain == remain:
    remain = curr_remain
    for i in range(9):
        for j in range(9):
            d[i][j] = k_consistency(sudoku, d, i, j)
    
    sudoku, d, curr_remain, correct = easy_fill(sudoku, d, remain)
    
sudoku, d, remain = play_sudoku(sudoku, remain)
            
# find the minimum domain to start
#minLen, row, col = find_mindomain(sudoku, d)
            
# sudoku, d = insert_sudoku(sudoku, d, row, col, value_remain)
   