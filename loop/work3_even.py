a=int(input("enter a starting no : "))
b=int(input("enter a ending no : "))
x=0
while a<=b:
    if a%2==0:
        x=x+a
    a+=1
print(a,x)