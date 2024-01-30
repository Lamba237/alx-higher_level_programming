#!/usr/bin/python
"""
Queen chess
"""
import sys


def is_it_safe(board, row, col, numb):
    """
    :param board: board
    :param row: row
    :param col: col
    :param numb: number
    :return: either true or false
    """

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, numb, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_the_nqueens_util(board, col, nums, solutions):
    """
    :param board: board
    :param col: column
    :param nums: numbers
    :param solutions: solution to program
    :return: nothing
    """
    if col == nums:
        solutions.append([[i, j] for i in range(nums) for j in range(nums) if board[i][j] == 1])
        return

    for i in range(nums):

        if is_it_safe(board, i, col, nums):
            board[i][col] = 1
            solve_the_nqueens_util(board, col + 1, nums, solutions)
            board[i][col] = 0


def print_solution(number):
    """
    :param number: numbers
    :return: nothing
    """
    board = [[0 for _ in range(number)] for _ in range(number)]
    solutions = []
    solve_the_nqueens_util(board, 0, number, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 4:
            print("N must be at least 4")
            sys.exit(1)

        print_solution(num)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
