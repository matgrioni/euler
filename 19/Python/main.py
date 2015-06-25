#!/usr/bin/python

import time

class Month(object):
    DAYSPERMONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, index, year):
        self.index = index
        self.year = year

        self.leapYear = self.year % 4 == 0 and \
                        (self.year % 100 != 0 or self.year % 400 == 0)
    
    def setYear(self, year):
        self.year = year
        self.leapYear = self.year % 4 == 0 and \
                        (self.year % 100 != 0 or self.year % 400 == 0)

    def days(self):
        d = Month.DAYSPERMONTH[self.index]

        if self.leapYear and self.index == 1:
            d += 1

        return d

print("Finds how many of n weekdays fell on the first of months between 1 Jan")
print("1901 and 31 Dec 2000. n from 0 to 6 for the days of the week starting")
print("with Sunday.")

n = int(raw_input("Enter n > "))

start = time.time()

month = Month(0, 1901)
day = 2

count = 0
while month.year < 2001:
    if day == n:
        count += 1

    day = (day + month.days() % 28) % 7
    month.index += 1

    if month.index > 11:
        month.setYear(month.year + 1)
        month.index = 0

end = time.time()

print("Results: {}".format(count))
print("{} s".format(end - start))
