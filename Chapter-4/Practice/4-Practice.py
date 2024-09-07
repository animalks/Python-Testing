#! /usr/bin/python3
D = eval(input("Please input a number: "))
A = D
print (A)
while True:
        B = A%10
        print (B, end=' ')
        A = A//10
        if A < 1:
            break
