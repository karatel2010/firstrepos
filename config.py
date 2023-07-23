from tkinter import *
from speedtest import Speedtest
import requests
def getspeed():
    respons = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=55.605934&lon=37.66452&appid=8537d9ef6386cb97156fd47d832f479c')
    respons = respons.json()
    print(respons)
    upl_label.config(text=f" в москве сегодня {round(respons['main']['temp_max'])-273}\nощущается как {round(respons['main']['feels_like'])-273} ")

root=Tk()
root.title('speed test')
root.geometry('400x400')
butt=Button(root,text='weather',font=36,command=getspeed)
butt.pack(side=BOTTOM,pady=16)
upl_label=Label(root,text='',font=30)
upl_label.pack(pady=(30,0))



root.mainloop()