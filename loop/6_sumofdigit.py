num=int(input("enter a no : "))
i=1
x=0
sum=0
while num>0:
    x=num%10
    sum=(sum+x)
    num=num//10
print(sum)