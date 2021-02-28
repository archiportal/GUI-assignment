# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:11:49 2021

@author: ARCHISMAN ROY
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:03:01 2021

@author: ARCHISMAN ROY
"""

from tkinter import *
from PIL import Image,ImageTk

sports = Tk()
sports.geometry("1000x800")

# BG IMAGE #
bgImage = PhotoImage(file=r"Rain.png")
label13=Label(sports, image = bgImage)
label13.place(relwidth=1, relheight=1)


def total():
    Bat = ent1.get()
    Football = ent2.get()
    Pads = ent3.get()
    Guard = ent4.get()
    Duce = ent5.get()
    Jers = ent6.get()

    if Bat == '':
        Bat = '0'
    if Football == '':
        Football = '0'
    if Pads == '':
        Pads = '0'
    if Guard == '':
        Guard = '0'
    if Duce == '':
        Duce = '0'
    if Jers == '':
        Jers = '0'

    t = ((int(Bat)*2000)+(int(Football)*1000)+(int(Pads)*1000) +
         (int(Guard)*500)+(int(Duce)*500)+(int(Jers)*700))
    tot = Label(sports, text=t, font="times 18")
    tot.place(x=230, y=470)

label10 = Label(sports, text="Total:", font="times 18 bold")
label10.place(x=150, y=470)

label1 = Label(sports, text="GOODLUCK - Sports equipments",
               font="times 25 bold")
label1.place(x=350, y=20, anchor="center")

label2 = Label(sports, text="ITEMS", font="times 18")
label2.place(x=580, y=70)
label = Label(sports, text="PRICE(In Rupees)", font="times 18")
label.place(x=700, y=70)

item1 = Label(sports, text="Cricket Bat", font="times 14")
item1.place(x=580, y=120)

item2 = Label(sports, text="Football Size 5", font="times 14")
item2.place(x=580, y=150)

item3 = Label(sports, text="Batting pads", font="times 14")
item3.place(x=580, y=180)

item4 = Label(sports, text="Shin guard", font="times 14")
item4.place(x=580, y=210)

item5 = Label(sports, text="Duce Ball", font="times 14")
item5.place(x=580, y=240)

item6 = Label(sports, text="Jersey", font="times 14")
item6.place(x=580, y=270)

price1 = Label(sports, text="2000", font="times 14")
price1.place(x=700, y=120)

price2 = Label(sports, text="1000", font="times 14")
price2.place(x=700, y=150)

price3 = Label(sports, text="1000", font="times 14")
price3.place(x=700, y=180)

price4 = Label(sports, text="500", font="times 14")
price4.place(x=700, y=210)

price5 = Label(sports, text="500", font="times 14")
price5.place(x=700, y=240)

price6 = Label(sports, text="700", font="times 14")
price6.place(x=700, y=270)

label3 = Label(sports, text="Enter the quanities of the items",
               font="times 20")
label3.place(x=150, y=70)

label4 = Label(sports, text="Cricket Bat", font="times 16")
label4.place(x=50, y=120)
ent1 = Entry(sports)
ent1.place(x=50, y=150)

label5 = Label(sports, text="Football Size 5", font="times 16")
label5.place(x=350, y=120)
ent2 = Entry(sports)
ent2.place(x=350, y=150)

label6 = Label(sports, text="Batting pads", font="times 16")
label6.place(x=50, y=200)
ent3 = Entry(sports)
ent3.place(x=50, y=230)

label7 = Label(sports, text="Shin guard", font="times 16")
label7.place(x=350, y=200)
ent4 = Entry(sports)
ent4.place(x=350, y=230)

label8 = Label(sports, text="Duce Ball", font="times 16")
label8.place(x=50, y=280)
ent5 = Entry(sports)
ent5.place(x=50, y=310)

label9 = Label(sports, text="Jersey", font="times 16")
label9.place(x=350, y=280)
ent6 = Entry(sports)
ent6.place(x=350, y=310)

b1 = Button(sports, text="Calculate total", width="30", command=total)
b1.place(x=180, y=380)

sports.mainloop()
