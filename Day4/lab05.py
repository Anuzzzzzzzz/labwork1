"""
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not
"""

a = int(input("Number of class held: "))
b = int(input(("Number of class attend: ")))

print(f"Total classes held till date:{a}.")
print(f"You attend {b} out of {a} classes.")

percentage = round(b / a * 100)

print(f"Your percentage is {percentage}%")

if percentage < 75:
    print("You are not allowed to sit in exam. ")
else:
    pass
