##added exception handling on choise

std=[{'name': 'agnaey', 'age': '20', 'mark': '31'}, {'name': 'tutu', 'age': '21', 'mark': '12'}]
while True:
    print('''
1)add
2)view
3)update
4)delete
5)exit
'''
)
    while True:
        try:
            ch=int(input('enter a choise:'))
            break
        except:
            print('----enter correct data----')
    if ch==1:
        name=str(input('enter the name :'))
        age=str(input('enter the age :'))
        mark=str(input('enter the mark :'))
        std.append({'name':name,'age':age,'mark':mark})
        print(std)
    elif ch==2:
        print('{:<10}{:<8}{:<8}'.format('name','age','mark'))
        print('-'*20)
        for i in std:
            print('{:<10}{:<8}{:<8}'.format (i['name'],i['age'],i['mark']))
    elif ch==3:
        name=input('enter the name :')
        f=0
        for i in std:
            if i['name']==name:
                new_mark=int(input('enter the new mark :'))
                i['mark']=new_mark
                f=1
        if f==0:
            print('name is not in the list')
    elif ch==4:
        name=input('enter the name you want to delete :')
        for i in std:
            if i['name']==name:
                std.remove(i)
                f=1
        if f==0:
            print('invalid')
    elif ch==5:
        break
    else:print('invalid number')
    
            
            