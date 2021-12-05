"""WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
"""
maths=float(input("Enter the marks of maths:"))
english=float(input("Enter the marks of english:"))
chemistry=float(input("Enter the marks of chemistry:"))
physics=float(input("Enter the marks of physics:"))
total_marks=400
marks_obtained=maths+english+chemistry+physics
percentage=marks_obtained/total_marks*100
if(percentage>70):
    print("you got distinction")
elif(percentage>60):
    print("you got first divison")
elif(percentage>40):
    print("you are passed")
elif(percentage<40):
    print("you are failed")   

    