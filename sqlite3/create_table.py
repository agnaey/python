import sqlite3
  ###'''   creating table                '''


con=sqlite3.connect('python/sqlite3/create.db')
try:
    con.execute('create table std(roll_no int,name text,age int,mark real)')
except:
    print('table already exits')

### to add values in table 
con.execute('insert into std(roll_no,name,age,mark)values(1,"agnaey",21,40),(2,"akshay",20,42)')
con.commit()    ##to save                                       ##        ^^^ you can add multiple pepl using comma and add again

