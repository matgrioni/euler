#!/usr/bin/python

import time
import math

def prime(num):
    prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break

    return prime

print("This program finds the sum of prime numbers less than n")
n = int(raw_input("Enter n > "))

start = time.time()
sum = 0
for i in range(2, n + 1):
    if prime(i):
        sum += i
end = time.time()

print("Result: {}".format(sum))
print("{} s".format(end - start))
