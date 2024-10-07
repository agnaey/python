import sqlite3
con=sqlite3.connect('python/sqlite3/work1.db')
try:
    con.execute('create table emp(id int,name text,position text,age int,place text,phone int)')
except:
    print('table already exits')

emp=[]
while True:
    print('''
        1.add
        2.view
        3.update
        4.delete
        5.search
''')
    ch=int(input(' enter your choise:'))
    if ch==1:
        id=int(input('enter the id:'))
        name=input('enter name of the Employe :')
        position=input("enter the Position of Employe :")

        age=int(input("enter the Age of Employe :"))
        place=input("enter the Place of Employe :")
        phone=int(input("enter the Phone no of Employe :"))
        emp.append({'id':id,'name':name ,'position':position,'age':age,'place':place,'phone':phone})
        con.execute('insert into emp(id,name,position,age,place,phone)values(?,?,?,?,?)',(id,name,position,age,place,phone))
        con.commit()
    
    