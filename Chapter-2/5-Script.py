#! /usr/bin/python3

a = eval(input('Please input your weight in KG: '))
b = eval(input('Please input your height in M: '))
c = a/(b*b)
print ('Your BMI is', c)
if c > 24.9:
    print ('Your are overweight need reduce fat')
elif c < 18.5:
    print ('You are too thin, need gain more weight')
else:
    print ('You are in ideal weight')


