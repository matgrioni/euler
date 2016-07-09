#!/usr/bin/python

import time
import math

print("Finds the maximum number of pythagorean triplets with a given perimeter <= p")
perimeter = int(raw_input("Enter p > "))

start = time.time()

# Initialize counter array
counts = [0] * (perimeter + 1)

# Perimeter must be even in a right triangle and p = a + b + c and
# a^2 + b^2 = c^2 substitution was used to find rem. This results in
# p * (p - 1 * a) / (2 * (p - a)) which must be an integer in a right
# triangle.
for p in range(2, perimeter + 1, 2):
    for a in range(1, p - 1):
        rem = p * (p - 2 * a) % (2 * (p - a))
        
        if rem == 0:
            counts[p] += 1

res = counts.index(max(counts))
end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
