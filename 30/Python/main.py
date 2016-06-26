#!/usr/bin/python

import time

def isNarcissitic(number, p):
    copy = number
    digits = []

    while copy > 0:
        digits.append(copy % 10)
        copy /= 10

    s = sum(map(lambda d: d ** p, digits))
    return s == number

print("This program finds the sum of all numbers whose digits summmed and taken")
print("to a power, p, equal the number itself")
p = int(raw_input("Enter p > "))

start = time.time()
# Find the upper limit for the size of the possible numbers
# The size will be expressed as the number of digits in the number
# TODO: Is there a more pythonic way of expressing this
n = 1
while n * 9 ** p >= 10 ** (n - 1):
    n += 1

s = sum(filter(lambda x: isNarcissitic(x, p), range(2, 10 ** (n - 1))))
end = time.time()

print("Result: {}".format(s))
print("{} s".format(end - start))
