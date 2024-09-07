#! /usr/bin/python3
import os
IP = ["192.168.1.2", "218.213.85.210", "10.2.3.2"]
for x in IP:
    print (x)
    os.system('timeout --signal=9 2 telnet ' + str(x) + ' 443')
    #os.system('ping -c 1', (a)  + str(i))
