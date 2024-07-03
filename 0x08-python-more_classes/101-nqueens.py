#!/usr/bin/python3
"""
This module solves the N queens puzzle. The N queens puzzle is the challenge
of placing N non-attacking queens on an N×N chessboard.

Usage:
    ./101-nqueens.py N

Where N is the size of the board and the number of queens to place.
The solution(s) display the positions of each queen on the chessboard,
with each position represented by a list [row, column].

Attributes:
    None

Todo:
    * Improve efficiency using advanced algorithms if necessary.
"""

import sys

def is_safe(queen_position, new_queen):
    """
    Check if a new queen's position is safe from attack by other queens.

    Parameters:
    queen_position (list of tuples): The current positions of queens on the board.
    new_queen (tuple): The position (row, column) of the queen to be placed.

    Returns:
    bool: True if the position is safe, False otherwise.
    """
    for queen in queen_position:
        if queen[1] == new_queen[1] or \
           queen[0] - queen[1] == new_queen[0] - new_queen[1] or \
           queen[0] + queen[1] == new_queen[0] + new_queen[1]:
            return False
    return True

def solve_nqueens(n, row=0, queen_position=[]):
    """
    Recursively find and print all solutions for the N queens puzzle.

    Parameters:
    n (int): The size of the chessboard and the number of queens to place.
    row (int): The current row to try placing a queen in.
    queen_position (list of tuples): The positions of queens already placed.

    Returns:
    None
    """
    if row == n:
        print(queen_position)
        return

    for col in range(n):
        if is_safe(queen_position, (row, col)):
            queen_position.append((row, col))
            solve_nqueens(n, row + 1, queen_position)
            queen_position.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
