import sqlite3
  ###'''   creating table                '''


con=sqlite3.connect('python/sqlite3/create.db')
try:
    con.execute('create table std(roll_no int,name text,age int,mark real)')
except:
    print('table already exits')

### to add values in table 
# con.execute('insert into std(roll_no,name,age,mark)values(1,"agnaey",21,40),(2,"akshay",20,42)')
# con.commit()    ##to save                                       ##        ^^^ you can add multiple pepl using comma and add again


limit=int(input('enter the limit:'))
for i in range(limit):
  roll=int(input('enter a no:'))
  name=input('enter your name:')
  age=int(input('enter your age:'))
  mark=float(input('enter your mark:'))
  con.execute('insert into std(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
  con.commit()

# ----------------------------

''' table in terminal'''

# data=con.execute('select * from std')
# print('{:<10}{:<20}{:<10}{:<10}'.format('roll_no','name','age','mark'))
# print('-'*47)
# for i in data:
#     print('{:<10}{:<20}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))


''' filter '''

# data=con.execute('select * from std where name="akshay" ')
# for i in data:
#   print(i)

 ##  user input filter
# roll=int(input('enter the age:'))
# data=con.execute('select * from std where roll_no=?',(roll,))
# for i in data:
# print(i)   

# ---------------------------------

''' update'''

# con.execute('update std set name="anaga" where name="agnaey"')
# con.commit()

'''user input Update'''

# name=input('enter the name:')
# up_name=input('enter the update name :')
# data=con.execute('update std set name=? where name =?',(up_name,name))
# con.commit()

'''delete'''

# con.execute('delete from std where roll_no="1"')
# con.commit()

''' user input delete'''

# roll_no=int(input('delete roll no:'))
# data=con.execute('delete from std where roll_no=?',(roll_no,))
# con.commit()

