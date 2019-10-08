import os
import sys
import time
from copy import deepcopy

def display(board) :
    os.system('clear')
    for line in board:
        print(line)

def count_neighbours(board, x, y):
    counter = 0
    for d_y in [-1, 0, 1]:
        for d_x in [-1, 0, 1]:
            if (d_x, d_y) != (0, 0):
                if 0 <= y + d_y <= 9 and 0 <= x + d_x <= 9:
                    counter += board[y + d_y][x + d_x]
    return counter

def is_alive(board, x, y):
    return board[y][x] == 1

def get_generation(board):
    new_board = deepcopy(board)
    for y in range(10):
        for x in range(10):
            counter = count_neighbours(board, x, y)
            if is_alive(board, x, y):
                new_board[y][x] = int(2 <= counter <= 3)
            else:
                new_board[y][x] = int(counter == 3)
    return new_board

def generate(board):
    display(board)
    for generation in range(5):
        time.sleep(1)
        board = get_generation(board)
        display(board)

if __name__ == "__main__":
    generate([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
