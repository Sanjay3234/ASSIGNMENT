'''
# Question 1 = Make a calculator to select the choice to perform multiple operation
name=input("PLEASE ENTER YOUR NAME =")
while name.isalpha()==False or len(name)<8 :
    if ' ' in name:
        break
    else:
        print("THE NAME YOU ENTERED IS INCORRECT")
    name=input("ENTER THE NAME AGEIN =")
print("HELLO SIR ! NOW YOU CAN USE THE CALCULATOR FOR FOLLOWING OPERATIONS")
print("Select the operation you want to perform")
print("1.Add    2.Subtract     3.Multiply      4.Divide     5.Reminder     6.Quotient      7.Power")
Choice=int(input("Enter your choice(1/2/3/4/5/6/7):"))
if Choice == 1:
    num1 = int(input("Enter first number ="))
    num2 = int(input("Enter second number ="))
    sum=num1+num2
    print("Sum of num1 and num2 =",num1+num2)
elif Choice == 2:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Difference=num1-num2
    print("Difference of num1 and num2 =", num1 - num2)
elif Choice == 3:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Multiplication=num1*num2
    print("Multiplication of num1 and num2 =", num1 * num2)
elif Choice == 4:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Divide=num1/num2
    print("Division of num1 and num2 =", num1 / num2)
elif Choice == 5:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Quotiend=num1//num2
    print("Quotient after dividing num1 and num2 =", num1 // num2)
elif Choice == 6:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    Reminder=num1%num2
    print("Reminder after dividing num1 and num2 =", num1 % num2)
elif Choice == 7:
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    power=num1**num2
    print("Power of num1 by num2 =", num1 ** num2)
#Question 2 = to check entered year is leap year or not.
    year=int(input("enter the value of year ="))
if year%4==0:
    print(year,"is leap")
elif year%100==0:
    print(year,"yearis leap")
elif year%400==0:
    print(year,"is leap")
else:
    print(year,"is not leap")'
#Question 3 = ask from user naem,age and mobile number and should be valid [ isdigit(),isalpha() and isnull() ]
# validation name
name=input("enter your name =")
if name.isalpha()==True and len(name)>7 or ' ' in name:
    print(name, "valid")
else:
    print(name, "is invalid")
age=input("enter your age =")
# validation age
if age.isnumeric()==True and int(age)>=18 or ' ' in age:
#Question 4 = to identify which polygon figure is the entered value shows
AB=int(input("enter the length ="))
BC=int(input("enter the breadth ="))
CD=int(input("enter the length ="))
AD=int(input("enter the breadth ="))
if AB==CD and BC==AD:#AB==BC==CD==AD:
    print("it is a rectangle")
elif AB==BC==CD==AD:#AB==CD and BC==AD:
    print("It is a square")
else:
    print("entered value is no match the condition ")
    print(age,"valid")
else:
    print(age, "is invalid")
# validation mobile
mobile=input("enter your mobile number =")
if mobile.isnumeric()==True and len(mobile)==10 or ' ' in mobile:
    print(mobile,"valid")
else:
    print(mobile, "is invalid")
'''