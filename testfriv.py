from tkinter import *
window=Tk()
window.title('вирус')
window.geometry('300x150')
window.minsize(100,100)
window.maxsize(500,1500)
photo=PhotoImage(file='1.png')
window.iconphoto(False,photo)
def ff():
    while True:
        print('goodbuy')
gg=Label(window,text='hello',background='green')
gg.pack(pady=10)

pp=Button(window,text='piu piu piu',background='yellow',command=ff)
pp.place(x=400,y=5)


window.mainloop()
