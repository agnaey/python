def number():
        a=int(input('enter a no:'))
        b=int(input('enter another no:'))
        return a,b
def add():
     a,b=number()
     print(a+b)
def sub():
     a,b=number()
     print(a-b)
def mul():
     a,b=number()
     print(a*b)
def div():
     a,b=number()
     print(a/b)
def mod():
     a,b=number()
     print(a%b)


while True:
    print(
        '''
1.add
2.sub
3.mul
4.div
5.mod
6.exit
'''
    )
    ch=int(input('enter your choise:'))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        div()
    elif ch==5:
        mod()
    elif ch==6:
        break
    else:print('invalid no')
