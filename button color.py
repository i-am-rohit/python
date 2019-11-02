# from tkinter  import *
# root =Tk()
# root.title("login")
# root.geometry("655x333")
# btnlogin = Button(master=root,text="login")
# btnlogin.grid(row=0,column=0)
# btnlogin1 = Button(master=root,text="login")
# btnlogin1.grid(row=0,column=1)
# root.mainloop()

from tkinter import *
root=Tk()
root.title("login")
root.geometry("655x333")

def btnlogin_click(event):
    btnlogin["bg"]="red"

def btnlogin_motion(e):
    varemailid.set("X: "+str(e.x))
    varpassword.set("y: "+str(e.y))
    btnlogin.place(x=e.x,y=e.y)

# def btnlogin_enter(event):
#     btnlogin["bg"] = "red"

# def btnlogin_leave(event):
#     btnlogin["bg"] = "blue"

lblEmailid=Label(master=root,text="Email id")
lblEmailid.grid(row=0,column=0)
varemailid = StringVar()

lblpassword=Label(master=root,text="Paassword")
lblpassword.grid(row=1,column=0)
varpassword = StringVar()

txtemail=Entry(master=root,textvariable=varemailid)
txtemail.grid(row=0,column=1)

txtpassword=Entry(master=root,textvariable=varpassword)
txtpassword.grid(row=1,column=1)

btnlogin=Button(master=root,text="Login")
btnlogin.grid(row=3,column=2)
btnlogin.bind("<Button-1>",btnlogin_click)

# btnlogin.bind("<Enter>",btnlogin_enter)
# btnlogin.bind("<Leave>",btnlogin_leave)
btnlogin.bind("<Motion>",btnlogin_motion)

root.mainloop()