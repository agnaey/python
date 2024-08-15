num=int(input("enter a no : "))
rev=0
for i in range (num):
    if num<=0:
        break
    x=num%10
    rev=(rev*10)+x
    num=num//10
print(rev)