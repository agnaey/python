import mysql.connector
con = mysql.connector.connect(host='localhost',user='agnaey',password='agnaey',database='agnaeydatas')
con.autocommit=True               ## to commit without typing it again & again
cur = con.cursor()
# cun.execute('create database agnaeydatas')         ## to create table in mysql
try:
    cur.execute("create table std (roll_no int,name text,age int)")
except:
    print('table already exits')

# roll_no=int(input('enter the roll no: '))
# name=input('enter your name: ')
# age=int(input('enter your age:'))
# cur.execute('insert into std (roll_no,name,age) values(%s,%s,%s)',(roll_no,name,age))

'''    update '''
# name=(input('enter your name:'))
# u_name=(input('enter new name:'))
# cur.execute('update std set name=%s where name =%s',(u_name,name))


'''delete'''

# roll_no=int(input('delete roll no:'))
# cur.execute('delete from std where roll_no=%s',(roll_no,))

'''search'''
# roll_no=int(input('enter the roll no:'))
# cur.execute('select * from std where roll_no=%s',(roll_no,))
# print('{:<10}{:<20}{:<10}'.format('roll_no','name','age'))
# print('-'*35)
# for i in cur:
#     print('{:<10}{:<20}{:<10}'.format(i[0],i[1],i[2]))

'''view'''
cur.execute('select * from std')
print('{:<10}{:<20}{:<10}'.format('roll_no','name','age'))
print('-'*35)
for i in cur:
    print('{:<10}{:<20}{:<10}'.format(i[0],i[1],i[2]))





