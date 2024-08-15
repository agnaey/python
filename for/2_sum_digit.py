num=int(input("enter a no :"))

x=0
sum=0
for i in range (num):
    x=num%10
    sum=(sum+x)
    num=num//10
print (sum)