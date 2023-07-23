from tkinter import *

def button_pressed(evt):
  current_entry = str(evt.widget)
  button_number = current_entry.replace('.!button','')
  if button_number=='15':
    a=str(eval(lab['text']))
    lab.config(text=a)
    return
  elif button_number == "":
    a = "1"
  elif button_number == "10":
    a = "0"
  elif button_number == "11":
    a = "+"
  elif button_number == "12":
    a = "-"
  elif button_number =='13':
    a='/'
  elif button_number =='14':
    a='*'
  elif button_number =='16':
    lab.config(text='')
  else:
    a = button_number
  lab.config(text=lab['text'] + a)

root=Tk()
root.title('speed test')
root.geometry('300x300')

lab=Label(root, text="", font=20)
lab.place(x=100, y=20)

button = []
for i in range(0,9):
  button.append(Button(root,text=str(i+1),font=20))
  button[i].bind('<ButtonPress>', button_pressed)
  button[i].place(x=50*((i)%3)+50, y=int((i)/3)*50+50)

button.append(Button(root,text="0",font=20))
button[i+1].bind('<ButtonPress>', button_pressed)
button[i+1].place(x=100, y=200)

button.append(Button(root,text="+",font=20))
button[i+2].bind('<ButtonPress>', button_pressed)
button[i+2].place(x=200, y=50)

button.append(Button(root,text="-",font=20))
button[i+3].bind('<ButtonPress>', button_pressed)
button[i+3].place(x=200, y=100)

button.append(Button(root,text="/",font=20))
button[i+4].bind('<ButtonPress>', button_pressed)
button[i+4].place(x=200, y=150)

button.append(Button(root,text="*",font=20))
button[i+5].bind('<ButtonPress>', button_pressed)
button[i+5].place(x=200, y=200)
lab.config(text="")

button.append(Button(root,text="=",font=20))
button[i+6].bind('<ButtonPress>', button_pressed)
button[i+6].place(x=200, y=250)

button.append(Button(root,text="стереть",font=20))
button[i+7].bind('<ButtonPress>', button_pressed)
button[i+7].place(x=30, y=250)

root.mainloop()

