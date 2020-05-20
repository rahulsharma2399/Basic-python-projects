import tkinter as tk
app=tk.Tk()
app.geometry('500x400')
app.title('My Notepad')
a=tk.Menubutton(app,text='File')
a.grid(row=0,column=0)


b=tk.Menubutton(app,text='Edit')
b.grid(row=0,column=1)

c=tk.Menubutton(app,text='Format')
c.grid(row=0,column=2)

d=tk.Menubutton(app,text='View')
d.grid(row=0,column=3)

e=tk.Menubutton(app,text='help')
e.grid(row=0,column=4)

