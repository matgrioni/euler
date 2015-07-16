#!/usr/bin/python

import time

input = [
    "75",
    "95 64",
    "17 47 82",
    "18 35 87 10",
    "20 04 82 47 65",
    "19 01 23 75 03 34",
    "88 02 77 73 07 63 67",
    "99 65 04 28 06 16 70 92",
    "41 41 26 56 83 40 80 70 33",
    "41 48 72 33 47 32 37 16 94 29",
    "53 71 44 65 25 43 91 52 97 51 14",
    "70 11 33 28 77 73 17 78 39 68 17 57",
    "91 71 52 38 17 14 91 43 58 50 27 29 48",
    "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
    "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
]

# Process the lines
lines = [[int(x) for x in line.split()] for line in input]

# Finds the max sum path in the tree recursively.
# Start at the top of the tree if no parameters are given.
def maxPath(row=0, col=0):
    # If this row is the last of the tree, this current node is the max.
    if row == len(lines) - 1:
        return lines[row][col]

    # Otherwise, we get the current node, and see which of the two paths it
    # can take are larger.
    node = lines[row][col]
    return node + max((maxPath(row + 1, col), maxPath(row + 1, col + 1)))

print("Finds the max sum path along the tree of Project Euler problem 18")
print(maxPath())
