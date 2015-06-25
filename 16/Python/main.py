#!/usr/bin/python

import time

# Returns the sum of the digits of 2 ^ n, where
# num is the provided parameter
def sumOfDigits(n):
    if n == 1:
        return 2
    else:
        priorSum = sumOfDigits(n - 1)

        newSum = 0
        while priorSum > 0:
            lastDigit = (priorSum % 10) * 2
            newSum += lastDigit % 10 + lastDigit / 10

            priorSum /= 10

        return newSum

print("Finds the sum of the digits of 2^n")
n = int(raw_input("Enter n > "))

start = time.time()
res = sumOfDigits(n)
end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
