#! /usr/bin/python3
a = int(input('Please enter the first number: '))
b = int(input('Please enter the second number: '))
c = (input('Please input "+" or "-" or "*" or "/" '))
if c == "+":
    print ('The output is', a + b) 
elif c == "-":
    print ('The output is', a - b)
elif c == "*":
    print ('The output is', a * b)
else:
    print ('The output is', a / b)
