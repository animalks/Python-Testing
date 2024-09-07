#! /usr/bin/python3
import random
Even=0
Odd=0
output_list = []
for i in range(4):
    input("Please press enter, the " + str(i+1) + " person: ")
    A = random.randint(1,100)
    print (A)
    if A%2 == 0:
        Even = Even + 1
    else:    
        Odd = Odd + 1    
print ("No. of Even number is " + str(Even))    
print ("No. of Odd number is " + str(Odd))    
