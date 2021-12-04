"""The program should read three integers:number of students in each of the three classes, a, b and c respectively
Suppose In the first test there are three groups. The first group has 20 students so they need 10 desks. 
The second group has 21 students, so they can get by with no fewer than 11 desks.
11 desks are also enough for the third group of 22 students. 
we need 32 desks in total.
"""
a_class = int(input("Enter Number of Students in a Class:"))
b_class = int(input("Enter Number of Students in b Class:"))
c_class = int(input("Enter Number of Students in c Class:"))
if a_class % 2 == 0:
    a_class_chairs = a_class/2
else:
    a_class_chairs =  (a_class//2 )+ 1
if b_class % 2 == 0 :
    b_class_chairs = b_class/2
else:
    b_class_chairs = (b_class//2)+1
if c_class %2 == 0:
    c_class_chairs = c_class/2
else:
    c_class_chairs = (c_class//2)+1
print(f"a Class Needs {a_class_chairs} Chairs\nb Class Needs {b_class_chairs} Chairs\nc Class Needs {c_class_chairs} Chairs\nIn Total We Need {a_class_chairs+b_class_chairs+c_class_chairs} Additional Chairs ")