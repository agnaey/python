import datetime
emp=[]
while True:
    print(
    '''
    1.Register Employe
    2.Display Employe
    3.Update Employe details
    4.Delete Employe
    5.task
    6.search
    7.exit
    '''
    )
    ch=int(input('enter your choise :'))
    if ch==1:
        id=int(input('enter ID :'))
        name=input('enter name of the Employe :')
        age=int(input("enter the Age of Employe :"))
        place=input("enter the Place of Employe :")
        phone=int(input("enter the Phone no of Employe :"))
        position=input("enter the Position of Employe :")
        salary=int(input("enter the Salary of Employe :"))
        emp.append({'id':id,'name':name ,'age':age,'place':place,'phone':phone,'position':position,'salary':salary})
    elif ch==2:
        print('{:<10}{:<20}{:<8}{:<20}{:<10}{:<15}{:<20}'.format('id','name','age','place','phone','position','salary'))
        print('-'*100)
        for i in emp:
            print('{:<10}{:<20}{:<8}{:<20}{:<10}{:<15}{:<20}'.format(i['id'],i['name'],i['age'],i['place'],i['phone'],i['position'],i['salary']))
