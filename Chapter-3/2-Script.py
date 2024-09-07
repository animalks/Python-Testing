#! /usr/bin/python3
import os
i = 0
while i < 10:
    i=i + 1
    os.system('ping -c 1 192.168.1.' + str(i))

