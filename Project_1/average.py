#!/usr/bin/env python2
# Project 1

print "Python 101"

arr = []
avg = 0
name = raw_input("Enter name: ")

for n in range(0, 4):
    temp = raw_input("Enter grade " + str(n+1) +": ")
    arr.append(int(temp))
    avg = avg + arr[n]

avg = avg/5.0
print name + " Average: " + str(avg)
