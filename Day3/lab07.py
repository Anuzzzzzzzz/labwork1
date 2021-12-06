#Given a positive real number, print its fractional part. 


number = float(input("Enter any positive number : "))
friction_number =number%(number/number)
print(f"Frictional Part of {number//number} is : {friction_number}")