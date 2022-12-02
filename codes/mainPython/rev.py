#reverse of a number
rev=0
num=int(input("enter the number"))
while(num>0):
    rem=num%10
    num=num//10
    rev=rev*10+rem
    print("reverse is",rev)