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
        print('register name:',e1.get())         ## in terminal print
        l2. config(text=e1.get())               ## to show in output on notepad


    # def save():                      ## save the reg
    #     l2. config(text=e1.get())

    l1=tkinter.Label(win1,text='Register form',bg='yellow',fg='red')
    l1.pack()
    l1=tkinter.Label(win1,text='username',bg='yellow',fg='red')
    l1.place(x=80,y=40)
    e1=tkinter.Entry(win1)                     ##input box          
    e1.place(x=150,y=40)
    l3=tkinter.Label(win1,text='password',bg='yellow',fg='red')
    l3.place(x=80,y=70)
    e3=tkinter.Entry(win1)                   ##input box          
    e3.place(x=150,y=70)
    b3=tkinter.Button(win1,text='save',bg='red',activebackground='green',fg='black',activeforeground='white',padx=20,pady=10,command=print1)     
    b3.place(x=150,y=100) 
    l2=tkinter.Label(win1)            ## to show the name
    l2.place(x=160,y=150)
    win1.mainloop()

    

def save():
    print('username: ',e1.get())     ##to show on terminal
    l2. config(text=e1.get())          ## to show in output on notepad

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

b3=tkinter.Button(win,text='save',bg='red',activebackground='green',fg='black',activeforeground='white',padx=20,pady=10,command=save)  
b3.place(x=100,y=100) 

b1=tkinter.Button(win,text='register',bg='red',activebackground='green',fg='black',activeforeground='white',padx=20,pady=10,command=reg_form)     
b1.place(x=200,y=100)                                    ##      button

l2=tkinter.Label(win)                         ## to show the input after save
l2.place(x=180,y=160)

win.mainloop()