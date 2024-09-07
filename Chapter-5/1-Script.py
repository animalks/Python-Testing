#! /usr/bin/python3
for i in range (1, 5):
    print ('*', end = ' ')
print ()
for i in range (1, 10):
    print ('*', end = ' ')
print ()
for i in range (1, 15):
    print ('*', end = ' ')

print ()
print ('=====================================')

def FIRST (n):
    for i in range (1, n):
        print ('*', end = ' ')
    print ()

def main ():
    FIRST (5)
    FIRST (10)
    FIRST (15)
main ()
