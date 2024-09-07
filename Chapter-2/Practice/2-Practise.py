#! /usr/bin/python3
a = int(input('Please enter an number: '))
if (a%3 == 0) and (a%5 == 0):
    print (a , 'is an multiple of 3 and 5')
elif (a%3 == 0):
    print (a , 'is an multiple of 3')
elif (a%5 == 0):
    print (a, 'is  an multiple of 5')
else:
    print (a, 'is not an multiple of 3 and 5')

