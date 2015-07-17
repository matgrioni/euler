#!/usr/bin/python

import time

# Returns if the given number is an abundant number or not
def isAbundant(n):
    # Check through all possible proper factors
    # TODO: Use sqrt as limit instead to be more efficient
    s = 0
    for i in range(1, n/2 + 1):
        if n % i == 0:
            s += i

    return s > n

print("Finds the sum of all numbers that can't be written as a sum of")
print("abundant numbers")

start = time.time()

# All numbers greater than 28123 can be writtten as a sum of abundant numbers
# so only go up to 28123.
s = 0
for i in range(1, 28124):

    # Since 12 is the smallest abundant number, any possible sum of two abundant
    # numbers has to have the first number start from 12 and end 12 before the
    # checked number. For example with 35, start from 12 and go up to 23, once
    # you pass 23, 24 + 11 = 35 and we already know 11 is not abundant.
    #
    # sumAbundant assumes that i can not be written as a sum of two abundant
    # numbers. True if it can be, false if i can not be written like that.
    sumAbundant = False
    for j in range(12, i / 2 + 1):
        if isAbundant(j) and isAbundant(i - j):
            sumAbundant = True
            break
    
    # So i can not be written as a sum of two abundant numbers.
    if not sumAbundant:
        s += i

end = time.time()

print("Result: {}".format(s))
print("{} s".format(end - start))
