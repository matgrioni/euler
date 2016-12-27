#!/usr/bin/python

import time

print("Count unique terms for a^b where 2 <= a <= n and 2 <= b <= n.")
n = int(raw_input("Enter n > "))

start = time.time()

s = set()
for a in range(2, n + 1):
    for b in range(2, n + 1):
        s.add(a ** b)

res = len(s)
end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
