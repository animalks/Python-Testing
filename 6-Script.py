#! /usr/bin/python3
PPP = str(input())
BBB = set(PPP.lower())
print (BBB)
BBB.remove(' ') 
BBB.remove('.') 
BBB.remove(',') 
print (BBB)

if len(BBB) == 26:
    print ("Good")
else:
    print ("Bad")
