#! /usr/bin/python3
import os
print ("\033[1;34;40m This is the Start of the Ping Test")
print ("\033[0m ")
AA = (input("Please enter the first IP address: "))
BB = (input("Please enter the second IP address: "))
CC = (input("Please enter the third IP address: "))

IP = [AA, BB, CC]
for x in IP:
    result = os.system('ping -c 3 -W 1 ' + str(x))
    if result is 0:
        print("\033[1;32m Connection OK")
        print("\033[0m --------------------------------------------------------------------------------------------------")
    else:
        print("\033[1;31;40m Connection failed")
        print("\033[0m --------------------------------------------------------------------------------------------------")

