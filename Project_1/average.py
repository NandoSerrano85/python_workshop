#!/usr/bin/env python2
# Project 1

print "Python 101"

arr = list()
avg = 0
name = raw_input("Enter name: ")
size = int(raw_input("How many grade with you enter: "))
for n in range(0, size):
    temp = raw_input("Enter grade " + str(n+1) +": ")
    arr.append(int(temp))
    avg = avg + arr[n]

avg = avg/size
print name + " Average: " + str(avg)

if avg >= 90:
    print "Letter grade is A"
elif avg >= 80:
    print "Letter grade is B"
elif avg >= 70:
    print "Letter grade is C"
elif avg >= 60:
    print "Letter grade is D"
else:
    print "Letter grade is f"