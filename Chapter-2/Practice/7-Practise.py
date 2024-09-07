#! /usr/bin/python3
word  = int(input('Please enter the first number: '))
if (word > 38000):  
    print ('After discount the price is', word*0.7) 
elif (word > 28000):
    print ('After discount the price is', word*0.8)
elif (word > 18000):
    print ('After discount the price is', word*0.9)
elif (word > 8000):
    print ('After discount the price is', word*0.95)
else:
    print (word)
