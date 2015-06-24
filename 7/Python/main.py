#!/usr/bin/python

import time

print("This program finds the nth prime number")
n = int(raw_input("Enter n > "))

count = 0
current = 1
while count < n:
    current += 1

    prime = True
    for i in range(2, current/2 + 1):
        if current % i == 0:
            prime = False
            break

    if prime:
        count += 1


print("Result: {}".format(current))
