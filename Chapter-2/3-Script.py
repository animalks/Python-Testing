#! /usr/bin/python3

a = int(input('Please input a number: '))
if a > 100:
    print (a, 'is greater than 100')
elif a > 50:
    print (a, 'is between 50 - 100')
else:
    print (a, 'is smaller than 50')
