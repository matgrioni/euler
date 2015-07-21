#!/usr/bin/python

import time

print("Finds the maximum path sum for the triangle defined in triangle.txt")

# Process the lines in triangle.txt
lines = []
with open("triangle.txt", "r") as f:
    for line in f.readlines():
        lines.append([int(num) for num in line.split()])

# Given a current position in the line triangle, row: i, col: j returns the
# max sum from that position
def maxSum(i, j):
    if i == len(lines) - 1:
        return lines[i][j]
    else:
        return lines[i][j] + max((lines[i+1][j], lines[i+1][j+1]))

start = time.time()

# Rather than work from top to bottom, with greedy solution
# Go from bottom to top, and replace the row above the current one,
# with the max possible number given the prior row.

# So while there are at least two rows to work with keep simplifying the
# triangle.
while len(lines) > 1:
    # Substitute the numbers in the penultimate row with the max sum
    # possible from that position
    penultimate = [maxSum(len(lines) - 2, col)
                   for col in range(len(lines[len(lines) - 2]))]

    del lines[-1]
    lines[-1] = penultimate

end = time.time()

print("Result: {}".format(lines[0][0]))
print("{} s".format(end - start))
