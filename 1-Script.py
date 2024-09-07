#! /usr/bin/python3
ABC = []
while True:
    n = int(input())
    if n == -999:
        break
    ABC.append(n)

print (ABC)
print (len(ABC))
print (max(ABC))
print (min(ABC))
print (sum(ABC))
