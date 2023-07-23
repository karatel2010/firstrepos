from tkinter import *
import asyncio

# async def get_speed():
#     down=Speedtest().download()
#     await print(down)
def cross():
    colvocross.config(text=int(colvocross['text'])+1)
    price.config(text=int(price['text']) + 7777)
    col_vo.config(text=int(col_vo['text']) + 1)

def tsh():
    colvotshirt.config(text=int(colvotshirt['text'])+1)
    price.config(text=int(price['text']) + 1200)
    col_vo.config(text=int(col_vo['text']) + 1)

def cp():
    colvocap.config(text=int(colvocap['text'])+1)
    price.config(text=int(price['text']) + 700)
    col_vo.config(text=int(col_vo['text']) + 1)


def cross_():
    if int(colvocross['text'])>0:
        price.config(text=int(price['text']) - 7777)
        col_vo.config(text=int(col_vo['text']) - 1)
    if int(col_vo['text']) <=0:
        col_vo.config(text='0')
    if int(price['text'])<=0:
        price.config(text='0')
    if int(colvocross['text']) > 0:
        colvocross.config(text=int(colvocross['text'])-1)
def tsh_():
    if int(colvotshirt['text'])>0:
        price.config(text=int(price['text']) - 1200)
        col_vo.config(text=int(col_vo['text']) - 1)
    if int(col_vo['text']) <= 0:
        col_vo.config(text='0')
    if int(price['text']) <= 0:
        price.config(text='0')
    if int(colvotshirt['text']) > 0:
        colvotshirt.config(text=int(colvotshirt['text'])-1)

def cp_():
    if int(colvocap['text'])>0:
        price.config(text=int(price['text']) - 700)
        col_vo.config(text=int(col_vo['text']) - 1)
    if int(price['text']) <= 0 :
        price.config(text='0')
    if int(col_vo['text']) <= 0:
        col_vo.config(text='0')
    if int(colvocap['text'])>0:
        colvocap.config(text=int(colvocap['text']) - 1)

root=Tk()
root.configure(background='black')
root.title('speed test')
root.geometry('800x200')

frameforbuttun=Frame(background='black')
framefortovar=Frame(background='black')
frameforpc=Frame(background='black')
framee=Frame(background='black')
framefor_=Frame(background='black')
frameforev=Frame(background='black')
crossovki=Button(master=frameforbuttun,text='+',font=20,command=cross)
crossovki.pack()
t_shirt=Button(master=frameforbuttun,text='+',font=20,command=tsh)
t_shirt.pack(pady=10)
cap=Button(master=frameforbuttun,text='+',font=20,command=cp)
cap.pack()


crossovki_=Button(master=framefor_,text='-',font=20,command=cross_)
crossovki_.pack()
t_shirt_=Button(master=framefor_,text='-',font=20,command=tsh_)
t_shirt_.pack(pady=10)
cap_=Button(master=framefor_,text='-',font=20,command=cp_)
cap_.pack()


cross_l=Label(master=framefortovar,text=' крутые кроссовки купи не пожалеешь цена : 7777р',font=20)
cross_l.pack()
tsh_l=Label(master=framefortovar,text='классная футболка купи не пожалеешь цена : 1200р',font=20)
tsh_l.pack(pady=20)
cap_l=Label(master=framefortovar,text='              купи кепку не пожалеешь цена : 700р            ',font=20)
cap_l.pack()


price=Label(master=frameforpc,text='0',font=10)
price.pack()
col_vo=Label(master=frameforpc,text='0',font=10)
col_vo.pack(pady=10)

pric=Label(master=framee,text='к оплате :',font=10)
pric.pack()
col_v=Label(master=framee,text='кол-во товаров :',font=10)
col_v.pack(pady=10)


colvocross=Label(master=frameforev,text='0',font=30)
colvocross.pack(pady=5)
colvotshirt=Label(master=frameforev,text='0',font=30)
colvotshirt.pack(pady=10)
colvocap=Label(master=frameforev,text='0',font=30)
colvocap.pack(pady=10)


frameforbuttun.place(x=400,y=50)
framefortovar.place(x=10,y=50)
framee.place(x=489,y=50)
frameforpc.place(x=650,y=50)
framefor_.place(x=425,y=50)
frameforev.place(x=450,y=55)
# upl_l=Entry(root,font=30)
# upl_l.place(x=30,y=200)


root.mainloop()
