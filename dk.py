def plaindrome(num):
    a=num
    reverse=0
    while num>0:
        reminder=num%10
        #num=num//10
        reverse=reverse*10+reminder
        num = num // 10
    if a==reverse:
        print(a," is an armstrong number")
    else:
        print(a," is not an armstrng number")
num1=int(input("enter the value of num ="))
plaindrome(num1)