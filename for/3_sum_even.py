a=int(input("enter a no : "))
b=int(input("enter a no : "))
x=0
for a in range (a,b+1):
    if a%2==0:
        x=x+a
print(x)