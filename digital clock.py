from tkinter import *
import time

tk_window=Tk()
#tk_window.geometry(("1200x1200"))
tk_window.title('DIGITAL CLOCK')

def t_curr():
    a2=time.strftime("%H:%M:%S:%p")
    a1.config(text=a2)
    a1.after(200,t_curr)

a=Label(text='time')
a.pack()
a1=Label(tk_window,font=('times new roman',155,'bold'),
         fg='red',bg='black')
a1.pack()
t_curr()
tk_window.mainloop()