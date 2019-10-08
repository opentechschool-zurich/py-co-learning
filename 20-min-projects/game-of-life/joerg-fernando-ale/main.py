# jörg, fernando, ale
import os
import sys
import time

def display(board) :
    for line in board:
        print(line)

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# display(board)
# sys.exit()

def count_neighbours(x, y):
    counter = 0
    if y > 0:
        if x > 0:
            counter += board[x -1][y -1]
        counter += board[x][y -1]
        if x < 9:
            counter += board[x + 1][y -1]

    if x > 0:
        counter += board[x - 1][y]
    if x < 9:
        counter += board[x + 1][y]

    if y < 9:
        if x > 0:
            counter += board[x - 1][y + 1]
        counter += board[x][y + 1]
        if x < 9:
            counter += board[x + 1][y + 1]
    return counter

display(board)
for generation in range(4):
    new_board = board.copy()
    os.system('clear')
    for x in range(10):
        for y in range(10):
            counter = count_neighbours(x, y)
            if board[x][y] == 1:
                if counter in [2, 3]:
                    new_board[x][y] = 1
                else:
                    new_board[x][y] = 0
            else:
                if counter == 3:
                    new_board[x][y] = 1
                else:
                    new_board[x][y] = 0
    board = new_board
    display(board)
    time.sleep(1)
