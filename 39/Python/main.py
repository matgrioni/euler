#!/usr/bin/python

import time

print("Finds the amount of right triangles with integral sides <= n")
n = int(raw_input("Enter n > "))

start = time.time()

count = 0
m = 0
res = 0
for p in range(3, n+1):
    for a in range(1, p):
        for b in range(1, p-a+1):
            for c in range(1, p-a-b+1):
                if a * a + b * b == c * c and a + b + c == p:
                    count += 1

    if count > m:
        m = count
        res = p

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
