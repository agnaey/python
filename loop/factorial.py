num=int(input("enter a no : "))
no=num
i=1
fact=1
while num>1:
    fact=fact*num
    num-=1
print(f"factorial of this {no} is {fact}")