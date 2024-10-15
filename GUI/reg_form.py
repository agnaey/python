import sqlite3
import tkinter



win=tkinter.Tk()
win.title('batch11')
win.maxsize(500,500)
win.minsize(400,400)
win.config(bg='yellow')

def reg_form():                ## reg form after clicking register
    win1=tkinter.Tk()
    win1.title('batch11')
    win1.maxsize(500,500)
    win1.minsize(400,400)
    win1.config(bg='yellow')

    def print1(): 
        con=sqlite3.connect('python/GUI/samble.db')
        try:
            con.execute('create table user(uname text,password text)')
        except:
            print('-------table exist-------')

        con.execute('insert into user(uname,password)values(?,?)',(e1.get(),e3.get()))
        con.commit()
        win1.destroy()
        # print('register name: ',e1.get())         ## in terminal print
        # print('password: ',e3.get())
        # l2. config(text=e1.get())               ## to show in output on notepad


    # def save():                      ## save the reg
    #     l2. config(text=e1.get())

    l1=tkinter.Label(win1,text='Register form',bg='yellow',fg='red')
    l1.pack()
    l1=tkinter.Label(win1,text='username',bg='yellow',fg='red')
    l1.place(x=80,y=40)
    e1=tkinter.Entry(win1)                     ##uname box          
    e1.place(x=150,y=40)
    l3=tkinter.Label(win1,text='password',bg='yellow',fg='red')
    l3.place(x=80,y=70)
    e3=tkinter.Entry(win1)                   ##pass box          
    e3.place(x=150,y=70)
    b3=tkinter.Button(win1,text='save',bg='red',activebackground='green',fg='black',activeforeground='white',padx=20,pady=10,command=print1)     
    b3.place(x=150,y=100) 
    l2=tkinter.Label(win1)            ## to show the name
    l2.place(x=160,y=150)
    win1.mainloop()

    

# def save():
    # print('username: ',e1.get()) 
    # print('password: ',e3.get())    ##to show on terminal
    # l2. config(text=e1.get())          ## to show in output on notepad

def home():
    win2=tkinter.Tk()
    win2.title('batch11')
    win2.maxsize(500,500)
    win2.minsize(400,400)
    win2.config(bg='blue')
    l1=tkinter.Label(win2,text='HOME PAGE',bg='black',fg='white',pady=10,padx=15)
    l1.pack()
    b1=tkinter.Button(win2,text='Logout',bg='red',activebackground='red',command=win2.quit)
    b1.place(x=80,y=80)
    win2.mainloop()
    

def login():
    con=sqlite3.connect('python/GUI/samble.db')
    data=con.execute('select * from user where uname=? and password=?',(e1.get(),e3.get()))
    f=0
    for i in data:
        f=1
        home()
    if f==0:
        l4.config(text='---invalid uname or password---')


l1=tkinter.Label(win,text='hello world',bg='yellow',fg='red')
l1.pack()
l1=tkinter.Label(win,text='username',bg='yellow',fg='red')
l1.place(x=80,y=40)

e1=tkinter.Entry(win)                             ##  input form
e1.place(x=150,y=40)


l3=tkinter.Label(win,text='password',bg='yellow',fg='red')
l3.place(x=80,y=70)

e3=tkinter.Entry(win)                             ##  input form
e3.place(x=150,y=70)

b3=tkinter.Button(win,text='save',bg='red',activebackground='green',fg='black',activeforeground='white',padx=20,pady=10,command=login)  
b3.place(x=100,y=100) 

b1=tkinter.Button(win,text='register',bg='red',activebackground='green',fg='black',activeforeground='white',padx=20,pady=10,command=reg_form)     
b1.place(x=200,y=100)                                    ##      button

l2=tkinter.Label(win)                         ## to show the input after save
l2.place(x=180,y=160)

l4=tkinter.Label(win)
l4.place(x=130,y=200)

win.mainloop()