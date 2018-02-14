from tkinter import *
from tourlist import *
"""
master = Tk()

frame = Canvas(width=1280, height=600, bg="#4e0000")
frame.pack()

frame.create_line(0, 700, 200, 100)
frame.create_line(0, 100, 450, 0, fill="red", dash=(4, 4))

frame.create_oval(50,100,100,50, fill="green", width="6")
frame.create_oval(40,50,50,40, fill="black")


b1 = Button(master, text="Städte generieren")
b1.pack()


mainloop()
"""

class Gagui():
    def __init__(self,tourlist):
        self.tourlist=tourlist
        self.master=Tk()

        self.frame = Canvas(self.master, width=1200, height= 550, background="#476042")
        self.frame.pack()
        self.tourzeichnen()

    def tourzeichnen(self):
        self.tourlist.sort()
        tour=self.tourlist.getTour(0)
        for i in range(tour.getTourSize()-1) :
            stadt1=tour.getStadt(i)
            stadt2=tour.getStadt(i+1)
            x1=stadt1.x
            y1=stadt1.y
            x2=stadt2.x
            y2=stadt2.y
            start = [stadt1.x, stadt1.y]
            los1=(x1-4,y1-4)
            rus1=(x1+4,y1+4)
            los2=(x2-4,y2-4)
            rus2=(x2+4,y2+4)
            self.frame.create_line(x1, y1, x2, y2, fill="#000000", width="5")
            self.frame.create_line(x1, y1, x2, y2, fill="#FFFFFF", width="2")
            self.frame.create_rectangle(los1[0]-3, los1[1]-3, rus1[0]+3, rus1[1]+3, fill="#000000", width="0")
            self.frame.create_rectangle(los1[0], los1[1], rus1[0], rus1[1], fill="#dd0000", width="0")

            if i==tour.getTourSize()-2:
                self.frame.create_rectangle(los2[0]-3, los2[1]-3, rus2[0]+3, rus2[1]+3, fill="#000000", width="0")
                self.frame.create_rectangle(los2[0], los2[1], rus2[0], rus2[1], fill="#dd0000", width="0")
                self.frame.create_line(x2, y2, start[0], start[1])

        mainloop()

t=Tourlist(100,20)
gui=Gagui(t)

