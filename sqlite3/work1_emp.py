import sqlite3
con=sqlite3.connect('python/sqlite3/work1.db')
try:
    con.execute('create table emp(id int,name text,position text,age int,place text,phone int)')
except:
    print('table already exits')

while True:
    print('''
        1.add
        2.view
        3.update
        4.delete
        5.search
        6.exit
''')
    ch=int(input(' enter your choise:'))
    if ch==1:
        id=int(input('enter the id:'))
        name=input('enter name of the Employe :')
        position=input("enter the Position of Employe :")
        age=int(input("enter the Age of Employe :"))
        place=input("enter the Place of Employe :")
        phone=int(input("enter the Phone no of Employe :"))
        con.execute('insert into emp(id,name,position,age,place,phone)values(?,?,?,?,?,?)',(id,name,position,age,place,phone))
        con.commit()
    elif ch==2:
        data=con.execute('select * from emp')
        print('{:<10}{:<20}{:<15}{:<10}{:<15}{:<20}'.format('id','name','position','age','place','phone'))
        print('-'*80)
        for i in data:
            print('{:<10}{:<20}{:<15}{:<10}{:<15}{:<20}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif ch==3:
        id=int(input('enter the id:'))
        f=0
        data=con.execute('select * from emp')
        for i in data:
            if i[0]==id:
                f=1
                while True:
                    print('''
                        1.update name
                        2.update position
                        3.update age
                        4.update place
                        5.update phone
                        6.exit
                    ''')
                    ch=int(input('enter your choise:'))
                    if ch==1:
                        name=input('enter name of the Employe :')
                        con.execute('update emp set name=? where id=?',(name,id))
                    elif ch==2:
                        position=input("enter the Position of Employe :")
                        con.execute('update emp set position=? where id=?',(position,id))
                    elif ch==3:
                        age=int(input("enter the Age of Employe :"))
                        con.execute('update emp set age=? where id=?',(age,id))
                    elif ch==4:
                        place=input("enter the Place of Employe :")
                        con.execute('update emp set place=? where id=?',(place,id))
                    elif ch==5:
                        phone=int(input("enter the Phone no of Employe :"))
                        con.execute('update emp set phone=? where id=?',(phone,id))
                    elif ch==6:
                        break
                    else:print('invalid')
                con.commit()
    elif ch==4:
        id=int(input('enter the id:'))
        data=con.execute('delete from emp where id=?',(id,))
        con.commit()
        print('-----------deleted---------')
    elif ch==5:
        id=int(input('enter the id:'))
        data=con.execute('select * from emp where id=?',(id,))
        print('{:<10}{:<20}{:<15}{:<10}{:<15}{:<20}'.format('id','name','position','age','place','phone'))
        print('-'*80)
        for i in data:
            print('{:<10}{:<20}{:<15}{:<10}{:<15}{:<20}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    else:
        break


    
    