#!/usr/bin/python

import time
import string

def alphabetical(name1, name2):
    index = 0
    while index < min(len(name1), len(name2)):
        c1 = string.uppercase.index(name1[index])
        c2 = string.uppercase.index(name2[index])

        if c1 < c2:
            return True
        elif c1 > c2:
            return False

    return len(name1) < len(name2)

def sort(names):
    for i in range(len(names)):
        cur = names[i]

        for j in range(i+1, len(names)):
            next = names[j]

            # If the latter name comes first in the alphabet then insert
            # it before i
            if alphabetical(next, cur):
                names.remove(next)
                names.insert(i, next)
                cur = next

    print(names)

print("Finds sum of name scores in provided text file")
fn = raw_input("Enter filename > ")

start = time.time()

with open(fn, "r") as f:
    content = f.read()
    names = [name[1:-1] for name in content.split(",")]

    sort(names)

    s = 0
    for (i, name) in enumerate(names):
        nameScore = sum([string.uppercase.index(c) + 1 for c in name])
        s += nameScore * (i + 1)

end = time.time()

print("Result: {}".format(s))
print("{} s".format(end - start))
