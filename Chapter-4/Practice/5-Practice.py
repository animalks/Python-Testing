#! /usr/bin/python3
Peter = 0
Nancy = 0
Mary = 0

for i in range(6):
    print("1: Peter")
    print("2: Nancy")
    print("3: Mary")

    while True:
        X = int(input("Please choose your preference: "))
        if 1 <= X <= 3:
            break
        else:
            print("Invalid input. Please choose only 1-3.")

    if X == 1:
        Peter += 1
    elif X == 2:
        Nancy += 1
    elif X == 3:
        Mary += 1

print("Peter:", Peter)
print("Nancy:", Nancy)
print("Mary:", Mary)

