#!/usr/bin/python

import time

def lastDigits(n, l):
    if l == 1:
        return n % 10
    else:
        return lastDigits(n / 10, l - 1) * 10 + n % 10

print("Finds the last n digits of 1^1+2^2+...+1000^1000")
n = int(raw_input("Enter n > "))

start = time.time()

s = sum({i**i for i in range(1, 1001)})
res = lastDigits(s, 10)

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
