import tkinter.messagebox
import time
from tkinter import *
root=Tk()
root.configure(background='black')
root.title('')
root.geometry('450x250')
root.minsize(200,250)
root.maxsize(450,450)
photo=PhotoImage(file='1.png')
frame4=Frame(background='black')
frame6=Frame(background='black')
name=Label(master=frame4,text='введите имя:',font=20)
name.pack()
family=Label(master=frame4,text='введите фамилию:',font=20)
family.pack(pady=10,ipadx=10)
pasword=Label(master=frame4,text='введите пароль:',font=20)
pasword.pack()


nameen=Entry(master=frame6,font=20)
nameen.pack()
familyen=Entry(master=frame6,font=20)
familyen.pack(pady=10)
pasworden=Entry(master=frame6,font=20)
pasworden.pack()
frame6.place(x=200,y=20)
frame4.place(x=20.,y=20)
m=[]
class User():
    def __init__(self,name,surname,password):
        self.name=name
        self.surname=surname
        self.password=password
    def fname(self):
        return(f'{self.name} {self.surname}')


lbox=Listbox(root,width=25,height=3,font=1)
lbox.place(x=25,y=160)

def filllist(mas):
    lbox.delete(0,'end')
    i=0
    for u in mas:
        lbox.insert(i,u.fname())
        i+=1

def ready0():
    if nameen.get()=='' or familyen.get()=='' or  pasworden.get()=='':
        tkinter.messagebox.showwarning('Внимание','заполните все поля!')
        return
    use = User(name=nameen.get(),surname=familyen.get(), password=pasworden.get())
    m.append(use)
    filllist(m)
    familyen.delete(0,999999)
    nameen.delete(0,999999)
    pasworden.delete(0,999999)


def passwor():
    nu = lbox.curselection()
    n=list(nu)[0]
    print(f'{m[n].password}')


btn=Button(root,text='вывести пароль',font=20,command=passwor)
btn.place(x=200,y=200)
ready=Button(root,text='готово',font=20,command=ready0)
ready.place(x=200,y=125)

root.mainloop()