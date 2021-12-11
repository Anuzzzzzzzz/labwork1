"""
Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR".
"""

gender=input("Enter your gender here: ").lower()
age=int(input("Enter your age here: ").lower())

if gender=='female':
    print("She will work only in urban areas.")
elif gender=='male' and  20 < age < 40:
    print("He can any where he wants :)")
elif gender=='male' and 40 > age > 60:
    print("He will work in urban areas only.")
else:
    print("Error")