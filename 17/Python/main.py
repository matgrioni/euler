#!/usr/bin/python

import time

# The mapping from number in different places to words
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
        "ninety"]

print("Sums letters in 1 to n (inclusive) and n is less than 1001")
n = int(raw_input("Enter n > "))

start = time.time()

count = 0
for i in range(1, n+1):
    if i < 1000:
        if i >= 100:
            count += len(ones[i / 100 - 1])

            count += len("hundred")

            if i % 100 != 0:
                count += len("and")

        hundreds = i % 100
        last = hundreds % 10

        if hundreds != 0:
            if hundreds < 20:
                count += len(ones[hundreds-1])
            else:
                count += len(tens[hundreds / 10 - 2])

                if last != 0:
                    count += len(ones[last - 1])
    else:
        count += len("onethousand")

end = time.time()

print("Result: {}".format(count))
print("{} s".format(end - start))
