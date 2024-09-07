#! /usr/bin/python3
A = int(input("First number"))
B = int(input("Second number"))
result=0
for x in range(A, B+1):
    if x % 2==0:
        result  = result + x
print (result) 

