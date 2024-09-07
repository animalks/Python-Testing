#! /usr/bin/python3
a = eval(input('Mins:'))
b = eval(input('Seconds:'))
c = eval(input('Distance:'))

d = (c/1.6) / (a*60+b) * 60 * 60
print (d)
print("Speed = %.2f" % d)
