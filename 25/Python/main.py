#!/usr/bin/python

import time
import math

print("Finds the index of the first Fibonacci sequence term to have more than")
print("n digits")
n = int(raw_input("Enter n > ")) - 1

start = time.time()

limit = 10 ** n
n1 = n2 = 1
cur = 2
index = 3
while cur < limit:
    n1 = n2
    n2 = cur
    cur = n1 + n2

    index += 1

end = time.time()

print("Result: {}".format(index))
print("{} s".format(end - start))
