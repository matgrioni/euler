#!/usr/bin/python

import time
import math

print("Finds the maximum number of pythagorean triplets with a given perimeter <= p")
p = int(raw_input("Enter p > "))

start = time.time()

# Initialize counter array
counts = [0] * (p + 1)

for a in range(p):
    for b in range(p - a):
        csq = a * a + b * b
        c = math.sqrt(csq)

        if c.is_integer():
            ci = int(c)
            if a + b + c <= p:
                counts[a + b + ci] += 1

res = counts.index(max(counts))
end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
