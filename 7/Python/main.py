#!/usr/bin/python

import time
import math

print("This program finds the nth prime number")
n = int(raw_input("Enter n > "))

start = time.time()

count = 0
current = 1
while count < n:
    current += 1

    prime = True
    for i in range(2, int(math.sqrt(current)) + 1):
        if current % i == 0:
            prime = False
            break

    if prime:
        count += 1

end = time.time()

print("Result: {}".format(current))
print("{} s".format(end - start))
