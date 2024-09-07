#! /usr/bin/python3
n = 4
min = (input("Please input a first number:" ))
for i in range (n, 1, -1):
    #print (i)
    new_no = (input("Please input another number "))
    if new_no < min:
        min = new_no
    #    print (min)
print (min)
