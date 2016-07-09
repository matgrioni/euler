#!/usr/bin/python

import time
import math

class Pythagorean(object):
    PRIMITIVE_START = (3, 4, 5)

    def __init__(self):
        pass

    def triples(self, callback):
        return self._triples(callback, Pythagorean.PRIMITIVE_START)

    def _triples(self, callback, cur):
        t = []
        if callback(cur):
            t += [cur]

            u = self._uTransform(cur)
            a = self._aTransform(cur)
            d = self._dTransform(cur)

            t += self._triples(callback, u)
            t += self._triples(callback, a)
            t += self._triples(callback, d)

        return t

    def _uTransform(self, triple):
        return (triple[0] - 2 * triple[1] + 2 * triple[2],
                2 * triple[0] - triple[1] + 2 * triple[2],
                2 * triple[0] - 2 * triple[1] + 3 * triple[2])

    def _aTransform(self, triple):
        return (triple[0] + 2 * triple[1] + 2 * triple[2],
                2 * triple[0] - triple[1] + 2 * triple[2],
                2 * triple[0] + 2 * triple[1] + 3 * triple[2])

    def _dTransform(self, triple):
        return (-triple[0] + 2 * triple[1] + 2 * triple[2],
                -2 * triple[0] + triple[1] + 2 * triple[2],
                -2 * triple[0] + 2 * triple[1] + 3 * triple[2])

print("Finds the maximum number of pythagorean triplets with a given perimeter <= p")
perimeter = int(raw_input("Enter p > "))

start = time.time()

counts = [0] * (perimeter + 1)

p = Pythagorean()
for triple in p.triples(lambda (a, b, c): a + b + c <= perimeter):
    s = triple[0] + triple[1] + triple[2]

    for k in range(1, perimeter / s + 1):
        counts[k * s] += 1

res = counts.index(max(counts))

end = time.time()

print("Result: {}".format(res))
print("{} s".format(end - start))
