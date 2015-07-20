#!/usr/bin/python

import time

# A dict for memoization
memo = {}

# Amount is the amount you want to breakup, and denoms is a list of
# denominations in descending order ending in 1.
def ways(amount, denoms):
    if denoms[0] == 1:
            return 1
    else:
        # If this input set has already been resolved just use that result
        if (amount, denoms[0]) in memo:
            return memo[(amount, denoms[0])]
        else:
            # Find out how many times the largest denomination can fit into the
            # amount then recursively find how many times the different possibs
            # can fit into the remaining amount
            t = amount/denoms[0]

            total = 0
            for i in range(t + 1):
                # The largest count fits in t times, so the possibliites are
                # amount - 0*denom, amount-1*denom, etc..., up to the t limit
                total += ways(amount - i*denoms[0], denoms[1:])

            # Store the new result for this input set, so that it is memorized
            memo[(amount, denoms[0])] = total

            return total

print("Using british pound denominations, how many ways are there to make")
print("n pence")
n = int(raw_input("Enter n > "))

start = time.time()
res = ways(n, [200, 100, 50, 20, 10, 5, 2, 1])
end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
