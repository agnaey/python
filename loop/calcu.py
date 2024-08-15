while True:
    print('''
1.add
2.subtraction
3.multiplication
4.division
5.Floor division
6.modulus
7.exponent
8.exit
''')
    choise=int(input("enter your choise : "))
    if choise==1:
        a=int(input("enter a no : "))
        b=int(input("enter another no : "))
        print(a+b)
    elif choise==2:
        a=int(input("enter a no : "))
        b=int(input("enter another no : "))
        print(a-b)
    elif choise==3:
        a=int(input("enter a no : "))
        b=int(input("enter another no : "))
        print(a*b)
    elif choise==4:
        a=int(input("enter a no : "))
        b=int(input("enter another no : "))
        print(a/b)
    elif choise==5:
        a=int(input("enter a no : "))
        b=int(input("enter another no : "))
        print(a//b)
    elif choise==6:
        a=int(input("enter a no : "))
        b=int(input("enter a no :"))
        print(a%b)
    elif choise==7:
        a=int(input("enter a no : "))
        b=int(input("enter a no :"))
        print(a**b)
    elif choise==8:
        break
    else:
        print("invalid number")
