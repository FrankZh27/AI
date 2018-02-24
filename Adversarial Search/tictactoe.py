#!/usr/bin/env python
import sys
import random
import math
import copy

def generate_board():
    board = [['-']*3 for i in range(3)]
    return board

def is_last_move(board):
    count = 0
    for i in board:
        for j in i:
            if j == '-':
                count += 1
    if count == 1:
        return True
    else:
        return False     

def isOver(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True

def minimax(board, label):
    min_val = 1
    max_val = -1
    row = 0
    col = 0
    if (label == 'o'):
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board_copy = copy.deepcopy(board)
                    board_copy[i][j] = 'o'
                    if isTerminated(board_copy):
                        max_val = 1
                        row = i
                        col = j
                        return 1, i, j
                    else:
                        if isOver(board_copy):
                            max_val = 0
                            row = i
                            col = j
                            return 0, i, j
                        else:
                            curr_val, curr_row, curr_col = minimax(board_copy, 'x')
                            if curr_val > max_val:
                                max_val = curr_val
                                row = i
                                col = j
        return max_val, row, col
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board_copy = copy.deepcopy(board)
                    board_copy[i][j] = 'x'
                    if isTerminated(board_copy):
                        min_val = -1
                        row = i
                        col = j
                        return -1, i, j
                    else:
                        if isOver(board_copy):
                            min_val = 0
                            row = i
                            col = j
                            return 0, i, j
                        else:
                            curr_val, curr_row, curr_col = minimax(board_copy, 'o')
                            if curr_val < min_val:
                                min_val = curr_val
                                row = i
                                col = j
        return min_val, row, col

def printboard(board):
    print()
    for i in board:
        s = ""
        for j in range(2):
            s = s + i[j] + ','
        s = s + i[2]
        print(s)
    return    
        
def move(board, write_list):    
    val, row, col = minimax(board, 'o') 
    board[row][col] = 'o'
    printboard(board)
    board_copy = copy.deepcopy(board)
    write_list.append(board_copy)
    return board, write_list

def isTerminated(board):
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and 
                            (not board[i][0] == '-')):
            return True
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and 
                            (not board[0][i] == '-')):
            return True
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and
        (not board[0][0] == '-')):
        return True
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and
        (not board[0][2] == '-')):
        return True
    return False
    

# Initialize board and player x move_list  
board = generate_board()
write_list = []
plyx_win = False
plyo_win = False

s = int(sys.argv[1])
print ("Seed = ", s)
random.seed(s);
plyx_list = []
for i in range(0,40):
    num = math.floor(9 * random.random())
    plyx_list.append(num)
    print (num)

# start to play
curr_plyx_index = 0;
plyx_row = 2 - plyx_list[curr_plyx_index]//3
plyx_col = plyx_list[curr_plyx_index]%3
board[plyx_row][plyx_col] = 'x'
curr_plyx_index += 1

printboard(board)
board_copy = copy.deepcopy(board)
write_list.append(board_copy)

for i in range(4):
    board, write_list = move(board, write_list)
    if (isTerminated(board)):
        plyo_win = True
        break
    
    plyx_row = 2 - plyx_list[curr_plyx_index]//3
    plyx_col = plyx_list[curr_plyx_index]%3
    curr_plyx_index += 1
    while(not board[plyx_row][plyx_col] == '-'):
        plyx_row = 2 - plyx_list[curr_plyx_index]//3
        plyx_col = plyx_list[curr_plyx_index]%3
        curr_plyx_index += 1
    
    board[plyx_row][plyx_col] = 'x'
    printboard(board)
    board_copy = copy.deepcopy(board)
    write_list.append(board_copy)
    if (isTerminated(board)):
        plyx_win = True
        break

# write file
f = open('tictactoe.txt', 'w')
for b in write_list:
    f.writelines('\n')
    for row in b:
        s = ""
        for i in range(2):
            s = s + row[i] + ','
        s = s + row[2] + '\n'
        f.writelines(s)
f.close()
            
        
        
    