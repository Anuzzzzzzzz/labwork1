"""
    .Write a Python program to construct the following pattern, 
    using a nested for loop.
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
"""

for i in range(10):
    print("")
    if i <=5:
        for j in range(i):
            print("*",end="")
    else:
        for k in range(10-i):
            print("*",end="")