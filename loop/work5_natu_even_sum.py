a=int(input("enter a startig no"))
b=int(input("enter a ending no"))
start=a
x=y=z=0

while a<=b:
    x=x+a
    if a%2==0:
        y=y+a
    else:
        z=z+a
    a+=1
print(f"natural no {start},{b} is {x}")
print(f"natural no {start},{b} is {y}")
print(f"natural no {start},{b} is {z}")


