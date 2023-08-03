#!/usr/bin/python3
"""The N Queens problem"""


def placing_is_safe(board, row, col, dimension):
    """
    checks if a queen can be safely placed on a spot
    """
    # returns False if two queens share the same column
    for cur_row in range(row):
        if board[cur_row][col] == 1:
            return False

    # returns False if two queens share the same `\` diagonal
    for cur_row, cur_col in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[cur_row][cur_col] == 1:
            return False

    # returns False if two queens share the same `/` diagonal
    for cur_row, cur_col in zip(range(row, -1, -1), range(col, dimension, 1)):
        if board[cur_row][cur_col] == 1:
            return False

    return True


def print_solution(board: list):
    in_list = []

    for idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if row[col_idx] == 1:
                in_list.append([idx, col_idx])

    print(in_list)


def n_queen(board, row, dimension, count):
    """
    Solves the nqueen problem and prints all the
    possible solutions
    """
    if row == dimension:
        print_solution(board)
        return
    # place a queen in every square of the current row
    # and recur for each valid movement
    for col in range(dimension):
        # if no queen attacks the other
        if placing_is_safe(board, row, col, dimension):

            # place queen on current square
            board[row][col] = 1

            # recur for next row
            n_queen(board, row + 1, dimension, count)
            # backtrack and remove queen from current square
            board[row][col] = 0


def main(N):
    """Run program"""
    board = [[0 for _ in range(N)] for _ in range(N)]

    n_queen(board, 0, N, 0)


if __name__ == '__main__':
    from sys import argv, exit

    # check arguments
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    # check input
    if not argv[1].isdigit():
        print('N must be a number')
        exit(1)
    if int(argv[1]) < 4:
        print('N must be at least 4')
        exit(1)
    main(int(argv[1]))
