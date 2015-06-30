#!/usr/bin/python

import time

# Returns a string digits long of the numbers after the decimal
# point in 1/n.
def getDigits(n, digits):
    res = ""

    top = 10
    for i in range(digits):
        digit = top / n
        res += str(digit)
        top = (top - (digit * n)) * 10

    return res

print("Finds x < n for which 1/x has the longest repeating sequence")
n = int(raw_input("Enter n > "))
digits = int(raw_input("Digit check > "))

start = time.time()

length = 0
res = 0
for i in range(2, n):
    decimals = getDigits(i, digits)

    for s in range(digits):
        for l in range(1, digits + 1 - s):
            subs = [decimals[idx:idx+l] for idx in range(s, digits - l + 1, l)]
            repeat = len(set(subs)) == 1

            if repeat and l > length:
                length = l
                res = i
                break

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
