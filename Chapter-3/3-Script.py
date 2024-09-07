#! /usr/bin/python3
import os
a = str(input())
i = 0
while i < 10:
    i=i + 1
    os.system('ping -c 1 -W 1 ' + str(a) + str(i))
    #os.system('ping -c 1', (a)  + str(i))

