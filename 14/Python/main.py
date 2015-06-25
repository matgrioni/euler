#!/usr/bin/python

import time

def collatz(num):
    if num % 2 == 0:
        num /= 2
    else:
        num = 3 * num + 1

    return num

print("This program finds the number less than n with the longest collatz seq")
n = int(raw_input("Enter n > "))

start = time.time()

m = 0
num = 1

for i in range(1, n+1):
    res = i
    count = 1
    while res != 1:
        res = collatz(res)
        count += 1

    if count > m:
        num = i
        m = count

end = time.time()

print("Result: {}".format(num))
print("{} s".format(end - start))
