#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:37:03 2018

@author: jiaweizhong
"""
import sys
import random
import math
import copy

def generate_board():
    """Generate board"""
    board = [['-']*3 for i in range(3)]
    return board

def is_last_move(board):
    """check if it is the last move"""
    count = 0
    for i in board:
        for j in i:
            if j == '-':
                count += 1
    if count == 1:
        return True
    return False

def is_over(board):
    """Check if the game is over"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True

def minimax(board, label):
    """Minimax Algorithm"""
    min_val = 1
    max_val = -1
    row = 0
    col = 0
    if label == 'o':
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board_copy = copy.deepcopy(board)
                    board_copy[i][j] = 'o'
                    if is_terminated(board_copy):
                        max_val = 1
                        row = i
                        col = j
                        return 1, i, j
                    else:
                        if is_over(board_copy):
                            max_val = 0
                            row = i
                            col = j
                            return 0, i, j
                        else:
                            curr_val = minimax(board_copy, 'x')
                            if curr_val[0] > max_val:
                                max_val = curr_val[0]
                                row = i
                                col = j
        return max_val, row, col

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board_copy = copy.deepcopy(board)
                board_copy[i][j] = 'x'
                if is_terminated(board_copy):
                    min_val = -1
                    row = i
                    col = j
                    return -1, i, j
                else:
                    if is_over(board_copy):
                        min_val = 0
                        row = i
                        col = j
                        return 0, i, j
                    else:
                        result = minimax(board_copy, 'o')
                        if result[0] < min_val:
                            min_val = result[0]
                            row = i
                            col = j
    return min_val, row, col

def printboard(board):
    """Print board"""
    print()
    for i in board:
        str1 = ""
        for j in range(2):
            str1 = str1 + i[j] + ','
        str1 = str1 + i[2]
        print(str1)
    return

def move(board, write_list):
    """play_o move"""
    val = minimax(board, 'o')
    board[val[1]][val[2]] = 'o'
    printboard(board)
    board_copy = copy.deepcopy(board)
    write_list.append(board_copy)
    return board, write_list

def is_terminated(board):
    """Check if someone wins"""
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and \
            (not board[i][0] == '-'):
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and \
            (not board[0][i] == '-'):
            return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and \
        (not board[0][0] == '-'):
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and \
        (not board[0][2] == '-'):
        return True
    return False

def main():
    """Main function here"""
    board = generate_board()
    write_list = []

    number = int(sys.argv[1])
    print("Seed = ", number)
    random.seed(number)
    plyx_list = []
    for i in range(0, 40):
        num = math.floor(9 * random.random())
        plyx_list.append(num)
        print(num)

    # start to play
    curr_plyx_index = 0
    plyx_row = 2 - plyx_list[curr_plyx_index]//3
    plyx_col = plyx_list[curr_plyx_index]%3
    board[plyx_row][plyx_col] = 'x'
    curr_plyx_index += 1

    printboard(board)
    board_copy = copy.deepcopy(board)
    write_list.append(board_copy)

    for i in range(4):
        board, write_list = move(board, write_list)
        if is_terminated(board):
            break

        plyx_row = 2 - plyx_list[curr_plyx_index]//3
        plyx_col = plyx_list[curr_plyx_index]%3
        curr_plyx_index += 1
        while not board[plyx_row][plyx_col] == '-':
            plyx_row = 2 - plyx_list[curr_plyx_index]//3
            plyx_col = plyx_list[curr_plyx_index]%3
            curr_plyx_index += 1

        board[plyx_row][plyx_col] = 'x'
        printboard(board)
        board_copy = copy.deepcopy(board)
        write_list.append(board_copy)
        if is_terminated(board):
            break

    # write file
    file = open('tictactoe.txt', 'w')
    for board1 in write_list:
        file.writelines('\n')
        for row in board1:
            str3 = ""
            for i in range(2):
                str3 = str3 + row[i] + ','
            str3 = str3 + row[2] + '\n'
            file.writelines(str3)
    file.close()

if __name__ == "__main__":
    main()
