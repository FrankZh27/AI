#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:37:03 2018

@author: jiaweizhong
"""
import csv
import copy

def find_mindomain(sudoku, d):
    minLen = 9
    row = 0
    col = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 and len(d[i][j]) <= minLen:
                row = i
                col = j
                minLen = len(d[i][j])
    return minLen, row, col

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

def is_valid_insert(sudoku, element, row, col):
    for k in range(9):
        if not k == col:
            if sudoku[row][k] == element:
                return False
    
    for k in range(9):
        if not k == row:
            if sudoku[k][col] == element:
                return False
    
    grid_x = row//3*3
    grid_y = col//3*3
    
    for m in range(grid_x, grid_x+3):
        for n in range(grid_y, grid_y+3):
            if not(m == row and n == col):
                if sudoku[m][n] == element:
                    return False
    return True

def easy_fill(sudoku, d):
    count = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 and len(d[i][j]) == 1:
                s = list(d[i][j])
                if is_valid_insert(sudoku, s[0], i, j):
                    sudoku[i][j] = s[0]
                    d[i][j].remove(s[0])
                    count += 1
                else:
                    return sudoku, count, False
    return sudoku, count, True


def play_sudoku(sudoku, empty_slot):
    if empty_slot == 0:
        print(sudoku)
        return sudoku, True
    
    d = [['-']*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
          d[i][j] = set({1,2,3,4,5,6,7,8,9})
          if not sudoku[i][j] == 0:
              d[i][j].clear()
    
    count = -1
    valid = True
    filled = 0
    sudoku_copy = copy.deepcopy(sudoku)
    d_copy = copy.deepcopy(d)
    while (not count == 0) and valid:
        count = 0
        for i in range(9):
            for j in range(9):
                d_copy[i][j] = k_consistency(sudoku_copy, d_copy, i, j)
        
        sudoku_copy, count, valid = easy_fill(sudoku_copy, d_copy)
        filled += count
    
    if not valid:
        return sudoku, False
    else:
        if empty_slot - filled == 0:
            print(sudoku_copy)
            return sudoku_copy, True
            
        sudoku = copy.deepcopy(sudoku_copy)
        d = copy.deepcopy(d_copy)
        
        minLen, row, col = find_mindomain(sudoku, d)
        l = list(d[row][col])
        for element in l:
            sudoku_copy = copy.deepcopy(sudoku)
            d_copy = copy.deepcopy(d)
            if is_valid_insert(sudoku_copy, element, row, col):
                sudoku_copy[row][col] = element
                sudoku_copy, valid = play_sudoku(sudoku_copy, empty_slot-filled-1)
                if valid:
                    sudoku = copy.deepcopy(sudoku_copy)
                else:
                    continue
            else:
                continue
    return sudoku, valid
    
    
        


f = open('suinput.csv', 'r')
csv_file = csv.reader(f)
sudoku = []
for s in csv_file:
    for i in range(9):
        s[i] = int(s[i])
    sudoku.append(s)
f.close()

empty_slot = 81
d = [['-']*9 for i in range(9)]
for i in range(9):
    for j in range(9):
      d[i][j] = set({1,2,3,4,5,6,7,8,9})
      if not sudoku[i][j] == 0:
          d[i][j].clear()
          empty_slot -= 1

sudoku, valid = play_sudoku(sudoku, empty_slot)
f = open('suoutput.csv', 'w')
writer = csv.writer(f)
for row in sudoku:
    writer.writerow(row)
f.close()