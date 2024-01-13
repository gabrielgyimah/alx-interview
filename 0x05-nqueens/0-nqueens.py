#!/usr/bin/python3
""" NQueens Module """

import sys


def nqueens(n):
    """
    Solve the N-Queens puzzle and print the solutions
    """
    def backtrack(queens, cord_dif, cord_sum):
        """
        Recursive backtracking algorithm.
        """
        p = len(queens)
        if p == n:
            solution.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in cord_dif and p+q not in cord_sum:
                backtrack(queens + [q], cord_dif + [p - q], cord_sum + [p + q])
    solution = []
    final_solution = []
    backtrack([], [], [])
    for row in solution:
        for i, col in enumerate(row):
            cordinates = [i, col]
            final_solution.append(cordinates)
        print(final_solution)
        final_solution = []


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(n)
