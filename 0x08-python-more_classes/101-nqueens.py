#!/usr/bin/python3
"""
This Module solves the N queens challenge
"""
import sys


def is_safe(b, row, col, m):
    """
    :param b: board
    :param row: row
    :param col: column
    :param m: m attribute
    :return: either True or False
    """
    for i in range(col):
        if b[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if b[i][j] == 1:
            return False
    for i, j in zip(range(row, m, 1), range(col, -1, -1)):
        if b[i][j] == 1:
            return False
    return True


def solve_n_queens(my_board, col, n_num):
    """
    :param my_board: my board
    :param col: column
    :param n_num: number n for iteration
    :return: either True or res
    """
    if col == n_num:
        for i in range(n_num):
            for j in range(n_num):
                if my_board[i][j] == 1:
                    print("[[{}, {}]]".format(i, j), end="")
        print()
        return True
    res = False
    for i in range(n_num):
        if is_safe(my_board, i, col, n_num):
            my_board[i][col] = 1
            res = solve_n_queens(my_board, col + 1, n_num) or res
            my_board[i][col] = 0
    return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for i in range(n)] for j in range(n)]
    solve_n_queens(board, 0, n)
