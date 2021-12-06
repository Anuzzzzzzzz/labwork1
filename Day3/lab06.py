#Given an integer number, print its last digit. 
end_user = int(input("Enter an integer: "))

last_digit = end_user % 10

print(f"{last_digit} is the last digit of the given integer.")