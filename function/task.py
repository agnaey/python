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
    id=input("Enter your id :")
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
            password=name
            emp.append({'id':id,'name':name ,'age':age,'place':place,'phone':phone,'position':position,'salary':salary,'password':password})
            print(".....Employee added.....")
    if f1==0:
        print("Employee not found")
    
def display_emp():
    print("{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}{:<10}".format('id','name','age','place','phone','position','salary','password'))
    print('-'*100)
    for i in emp:
        print("{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}{:<10}".format(i['id'],i['name'],i['age'],i['place'],i['phone'],i['position'],i['salary'],i['password']))
    print()

while True:
    