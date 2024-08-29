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
        print('{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}'.format('id','name','age','place','phone','position','salary'))
        print('-'*100)
        for i in emp:
            print('{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}'.format(i['id'],i['name'],i['age'],i['place'],i['phone'],i['position'],i['salary']))
    elif ch==3:
        id=int(input('enter employe ID :'))
        f=0
        for i in emp:
            if 'id' in i:
                f=1
                while True:
                    print(
                        '''
1.Update ID
2.Update Age
3.update place
4.update phone
5.update position
6.update salary
7.exit
                        '''
                    )
                    ch=int(input('enter your choise :'))
                    if ch==1:
                        new_id=int(input('enter new ID:'))
                        i['id']=new_id
                    elif ch==2:
                        new_age=int(input('enter new age:'))
                        i['age']=new_id
                    elif ch==3:
                        new_place=input('enter new place :')
                        i['place']=new_place
                    elif ch==4:
                        new_phone=int(input('enter new phone no:'))
                        i['phone']=new_phone
                    elif ch==5:
                        new_position=input('enter new position:')
                        i['position']=new_position
                    elif ch==6:
                        new_salary=int(input('enter new salary:'))
                        i['salary']=new_salary
                    elif ch==7:
                        break
                    else:print('invalid')
    elif ch==4:
        id=int(input('enter the employe to remove:'))
        f=0
        for i in emp:
             if i['id']==id:
                f=1
                emp.remove(i)
        if f==0:
            print('employe not found')
    elif ch==5:
        id=int(input('enter employe ID:'))
        f=0
        for i in emp:
            if i['id']==id:
                f=1
                task=input('enter the task:')
                date=datetime.datetime.now().strftime("%x")
                days=int(input('how many days :'))
                i['task']=[task,date,days]
            if f==0:
                print('employ not found')
    elif ch==6:
        id=int(input('enter employe id :'))
        f=0   
        for i in emp:
            if i['id']==id:
                f=1
                print('{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}'.format('id','name','age','place','phone','position','salary'))
                print('{:<10}{:<20}{:<8}{:<20}{:<13}{:<15}{:<20}'.format(i['id'],i['name'],i['age'],i['place'],i['phone'],i['position'],i['salary']))
                print('work detals')
                if 'task' in i:
                    print(i['task'])
                else:
                    print('no work avalible')
        if f==0:
            print('employe not found')
    elif ch==7:
        break
    else:print('invalid no')
   
                
     
                    



