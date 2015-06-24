#!/usr/bin/python

print("This program finds the difference between the sum of squares of the")
print("first n natural numbers and the square of the sum of the first n")
print("natural numbers")

n = int(raw_input("Enter n > "))

# Program expands the square of the sum of the first n natural numbers.
# So this expression is in the form (a+b+c...)^2 = a^2+2ab+2bc+b^2...
# So all the x^2 values will cancel out when subtracted.
sum = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            sum += i * j

print("Result: {}".format(sum))
