#. Write a program to find the factorial of a number.

class Test():
    def factorial(self, n):
        f = 1
        for i in range(1, n+1):
            f = f * i
        return f
n = int(input("Enter a number: "))

obj = Test()
f = obj.factorial(n)
print("Factorial is: ", f)