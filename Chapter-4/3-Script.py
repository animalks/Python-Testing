#! /usr/bin/python3
n = 1
while n > 0:
    b = int(input("Would you like to continue? Press 1 to continue or 0 to exit: "))
    if b == 0:
        n = 0
    else:
        n = n + 1

print("You have terminated the connection")

