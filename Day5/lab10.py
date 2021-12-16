#.Write a Python program that accepts a string and calculate the number of digits and letters
string = input("Enter any string: ")

num_digit = 0
num_letters = 0

for i in string:
    if i.isdigit():
        num_digit = num_digit+1
    elif i.isalpha():
        num_letters = num_letters +1
else:
    print(f"Num of digit:{num_digit} , Num of letter: {num_letters} ")