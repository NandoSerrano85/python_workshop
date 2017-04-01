#!/usr/bin/env python2
# Project 2

gender = raw_input("Enter your gender: ")
name = raw_input("What is your name: ")
gen_dict = {"male":"Mr. ", "female": "Mrs. "}
if gen_dict[gender]:
    gender = gen_dict[gender]
else:
    gender = ""

first, last = name.split(" ")
address = raw_input(gender + last + ", what is your address: ")
number, street = address.find(" ")

place = raw_input("What is your favorite place to dine near Main Street? ")

addres2 = raw_input("And finally " + first + ", what is your city, state and zip: ")
city, state, zip_code = addres2.split(",")

print "Dear " + first +":\nMy anme is A.M. Aswindler, and I am running a contest for a $1000 gift\ncertificate to the " 
print place + " in " + city + ". I have wonderful news, you are\n"
print "a finalist in this sweepstakes and may soon be the luckiest person on \n"
print street + "! " + upper(gender) + upper(last) +", DO NOT PASS UP THIS OFFER! Please fill out your \n"
print "account information at the following site: http://www.swindler.net.\nGood luck!"