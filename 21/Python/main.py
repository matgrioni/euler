#!/usr/bin/python

import time
import math

def d(num):
    sqrt = int(math.sqrt(num))

    s = 0
    for i in range(1, sqrt):
        if num % i == 0:
            s += i

            if num / i < num:
                s += num / i

    if sqrt * sqrt == num:
        s += sqrt

    return s

print("Finds sum of amicable numbers less than n")
n = int(raw_input("Enter n > "))

start = time.time()

s = 0
for a in range(2, n+1):
    b = d(a)
    c = d(b)

    if a != b and c == a:
        s += a

end = time.time()

print("Result: {}".format(s))
print("{} s".format(end - start))
