#!/usr/bin/python3
"""
N queens
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_q < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(n):
    """
    Solves the N-Queens problem using backtracking.
    Returns a list of lists, where each inner list represents a solution
    with the positions of the queens on the board.
    """
    def is_safe(board, row, col):
        """
        Checks if a queen can be placed on the board[row][col].
        """
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal on the left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, col):
        """
        Recursive function to solve the N-Queens problem.
        """
        # Base case: If all queens are placed, return True
        if col == n:
            solutions.append([list(board[i]) for i in range(n)])
            return True

        # Place this queen in all rows one by one
        res = False
        for i in range(n):
            # If a queen can be placed on the board[i][col]
            if is_safe(board, i, col):
                # Place this queen on board[i][col]
                board[i][col] = 1

                # Recur to place rest of the queens
                res = solve(board, col + 1) or res

                # If placing the queen in board[i][col] doesn't lead to a solution,
                # remove the queen from board[i][col]
                board[i][col] = 0

        # If the queen cannot be placed in any row in this column, return False
        return res

    solutions = []
    board = [[0 for j in range(n)] for i in range(n)]
    solve(board, 0)
    return solutions


for answer in solve_nqueens(n_q):
    result = []
    for p in answer:
        result.append([i + 1 for i, x in enumerate(p) if x == 1])
    print(result)
