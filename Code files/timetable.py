
import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.gridlayout import GridLayout

from kivy.graphics import Color, Rectangle

import sqlite3

db = sqlite3.connect("cse(1).db")


def createTable():
    db.row_factory = sqlite3.Row
    db.execute('create table if not exists cse1(Day text, "8-9" text, "9-10" text, "10-11" text, "11-12" text, "12-1" text,"1-2" text, "2-3" text, "3-4" text, "4-5" text, "5-6" text)')

def AddRow(Day, Schedule):
    db.execute("insert into cse1 values(?,?,?,?,?,?,?,?,?,?,?)", (Day, Schedule[0], Schedule[1], Schedule[2], Schedule[3], Schedule[4], Schedule[5], Schedule[6], Schedule[7], Schedule[8], Schedule[9]))
    db.commit()


def ReturnLecture(day,slot):
    
    db.row_factory=sqlite3.Row
    lecture = db.execute("select * from cse1")
    for row in lecture:
        if row["Day"] == day:
            return row[slot]

def DeleteElement(ID):
    db.row_factory=sqlite3.Row
    db.execute("delete from cse1 where ID='{}'".format(ID))
    db.commit()

def UpdateRecord(day,slot,text):
    db.row_factory=sqlite3.Row
    db.execute("update cse1 set '{}'='{}' where Day='{}'".format(slot,text,day))
    db.commit()




class TimeTable(Screen):
    def __init__(self, **kwargs):
        super(TimeTable, self).__init__(**kwargs)


        createTable()
        days=["Mon","Tue","Wed","Thurs","Fri"]
        slots=["","8-9","9-10","10-11","11-12","12-1","1-2","2-3","3-4","4-5","5-6"]

        space = AnchorLayout(anchor_x = "left",anchor_y = "bottom",size =self.size)

        grid = GridLayout(cols=11)
        for i in range(0,11):
            label1 = Label(size_hint=(0.8,0.4),text="{}".format(slots[i]),valign="bottom",font_size=20)
            grid.add_widget(label1)
        for i in range(0,5):
            label2 = Label(size_hint=(0.1,0.05),text="{}".format(days[i]))
            grid.add_widget(label2)
            for j in range(0,10):
                label3 = Button(text="{}".format(ReturnLecture(days[i],slots[j+1])),background_color =[0.41, 0.42, 0.74, 1])
                

                grid.add_widget(label3)
        # mainbutton = Button(text='Login As', size_hint=(0.5,0.16),font_size=30,background_color=(1,1,1,1))
        space.add_widget(grid)


        self.add_widget(space)

        

class My9App(App):

    def build(self):
        return TimeTable()

if __name__ == '__main__':
	My9App().run()
