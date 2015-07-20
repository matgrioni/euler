#!/usr/bin/python

import time

# Using wikipedia there is a property of repeating decimals that for 1/k
# the period is <= k - 1. So if we were to divide 1/k long division style,
# the numbers would repeat once again if the remainder of one of the operations
# were 1. Returns the length of the cycle or 0 if there is no repetition.
def cycle(n):
    for i in range(1, n):
        if 10**i % n == 1:
            return i

    return 0

print("Finds x < n for which 1/x has the longest repeating sequence")
n = int(raw_input("Enter n > "))

start = time.time()

maxCycle = 0
res = 0

for i in range(1, n + 1):
    c  = cycle(i)
    if c > maxCycle:
        maxCycle = c
        res = i

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
