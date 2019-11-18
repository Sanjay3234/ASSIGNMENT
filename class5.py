'''
#Question 1 = Write a program to print the multiplication table of the number entered by the user?
num =3
for i in range (1,10):
        print(num,"*",i,"=",num*i)
#Question 2 = Ask the user to enter 10 numbers using only one input statement and add them to the List.
number=input("Enter multiple value: ").split()
x=number
print("Number of list is: ",x)
#Question 3 = From a list of numbers make a new list containing only the even numbers.
list1=[1,2,3,4,5,6,7,8,9,10]
print("the value of list1 =",list1)
num=[]
for num1 in list1:
    num2=num1
    if num2 % 2==0:
         num.append(num2)
print("even number in the list are",num)
#Question 4 = From a list separate the integers , strings and floats elements into three different lists.
import sys
list=[1,2,3,0,4,9.8,3.7,6.8,"nishan","sanjay","suwas","bhagat"]
list1=[]
list2=[]
list3=[]
for x in list:
    if type(x)==int:
        list1.append(x)
    elif type(x) ==float:
        list2.append(x)
    elif type(x)==str:
        list3.append(x)
else:
        sys.exit
print("list1=",list1)
print("list2=",list2)
print("list3=",list3)
#Question 5 = From a list ask the user the number he wants to remove from the list and then print the list.
list1=[1,2,3,4.6,5.9,6.7,"nishan","sanjay"]
index=int(input("enter the index ="))
if index in list1>7:
    del list1[index]
    print("list1=",list1)
else:
    print("out of range")
 '''