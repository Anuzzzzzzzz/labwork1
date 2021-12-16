#Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)


F = float(input("Enter tempreature in Fahrenhiet: "))
c = float(input("Enter tempreature in celcius: "))

fahrenheit = (5/9) * (F - 32) 
celcius = (5/9) * (c - 32)

print(f"{fahrenheit} is tempreature in celius.")
print(f"{celcius} is tempreature in fahrenhiet.")