#!/usr/bin/python

import time
import math

print("Returns the nth lexographic permutation of the digits 0-9")
n = int(raw_input("Enter n > ")) - 1

start = time.time()

left = list(range(10))
order = ""

for i in reversed(range(10)):
    fac = math.factorial(i)

    num = n / fac
    order += str(left[num])

    n -= num * fac
    del left[num]

end = time.time()

print("Result: {}".format(order))
print("{} s".format(end - start))
