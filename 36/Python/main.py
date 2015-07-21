#!/usr/bin/python

import time
import math

# Converts a decimal number to its binary representation
def dtob(n):
    # Get the largest power of 2 that fits into the number
    mag = int(math.log(n, 2))

    # Then going from this max, we find if the current power of 2 fits
    # If it does then add one to the binary representation.
    # Each loop multiply the binary representation by 10 as we are going
    # through the 2^3, kinda like 10^3 bases, and placeholders need to be
    # there.
    b = 0
    for i in range(mag, -1, -1):
        base = 2 ** i
        b *= 10
        
        if n >= base:
            n -= base
            b += 1

    return b

def reverse(n):
    if n < 10:
        return n
    else:
        magnitude = int(math.log10(n))

        rem = n % 10
        n /= 10

        return rem * 10 ** magnitude + reverse(n)

print("Finds the sum of all double-base palindromes less than n")
n = int(raw_input("Enter n > "))

start = time.time()

res = 0
for i in range(1, n):
    binary = dtob(i)
    if i == reverse(i) and binary == reverse(binary):
        res += i

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
