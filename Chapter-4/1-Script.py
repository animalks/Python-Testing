#! /usr/bin/python3
import random
output_list = []
for i in range(4):
    input("Please press enter, the " + str(i+1) + " person: ")
    A = random.randint(1,100)
    print ('%4d'%(A))
    output_list.append(A)

output1 = output_list[0]
output2 = output_list[1]
output3 = output_list[2]
output4 = output_list[3]

ZZ = max(output1, output2, output3, output4)
print (str(ZZ) + " is the largest number")
