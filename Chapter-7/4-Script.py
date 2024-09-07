#! /usr/bin/python3
WORD = {}
while True:
    n = str(input())
    if n == "enddd" :
        break
    WORD[n] = WORD.get(n, 0) + 1
print (WORD)

