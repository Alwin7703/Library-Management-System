from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
#import Library3
from subprocess import call

root1=Tk()
root1.title('Login')
root1.geometry('925x500+300+200')
root1.configure(bg="#fff")
root1.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
    if username=='admin' and password=='1234':
        call(["python", "e:\MINI PROJECT\Library1.py"])

    elif username=='alwin' and password=='1001':
        call(["python", "e:\MINI PROJECT\Library1.py"])

    elif username=='naman' and password=='1002':
        call(["python", "e:\MINI PROJECT\Library1.py"])
    
    elif username=='rishi' and password=='1003':
        call(["python", "e:\MINI PROJECT\Library1.py"])

    elif username=='saloni' and password=='1004':
        call(["python", "e:\MINI PROJECT\Library1.py"]) 

    else:
        messagebox.showerror("Invalid","invalid username and password")
        



img=PhotoImage(file = r"E:\MINI PROJECT\login1.png")
Label(root1,image=img,bg='white').place(x=50,y=50)
Label(root1,text="Welcome to Library Management System",fg='black',bg='white',font=('Times New Roman',24,'bold')).place(x=150,y=10)

frame=Frame(root1,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',20,'bold'))
heading.place(x=100,y=5)

###########------------------------------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

############------------------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
 
##############################################################

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
#label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
#label.place(x=75,y=270)

#sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
#sign_up.place(x=215,y=270)

root1.mainloop()