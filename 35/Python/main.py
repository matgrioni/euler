#!/usr/bin/python

import time
import math

# Rotates a number by one digit to the right. 917 --> 791
# Rotate to the right, otherwise if to the left don't get all the possiblities
# Such as 101 --> 011 --> 11 --> 11, when to the left
# If to the right, 101 --> 110 --> 011
def rotate(n):
    return (n % 10) * 10 ** int(math.log10(n)) + (n / 10)

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

print("Finds circular primes less than n")
n = int(raw_input("Enter n > "))

start = time.time()

count = 0
for i in range(2, n):
    rotated = i
    circular = True

    for _ in range(int(math.log10(i)) + 1):
        if not prime(rotated):
            circular = False
            break

        rotated = rotate(rotated)

    if circular:
        count += 1

end = time.time()

print("Result: {}".format(count))
print("{} s".format(end - start))
