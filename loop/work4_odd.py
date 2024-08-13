# a=int(input("enter a startimg no : "))
# b=int(input("enter a ending no : "))
# while a<=b:
#     if a%2==1:
#         print(a)
#     a+=1  








a=int(input("enter a startimg no : "))
b=int(input("enter a ending no : "))
h=a
x=0
while a<=b:
    if a%2==1:
        x=x+a
    a+=1  
print(x)   