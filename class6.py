'''
# Question 1 = Write a function to find the area ofa circle. The value of the radius must be entered by the user.
def circle(r,pi=3.142):
    return pi*r*r
radius = int(input ("enter the value or radius ="))
print("Area of a circle =",(circle(radius)))
circle(radius)
# Question 2 = write a function pow (a,b). The function should return the value a raised to the power of b.
# (a^b).Hint-: In python 2**3=8
def power(num1,num2):
    return num1**num2
number1=int(input("Enter the value of num1 ="))
number2=int(input("Enter the value of num2 ="))
print("Power or num1 =",power(number1,number2))
power(number1,number2)
# Question 3 = Write a function to test if a number entered by the user is Armstrong or not  Armstrong number.
# e.g. – 371 = 3^3 + 7 ^3 + 1^3 = 371
def armstrong(num):
    a=num
    w=a//10
    x=a%10
    y=w%10
    z=w//10
    sum=x**3+y**3+z**3
    if sum==num:
        print(num1,"= is an armstrong number")
    else:
        print(num1," is not an armstrng number")
num1=int(input("enter the value of num ="))
armstrong(num1)
# Question 4 = Write a function to check if a number is reverse of the number i.e.Palindrome e.g. – 12321 is palindrome.
def plaindrome(num):
    a=num
    reverse=0
    while num>0:
        reminder=num%10
       # num=num//10
        reverse=reverse*10+reminder
        num=num//10
    if a==reverse:
        print(a," is an armstrong number")
    else:
        print(a," is not an armstrng number")
num1=int(input("enter the value of num ="))
plaindrome(num1)
'''
