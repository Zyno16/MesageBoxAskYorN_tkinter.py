from tkinter import *
from tkinter import ttk
from tools import *

form =Tk()
form.geometry("700x500")
tkcenter(form)

def msg():
    msgbox("this is my message")
Button(form,text="show",command= msg).pack()

def msg2():
    if msgask("do you want to continue ?")==True:
        msgbox("yes")
    else:
        msgbox("no")

Button(form,text="show meassage",command =msg2).pack()       
        
    
    

bg = "navy"
bgall(form,bg)
fg ="lightblue"
fgall(form,fg)
font ="None 30 bold"
fontall(form,font)

form.mainloop()
