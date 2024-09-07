#! /usr/bin/python3
word  = (input('Please enter the first number: '))
if ('a' <= word <= 'z') or ('A' <= word <= 'Z'): 
    print ('This is a character') 
elif ('1' <= word <= '9'): 
    print ('This is a number')
else:
    print ('This ie  a symbol')
