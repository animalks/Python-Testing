#! /usr/bin/python3
A = eval(input("First number"))

for x in range(1, 13):
      A  = A + A*5.75**1/1200
      print('After', (x), end = ' ')   
      print('month the total money is', (A))
