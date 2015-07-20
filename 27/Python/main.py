#!/usr/bin/python

import time
import math

# Returns true if a number is prime, and false otherwise.
def prime(n):
    # Not sure if these should be prime or something else
    if n <= 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

# Checks if the result of a quadratic of the form n*n+a*n+b is prime given
# a, b, and n
def checkQuad(n, a, b):
    return prime(n*n + a*n + b)

print("For |a| < 1000, and |b| < 1000, finds the product of a and b")
print("which in the quadratic n^2 + an + b which produces the most")
print("consecutive primes")

start = time.time()

# Iterate from [0, 1000) for a and b, and then check the negative permutations
# as well.
prod = 0
cons = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while checkQuad(n, a, b):
            n += 1

        if n > cons:
            prod = a * b
            cons = n

end = time.time()

print("Result: {}".format(prod))
print("{} s".format(end - start))
