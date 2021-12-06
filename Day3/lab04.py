#Given three integers, print the smallest one. (Three integers should be user input) 

user_1 = int(input("Enter the 1st integer: "))
user_2 = int(input("Enter the 2nd integer: "))
user_3 = int(input("Enter the 3rd integer: "))

if (user_1 <= user_2 and user_1 <= user_3):
    print(user_1, "is the smallest.")
elif (user_2 <= user_1 and user_2 <= user_3):
    print(user_2, "is the smallest")
else:
    print(user_3, "is the smallest.")