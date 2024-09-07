#! /usr/bin/python3
import random
word  = random.randint(1, 100)
if (word%2==0):  
    print ('Even', word)
else:
    print ('Odd', word)
