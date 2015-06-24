#!/usr/bin/python

import time
import math

def divisorsCount(num):
    sqrt = int(math.sqrt(num))
    count = 0

    for i in range(1, sqrt):
        if num % i == 0:
            count += 2

    # If the int cast of the square root equals the original number than
    # it was an integer and an actual divisor of num
    if sqrt * sqrt == num:
        count += 1

    return count

print("This program finds the first triangle number to have over n divisors")
print("The nth triangular number is the sum of natural numbers up through n")
n = int(raw_input("Enter n > "))

start = time.time()

count = 0
index = 0
tri = 0
while count <= n:
    tri = (index * (index + 1)) / 2
    count = divisorsCount(tri)
    index += 1

end = time.time()

print("Result: {}".format(tri))
print("{} s".format(end - start))
