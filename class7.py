'''
# Question 1 : Write a program that copies content of one file to other file.
#write
f1=open("love.txt","w")
Name=input("My name is ")
Grade=input("I read in Grade ")
f1.writelines(Name+"\n")
f1.writelines(Grade)
f1.close()
#read
with open("love.txt","r") as f1:
    text=f1.read()
    print(text)
#copy
f2 = open ("nishan.txt","w")
f2.writelines(text)
f1.close()
f2.close()
# Question 2 : Write a program that corrects this [ Hello-This-is-a-text-file. ]
f1=open("school.txt","w")
text=input("enter your text to be replaced =")
f1.writelines(text)
f1.close()
f2=open("school.txt","r")
f3= open("college.txt","w")
for line in f2:
    text=line.replace("-"," ")
    f3.writelines(text)
f2.close()
f3.close()
'''
# Question 3 : Write a program to find prime  numbers from 1 to 2500 using list comprehension.

# Question 4 : Write a program that uses map to convert a list of temp in Fahrenheit to celsiu
#def celsius(f):
#   return (0.55)*(f-32)
#fahrenheit=[30,40,50,60,80]
#celcius=map(celsius,fahrenheit)
#print("Given Fahrenheit Degree =",fahrenheit)
#print("Fahrenheit Degree Converted into Celcius =",(list(celcius)))
# Question 5 : Write a program that creates three different types of errors and then write except statement for them.
# Question 6 : Write a program to create a user defined error whenever the string length is less than 3.