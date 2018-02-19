#!/usr/bin/env python
import sys
import random
import math
import copy

"""
s = int(sys.argv[1])
print ("Seed = ", s)
random.seed(s);
for i in range(0,5):
	print (math.floor(9 * random.random()))
"""
init_random = math.floor(9 * random.random())

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
# didn't finish
def calculate_val(board):
    val = 0
    for i in range(3):
        count_row = 0
        count_col = 0
        for j in range(3):
            if board[i][j] == 'o':
                count_row += 1
            if board[j][i] == 'o':
                count_col += 1
        if count_row == 3:
            val += 100
        elif count_row == 2:
            val += 10
        else:
            val += 1
        
        if count_col == 3:
            val += 100
        elif count_col == 2:
            val += 10
        else:
            val += 1
    
    count_cross = 0
    for i in range(3):
        if board[i][i] == 'o':
            count_cross += 1
    if count_cross == 3:
        val += 100
    elif count_cross == 2:
        val +=10
    else:
        val += 1
        
    count_cross = 0
    if (board[0][2] == 'o'):
        count_cross += 1
    if (board[1][1] == 'o'):
        count_cross += 1
    if (board[2][0] == 'o'):
        count_cross += 1
    if count_cross == 3:
        val += 100
    elif count_cross == 2:
        val += 10
    else:
        val += 1
    return val
        

def check_utility(board, label):
    min_val = sys.maxsize
    max_val = 0
    row = 0
    col = 0
    if (label == 'o'):
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board_copy = copy.deepcopy(board)
                    board_copy[i][j] = 'o'
                    curr_val, curr_row, curr_col = check_utility(board_copy, 'x')
                    if curr_val >= max_val:
                        row = i
                        col = j
        return max_val, row, col
    else:
        if is_last_move(board):
            board_copy = copy.deepcopy(board)
            for i in range(3):
                for j in range(3):
                    if board_copy[i][j] == '-':
                        board_copy[i][j] = 'x'
                        row = i
                        col = j
            val = calculate_val(board_copy)
            return val, row, col
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '-':
                        board_copy = copy.deepcopy(board)
                        board_copy[i][j] = 'x'
                        curr_val, curr_row, curr_col = check_utility(board_copy, 'o')
                        if curr_val <= min_val:
                            row = i
                            col = j
            return min_val, row, col

"""
def printboard(board):
    print()
    for i in board:
        print i[0],',',i[1],',',i[2]

"""
def printboard(board):
    print()
    for i in board:
        print(i)
        
def move(board):    
    val, row, col = check_utility(board, 'o')
    board[row][col] = 'o'
    printboard(board)
    return board
"""    
    for i in range(3):
        for j in range(3):
            if j == '-':
                board_copy = copy.deepcopy(board)
                board_copy[i][j] = 'o'
                curr_utility = check_utility(board_copy)
                if curr_utility >= max_utility:
                    max_utility = curr_utility
                    row = i
                    col = j
    
    board[row][col] = 'o'
    printboard(board)
    return board
"""
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
    

# Initialize board   
board = generate_board()
empty_slot = [[0]*3 for i in range(3)]
plyx_win = False
plyo_win = False

random.seed(3);
plyx_list = []
for i in range(0,40):
    num = math.floor(9 * random.random())
    plyx_list.append(num)

curr_plyx_index = 0;
plyx_row = plyx_list[curr_plyx_index]//3
plyx_col = plyx_list[curr_plyx_index]%3
board[plyx_row][plyx_col] = 'x'
empty_slot[plyx_row][plyx_col] = 1
curr_plyx_index += 1

printboard(board)

for i in range(4):
    board = move(board)
    if (isTerminated(board)):
        plyo_win = True
        break
    
    plyx_row = plyx_list[curr_plyx_index]//3
    plyx_col = plyx_list[curr_plyx_index]%3
    curr_plyx_index += 1
    while(not board[plyx_row][plyx_col] == '-'):
        plyx_row = plyx_list[curr_plyx_index]//3
        plyx_col = plyx_list[curr_plyx_index]%3
        curr_plyx_index += 1
    
    board[plyx_row][plyx_col] = 'x'
    empty_slot[plyx_row][plyx_col] = 1
    printboard(board)
    if (isTerminated(board)):
        plyx_win = True
        break
    