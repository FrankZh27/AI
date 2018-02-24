#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:37:03 2018

@author: jiaweizhong
"""
import csv
import copy
import sys

def find_mindomain(sudoku, domain):
    """find the domain with minimum length"""
    min_len = 9
    row = 0
    col = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 and len(domain[i][j]) <= min_len:
                row = i
                col = j
                min_len = len(domain[i][j])
    return row, col

def k_consistency(sudoku, domain, i_row, j_col):
    """Apply k-consistency to reduce the domain at d[i][j]"""
    row = domain[i_row][j_col]
    for k in range(9):
        if not k == j_col:
            if (not sudoku[i_row][k] == 0) and (sudoku[i_row][k] in row):
                row.remove(sudoku[i_row][k])

    for k in range(9):
        if not k == i_row:
            if (not sudoku[k][j_col] == 0) and (sudoku[k][j_col] in row):
                row.remove(sudoku[k][j_col])

    grid_x = i_row//3*3
    grid_y = j_col//3*3

    for m_row in range(grid_x, grid_x+3):
        for n_col in range(grid_y, grid_y+3):
            if not(m_row == i_row and n_col == j_col):
                if (not sudoku[m_row][n_col] == 0) and (sudoku[m_row][n_col] in row):
                    row.remove(sudoku[m_row][n_col])

    return row

def is_valid_insert(sudoku, element, row, col):
    """Check if it is a valid insertion"""
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

    for m_row in range(grid_x, grid_x+3):
        for n_col in range(grid_y, grid_y+3):
            if not(m_row == row and n_col == col):
                if sudoku[m_row][n_col] == element:
                    return False
    return True

def easy_fill(sudoku, domain):
    """fill the blanks already decided according to known numbers"""
    count = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 and len(domain[i][j]) == 1:
                number = list(domain[i][j])
                if is_valid_insert(sudoku, number[0], i, j):
                    sudoku[i][j] = number[0]
                    domain[i][j].remove(number[0])
                    count += 1
                else:
                    return sudoku, count, False
    return sudoku, count, True

def write_file(sudoku):
    """Write solution to csv file"""
    file = open('suoutput.csv', 'w')
    writer = csv.writer(file)
    for row in sudoku:
        writer.writerow(row)
    file.close()
    return

def play_sudoku(sudoku, empty_slot):
    """Fill sudoku based on k-consistency"""
    print(empty_slot)
    if empty_slot == 0:
        print(sudoku)
        write_file(sudoku)
        sys.exit()
        return sudoku, True

    domain = [['-']*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            domain[i][j] = set({1, 2, 3, 4, 5, 6, 7, 8, 9})
            if not sudoku[i][j] == 0:
                domain[i][j].clear()

    count = -1
    valid = True
    filled = 0
    sudoku_copy = copy.deepcopy(sudoku)
    d_copy = copy.deepcopy(domain)
    while (count != 0) and valid:
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
            write_file(sudoku_copy)
            sys.exit()
            return sudoku_copy, True

        sudoku = copy.deepcopy(sudoku_copy)
        domain = copy.deepcopy(d_copy)

        row, col = find_mindomain(sudoku, domain)
        list_element = list(domain[row][col])
        empty_slot = empty_slot - filled
        for element in list_element:
            sudoku_copy = copy.deepcopy(sudoku)
            d_copy = copy.deepcopy(domain)
            if is_valid_insert(sudoku_copy, element, row, col):
                sudoku_copy[row][col] = element
                sudoku_copy, valid = play_sudoku(sudoku_copy, empty_slot - 1)
                if valid:
                    sudoku = copy.deepcopy(sudoku_copy)
                else:
                    valid = False
                    continue
            else:
                valid = False
                continue
    return sudoku, False

def main():
    """This is the main function"""
    file = open('suinput.csv', 'r')
    csv_file = csv.reader(file)
    sudoku = []
    for line in csv_file:
        for i in range(9):
            line[i] = int(line[i])
        sudoku.append(line)
    file.close()

    empty_slot = 81
    domain = [['-']*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            domain[i][j] = set({1, 2, 3, 4, 5, 6, 7, 8, 9})
            if not sudoku[i][j] == 0:
                domain[i][j].clear()
                empty_slot -= 1

    sudoku, valid = play_sudoku(sudoku, empty_slot)
    if valid:
        file = open('suoutput.csv', 'w')
        writer = csv.writer(file)
        for row in sudoku:
            writer.writerow(row)
        file.close()

if __name__ == "__main__":
    main()
