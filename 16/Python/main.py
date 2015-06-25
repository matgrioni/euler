#!/usr/bin/python

import time
import math

print("Finds the sum of the digits of 2^n")
n = int(raw_input("Enter n > "))

start = time.time()

num = int(math.pow(2, n))
res = 0

while num > 0:
    res += num % 10
    num /= 10

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
