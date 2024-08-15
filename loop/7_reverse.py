num=int(input("enter a no : "))
i=1
rev=0
while num>0:
    x=num%10
    rev=(rev*10)+x
    num=num//10
print(rev)