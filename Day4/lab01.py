#Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.

year=int(input("enter year to be checked:"))
if (year % 4 ==0 and year % 100 !=0 or year % 400 ==0):
    print("the year is a leap year")
else:
    print("the yar is leap year")