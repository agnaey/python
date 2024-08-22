std=[]
while True:
    print(
    '''
    1.add
    2.view
    3.update
    4.delete
    5.exit
    '''
    )
    choice=int(input('enter your choice : '))
    if choice==1:
        name=input('enter your name :')
        age=int(input("enter your age :"))
        mark=int(input("enter your mark :"))
        std.append([name,age,mark])
    elif choice==2:
        print('{:<10}{:<8}{:<8}'.format('name','age','mark'))
        print('-'*20)
        for i in std:
            print('{:<10}{:<8}{:<8}'.format(i[0],i[1],i[2]))
    elif choice==3:
        name=input('enter your name : ')
        f=0
        for i in std:
            if name in i:
                new_mark=int(input('enter your new mark: '))
                i[2]=new_mark
                f=1
        if f==0:
            print("name is not in the list")
    elif choice==4:
        name=input("enter name you want to delete : ")
        f=0
        for i in std:
            if name in i :
                std.remove(i)
                f=1
        if f==0:
            print('name not found')

    elif choice==5:
        break
    else:
        print('invalid number')
