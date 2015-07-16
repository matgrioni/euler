#!/usr/bin/python

import time
import operator

print("Finds the largest product of n numbers in a 20x20 grid in data.txt")
n = int(raw_input("Enter n > "))

start = time.time()

# Create a 2 dimensional array of the numbers from the data file
nums = []
with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        nums.append([int(x) for x in line.split()])

res = 0
# Go through each number in the array and check of the possibilities.
# A string of n digits has 4 cardinal possibilites and 4 diagonal ones.
# But if you always check 2 of each type than you cover all of them.
for i in range(20):
    for j in range(20):
        # Check right using foldl of the n numbers to the right of current pos
        right = reduce(operator.mul, nums[i][j:j+n], 1)

        # Check product of n digits down to the right of the current pos
        col = [row[j] for row in nums]
        down = reduce(operator.mul, col[i:i+n], 1)

        # Check down right diagonal
        dr = 0
        if (19 - i) + j < 20:
            drnums = [row[j + t] for (t, row) in enumerate(nums[i:])]
            dr = reduce(operator.mul, drnums[:n], 1)

        # Check down left diagonal but only if there is enough space that it
        # desn't wrap back around with a negative index
        dl = 0
        if j - n >= 0:
            dlnums = [row[j - i] for (i, row) in enumerate(nums[i:])]
            dl = reduce(operator.mul, dlnums[:n], 1)

        results = [right, down, dr, dl]
        for result in results:
            if result > res:
                res = result

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
