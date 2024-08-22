employe=[]
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
    ch=int(input('enter your choice :'))
    if ch==1:
        id=int(input('enter ID :'))
        name=input('enter name of the Employe :')
        age=int(input("enter the Age of Employe :"))
        place=input("enter the Place of Employe :")
        phone=int(input("enter the Phone no of Employe :"))
        position=input("enter the Position of Employe :")
        salary=int(input("enter the Salary of Employe :"))
        employe.append([id,name,age,place,phone,position,salary])
    elif ch==2:
        print('{:<10}{:<20}{:<8}{:<20}{:<15}{:<15}{:<20}'.format('id','name','age','place','phone','position','salary'))
        print('-'*100)
        for i in employe:
            print('{:<10}{:<20}{:<8}{:<20}{:<10}{:<15}{:<20}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    elif ch==3:
        id=int(input("enter employe ID : "))
        f=0
        for i in employe:
            if id in i :
                f=1
                while True:
                    print(
                        '''
1.Update ID
2.Update Age
3.Update Mobile no
4.Update Position
5.Update Salary
6.Exit
                        '''
                    )
                    ch=int(input('enter your choice :'))
                    if ch==1:
                        new_id=int(input('enter new employe id :'))
                        i[0]=new_id
                    elif ch==2:
                        new_age=int(input('enter the new age of the employe'))
                        i[2]=new_age
                    elif ch==3:
                        new_mobile=int(input('enter the new mobie no of the employe'))
                        i[3]=new_mobile
                    elif ch==4:
                        new_Position=int(input('enter the new Position of the employe'))
                        i[4]=new_Position
                    elif ch==5:
                        new_Salary=int(input('enter the new Salary of the employe'))
                        i[4]=new_Salary
                    elif ch==6:
                        break
                    else:
                        print('invalid number')

            