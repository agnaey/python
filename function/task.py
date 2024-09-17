emp=[]

def login():
    username=input('enter username :')
    password=input('enter password :')
    f=0
    user=''
    if username=='admin' and password=='admin':
        f=1
        print('welcome',username)
    for i in emp:
        if i['id']==username and i['password']==password:
            f=2
            user=i
    return f,user
def add_emp():
    id=input("Enter the id :")
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            print("Employee already exists")
    if f1==0:
            name=input("Enter the name :")
            age=int(input("Enter the age :"))
            place=input("Enter the place :")
            phone=int(input("Enter the phone :"))
            position=input("Enter the position :")
            salary=int(input("Enter the salary :"))
            password=name
            emp.append({'id':id,'name':name ,'age':age,'place':place,'phone':phone,'position':position,'salary':salary,'password':password})
            print(".....Employee added.....")


    
def display_emp():
    print("{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}{:<10}".format('id','name','age','place','phone','position','salary','password'))
    print('-'*100)
    for i in emp:
        print("{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}{:<10}".format(i['id'],i['name'],i['age'],i['place'],i['phone'],i['position'],i['salary'],i['password']))
        print('-'*100)

    print()

def delete_emp():
    id=input("Enter your id :")
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            emp.remove(i)
            print(".....Employee deleted.....")
    if f1==0:
            print("Employee not found")

def emp_update():
    id=input("Enter the id :")
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            name=input("Enter the name :")
            age=int(input("Enter the age :"))
            place=input("Enter the place :")
            phone=int(input("Enter the phone :"))
            position=input("Enter the position :")
            salary=int(input("Enter the salary :"))
            i['name']=name
            i['age']=age
            i['place']=place
            i['phone']=phone
            i['position']=position
            i['salary']=salary
            print(".....Employee updated.....")
    if f1==0:
        print("Employee not found")

def view_profile():
    print("{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}{:<10}".format('id','name','age','place','phone','position','salary','password'))
    print('-'*100)
    for i in emp:
        print("{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}{:<10}".format(i['id'],i['name'],i['age'],i['place'],i['phone'],i['position'],i['salary'],i['password']))

def edit_profile():
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            name=input("Enter your name :")
            age=int(input("Enter your age :"))
            place=input("Enter your place :")
            phone=int(input("Enter your phone :"))
            position=input("Enter your position :")
            salary=int(input("Enter your salary :"))
            i['name']=name
            i['age']=age
            i['place']=place
            i['phone']=phone
            i['position']=position
            i['salary']=salary
            print(".....edited.....")
    if f1==0:
        print("Employee not found")




while True:
    print(
        ''''
        1.login
        2.exit
        '''
    )
    ch=int(input('enter your choise :'))
    if ch==1:
        f,user=login()
        #admin
        if f==1:
            while True:
                print(
                    '''
                    1.add employee
                    2.display employee
                    3.delete employee
                    4.update employee
                    5.logout
                    '''
                )
                ch=int(input('enter your choise :'))
                if ch==1:
                    add_emp()
                elif ch==2:
                    display_emp()
                elif ch==3:
                    display_emp()
                elif ch==4:
                    emp_update()
                elif ch==5:
                    print('.....exited.....')
                    break
        elif f==0:
            print('invalid user or password')
        elif f==2:
            while True:
                if user['name']==user['password']:    
                    print('create new password')
                    password=input('enter password :')
                    user['password']=password
                    print('password created')
                else:
                    print(
                        '''
                        1.view profile
                        2.edit profile
                        3.logout
'''
                    )
                    cho=int(input('enter your choise :'))
                    if cho==1:
                        view_profile(user)
                    elif cho==2:
                        edit_profile(user)
                    elif cho==3:
                        print('.....exited.....')
                        break
    elif ch==2:
        print('.....exited.....')
        break
        


    