#!/usr/bin/python

import time
import math

class Fraction(object):
    def __init__(self, n, d):
        gcd = Fraction._gcd(n, d)
        self.n = n / gcd
        self.d = d / gcd

    @staticmethod
    def _gcd(a, b):
        if b == 0:
            return a
        else:
            return Fraction._gcd(b, a % b)

print("Count unique terms for a^b where 2 <= a <= n and 2 <= b <= n.")
n = int(raw_input("Enter n > "))

start = time.time()

res = (n - 1) * (n - 1)

for a in range(2, n + 1):
    exp = int(math.log(n, 2))

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
