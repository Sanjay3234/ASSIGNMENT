'''''
# question 1 = five subject mark from user and input into list and ptint sum of all marks
mark=[]
math=int(input("enter the mark of math ="))
science=int(input("enter the mark of science ="))
nepali=int(input("enter the mark of nepali ="))
computer=int(input("enter the mark of computer ="))
social=int(input("enter the mark of social ="))
mark.append(math)
mark.append(science)
mark.append(nepali)
mark.append(computer)
mark.append(social)
print(mark)
OM=math+science+nepali+computer+social
print("obtained mark of five subject = ",OM)
#Question 2 = take input from the user and ask the user which string needs to be counted
user=input("enter a string = ")
user1=input("which stringneed u ant to count = ")
print(user1.count(user1))
# Question 3 = max and mi from the list
list1=[1,4,2,6,7]
print(max(list1))
print(min(list1))
# Qustion 4 = replace a word from the stringand convert the string in uppercase
Name="SANJAY KUMAR PANDIT"
print(Name)
print (Name.replace("SANJAY","AJAY"))
print(Name.swapcase())
s'''