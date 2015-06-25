#!/usr/bin/python

import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Finds the amount of ways to get to the lower right hand corner of an")
print("nxn square given that one can only move down or right")
n = int(raw_input("Enter n > "))

start = time.time()
facn = factorial(n)
res = factorial(2 * n) / (facn * facn)
end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
