#!/usr/bin/python3
'''N Queens Challenge'''

import sys


def is_safe(queens, row, col):
    """Check if the current column is safe"""
    for i in range(row):
        if queens[i] == col or queens[i] - (row - i) == col or \
                queens[i] + (row - i) == col:
            return False
    return True


def nqueens(n, row=0, queens=None):
    """Backtracking algorithm to solve the N queens problem"""
    if queens is None:
        queens = [None] * n
    if row == n:
        yield queens[:]
    else:
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                for solution in nqueens(n, row + 1, queens):
                    yield solution


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    for solution in nqueens(n):
        print(solution)
     print(val)
