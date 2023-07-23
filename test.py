from tkinter import *
root=Tk()
def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
# root.configure(b)
root.title('')
root.geometry('800x800')
root.minsize(500,500)
root.maxsize(1000,1000)
photo=PhotoImage(file='1.png')
root.iconphoto(False,photo)
lkd=Label(root,pady=20,padx=50,text='df\nvvjv',bg='red',fg='white',font=('Arial',78,'bold'),width=6,height=5,anchor='ne',relief=RAISED,bd=10,justify=RIGHT)
lkd.pack()

root.mainloop()