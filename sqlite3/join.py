import sqlite3
con=sqlite3.connect('python/sqlite3/join.db')
try:
    con.execute('create table std (no int,name text,age int)')
    
except:
    print('table already exits')
try:
    con.execute('create table mark(no int,sub text,mark real)')
except:
    print('table already exist')


# con.execute('insert into std(no,name,age)values(1,"A",20),(2,"B",21),(3,"C",20)')
# con.commit()

# con.execute('insert into mark(no,sub,mark) values(1,"py",65),(2,"php",75),(4,"java",80),(1,"php",72)')
# con.commit()

'''innerjoin'''

# data=con.execute('select std.no,std.name,std.age,mark.sub,mark.mark from std inner join mark on std.no=mark.no')
# for i in data:
#     print(i)

'''left join'''

# data=con.execute('select std.no,std.name,std.age,mark.sub,mark.mark from std left join mark on std.no=mark.no')
# for i in data:
    # print(i)

'''cross join'''
data=con.execute('select std.no,std.name,std.age,mark.sub,mark.mark from std cross join mark')
for i in data:
    print(i)

