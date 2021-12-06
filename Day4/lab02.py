#Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.

input_a=int(input("enter the first number"))
input_b=int(input("enter the second number"))
input_c=int(input("enter the third number"))

if (input_a==input_b) or (input_b==input_c):
    print("zero")
else:
    print("sum:", input_a+input_b+input_c)