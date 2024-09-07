#! /usr/bin/python3
import random
A = random.randint(1,10)
B = random.randint(1,10)
print (A)
print (B)
#print (A + B) 
while True:
    C = input("Please Input the sum of two radmon numbers: ")
    #print (C)
    #print (A + B)
    if int(C) == (A + B):
        break
print("You are correct")
