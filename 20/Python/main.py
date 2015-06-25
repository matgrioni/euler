#!/usr/bin/python

import time
import math

print("Sums digits of n!")
n = int(raw_input("Enter n > "))

start = time.time()

fac = math.factorial(n)
res = 0
while fac > 0:
    res += fac % 10
    fac /= 10

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
