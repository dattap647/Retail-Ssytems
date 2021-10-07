from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
def signin():
    if userentry.get()=='' or passentry.get()=='':
        showerror('Error','Fields Cannot Be Empty')
    elif userentry.get()=='Datta'and passentry.get()=='1805':
        root.destroy()
        import retail
    else:
        showerror('Error','Invalid Username Or Password')

def func():
    if check.get()==1:
        userentry.insert(END,'Datta')
        passentry.insert(END,'1805')
    else:
        userentry.delete(0,END)
        passentry.delete(0,END)

root = Tk()
root.geometry('770x650+50+0')
root.title('Login Page')
root.config(bg='sienna3')

label=Label(root,text='Customer Login',font=('castellar',28,'bold'),bg='sienna3',fg='white')
label.place(x=180,y=40)
frame = Frame(root, bg='white', width=580, height=430)
frame.place(x=100, y=110)

userimage = PhotoImage(file='log.png')
userimageLabel = Label(frame, image=userimage, bg='white')
userimageLabel.place(x=230, y=5)
userLabel = Label(frame, text='Username', font=('arial', 22, 'bold'), bg='white', fg='black')
userLabel.place(x=120, y=150)
userentry = Entry(frame, font=('arial', 22,), bg='white', fg='black')
userentry.place(x=120, y=200)

passLabel = Label(frame, text='Password', font=('arial', 22, 'bold'), bg='white', fg='black')
passLabel.place(x=120, y=250)
passentry = Entry(frame, font=('arial', 22,), bg='white', fg='black',show='*')
passentry.place(x=120, y=300)




loginbutton2 = Button(frame, text='Login', font=('arial', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=signin)
loginbutton2.place(x=350, y=360)
check = IntVar()
rememberCheckButton=Checkbutton(frame,text='Remember Me',bg='white', command=func,variable=check,font=('arial', 16, 'bold'),fg='sienna3',onvalue=1,offvalue=0)
rememberCheckButton.place(x=120,y=350)



root.mainloop()