#! /usr/bin/python3
A1 = ()
B1 = ()

while True:
    n = int(input("A add: "))
    if n == -999:
        break
    A1 = A1 + (n,)

while True:
    n = int(input("B add: "))
    if n == -999:
        break
    B1 = B1 + (n,)

print (A1)
print (B1)

C1 = (A1) + (B1)

print (C1)

D1 = sorted(C1)
print (D1)
