emp=[]
def login():
    uname=input('ener your user name: ')
    passwrd=input('ener your password: ')
    f=0
    user=''
    if uname=='admin' and passwrd=='admin':
        f=1
    for i in emp:
        if i['id']==uname and i['password']==passwrd:
            f=2
            user=i
    return f,user

def add_emp():
    id=str(input('enter your id: '))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            print('existing id')
            add_emp()
    if f1==0:
        name=input('enter your name: ')
        age=int(input('enter your age: '))
        salary=int(input('enter your salary: '))
        place=input('enter your place: ')
        dob=int(input('enter your date of birth: '))
        password=dob
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'date_of_birth':dob,'password':password})
        print('Employee added successfully')
def update():
    id=str(input('enter your id: '))
    f2=0
    for i in emp:
        if i['id']==id:
            f2=1
            name=(input('enter your name: '))
            age=int(input('enter your age: '))
            salary=int(input('enter your salary: '))
            place=(input('enter your place: '))
            dob=(input('enter your date of birth: '))
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['date_of_birth']=dob
            print('updated successfully')
    if f2==0:
        print('invalid id!!!')
def delete():
    id=input('enter your id: ')
    f3=0
    for i in emp:
        if i['id']==id:
            f3=1
            emp.remove(i)
            print('REMOVED!!!')
    if f3==0:
        print('invalid id!!!')
def display():
    print('_'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format('id','name','age','salary','place','date of birth'))
    print('-'*65)
    for i in emp:
            print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format(i['id'],i['name'],i['age'],i['salary'],i['place'],i['date_of_birth']))
def view_profile(user):
    # print(user)
    print('_'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format('id','name','age','salary','place','date of birth'))
    print('-'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format(user['id'],user['name'],user['age'],user['salary'],user['place'],user['date_of_birth']))
def user_update(user):
    f4=0
    for i in emp:
        if i['id']==user['id']:
            f4=1
            name=input('enter the updatede name: ')
            age=int(input('enter your age: '))
            place=(input('enter your place: '))
            dob=(input('enter your date of birth: '))
            i['name']=name
            i['age']=age
            i['place']=place
            i['date_of_birth']=dob
            print('updated successfully...')
    if f4==0:
        print('invalid id!!!!')
    
while True:
    print('''
    1.login
    2.exit''')
    choice=int(input('enter the  choice: '))
    if choice==1:
        f,user=login()
        if f==1: #admin login
            while True:
                print('''
                    1.add emp
                    2.update emp
                    3.delete
                    4.diplay
                    5.logout
                    ''')
                sub_choice=int(input('enter your choice: '))
                if sub_choice==1:
                    add_emp()
                elif sub_choice==2:
                    update()
                elif sub_choice==3:
                    delete()
                elif sub_choice==4:
                    display()
                elif sub_choice==5:
                    break
                else:
                    print('invalid choice')
        elif f==0:
            print('invalid username or passsword!!!')
        elif f==2: #user login
            while True:
                if user['date_of_birth']==user['password']:
                    password=input('enter a new password')
                    user['password']=password
                else:
                    print('''
                        1.view profile
                        2.edit profile
                        3.logout
    ''')
                    sub_ch=int(input('enter your choice: '))
                    if sub_ch==1:
                        view_profile(user)
                    elif sub_ch==2:
                        user_update(user)
                    elif sub_ch==3:
                        break 
    elif choice==2:
        break