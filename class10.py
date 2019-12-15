# Question 1 :Write a program to create a user defined dictionary. User should enter the name of the key and the
#name of the value he wants for any number of keys.?
dic={}
a="yes"
while a=="yes":
    key=input("enter your key =")
value=input("enter the value for the key =")
if value.isdigit()==True:
    value=int(value)
else:
    value=value
dic[key]=value
a=input("do you want to add more =")
print(dic)
# Question 2 : Implement RegEx for Email ?