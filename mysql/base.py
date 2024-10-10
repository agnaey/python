import mysql.connector
con = mysql.connector.connect(host='localhost',user='agnaey',password='agnaey',database='agnaeydatas')
con.autocommit=True               ## to commit without typing it again & again
cur = con.cursor()
# cun.execute('create database agnaeydatas')         ## to create table in mysql
try:
    cur.execute("create table std (roll_no int,name text,age int)")
except:
    print('table already exits')
cur.execute('insert into std (roll_no,name,age) values(1,"akshay",21),(2,"tutu",20)')       ##to insert values


'   to print the inserted data'
# cur.execute ("select * from std")
# data = cur.fetchall()
# for i in data:
#     print(i)


