'''
# Question 1 : Using the OS Library change the name of a file.
#import os
#os.rename(r'C:\Users\SATHI\Downloads\Intern notes\skp.txt',r'C:\Users\SATHI\Downloads\Intern notes\DKP.txt')
# Question 2 : Using datetime library Print The current weekday, week, month and year in separate statements.
import datetime
day=datetime.date.today()
print("The curent weekday of year =",day.weekday())
print("The current month of year =",day.month)
print("The current year =",day.year)
# Question3 : Use two functions from the math Library.
import math
num=int(input("enter a number ="))
print("squareroot of the entered number =",int(math.sqrt(num)))
print("factorial of the entered number =",math.factorial(num))
#  Question 4 : Find more interesting Library. [ numpy = helps to find the cube root of any given number.
import numpy
num=int(input("enter the number ="))
print("cube root of given number =",int(numpy.cbrt(num)))
'''