"""Write a Python program to get the Fibonacci series between 0 to 50.
 Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before i
"""

x,y = 0,1 #--> Assingning variables

while y<50:
    print(y)
    x,y = y, x+y