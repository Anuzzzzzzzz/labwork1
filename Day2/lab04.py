"""
 N students take K apples and distribute them among each other evenly. The remaining
(the indivisible) part remains in the basket. How many apples will each single student
get? How many apples will remain in the basket? The program reads the numbers N and
K. It should print the two answers for the questions above.
"""
no_of_students = int(input("Enter No of Students : "))
no_of_apples = int(input("Enter No of Apples : "))
each_student_gets = no_of_apples // no_of_students
baskets = no_of_apples - (each_student_gets*no_of_students)
if no_of_apples < no_of_students:
 print("Sablai Pugne Gari Ta lyauna parchha ni ")
else:
 print(f"Each Students Gets {each_student_gets} Apples and {baskets} Remains in Basket ")
 