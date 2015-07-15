#!/usr/bin/python

######################################################################
# Author: Matias Grioni
# Created: 7/15/15
#
# Sums the diagonals of a spiral that is size n x n. The way this
# spiral is formed can be seen on Problem 28 of Project Euler. Note
# the problem asks for a 1001 x 1001 spiral, which by my algorithm
# is a spiral that has 501 levels.
######################################################################

import time

def sumSpiral(dim):
    return sum([4*(4*n*n-7*n+4) for n in range(2, ((dim + 1) / 2) + 1)]) + 1

print("Sums the diagonals of a spiral of numbers of size n x n")
n = int(raw_input("Enter n > "))

start = time.time()
result = sumSpiral(n)
end = time.time()

print("Result: {}".format(result))
print("{} s".format(end - start))
