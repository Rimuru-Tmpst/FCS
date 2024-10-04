

# 1. Write a program that takes two integers from the user and outputs the range of values from this list

list1 = [54,76,2,4,98,100]
int1 = int(input("enter the first integer: "))
int2 = int(input("enter the second integer: "))

if int1 > int2:
    int1, int2 = int2, int1
for num in list1:
    if int1 <= num <= int2:
        print(num)