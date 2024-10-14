import tkinter

win=tkinter.Tk()

win.title('batch11')
win.maxsize(500,500)
win.minsize(400,400)
win.config(bg='green')

l1=tkinter.Label(win,text='hello world',bg='green',fg='white')
l1.pack()


win.mainloop()