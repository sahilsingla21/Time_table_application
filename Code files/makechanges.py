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
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
import variables
import enterchange
import timetable
import cse_1

import sqlite3
from kivy.factory import Factory as F
# import plyer


spinner1=Spinner()
spinner2=Spinner()
    
# SLOT5="SLOT"
# DAY="DAY"

days=["Mon","Tue","Wed","Thurs","Fri"]
slots=["","8-9","9-10","10-11","11-12","12-1","1-2","2-3","3-4","4-5","5-6"]

  


class ChangesScreen(Screen):

    def __init__(self, **kwargs):
        super(ChangesScreen, self).__init__(**kwargs)


        # actionbar = F.ActionBar(pos_hint={'top': 1})

        # av = F.ActionView()
        # av.add_widget(F.ActionPrevious(title='Action Bar', with_previous=False))
        # av.add_widget(F.ActionOverflow())
        # av.add_widget(F.ActionButton(text='Btn0',icon='atlas://data/images/defaulttheme/audio-volume-high'))

        # for i in range(1, 5):
        #     av.add_widget(F.ActionButton(text='Btn{}'.format(i)))

        # ag = F.ActionGroup(text='Group1')
        # for i in range(5, 8):
        #     ag.add_widget(F.ActionButton(text='Btn{}'.format(i)))

        # av.add_widget(ag)

        # actionbar.add_widget(av)

        # # can't be set in F.ActionView() -- seems like a bug
        # av.use_separator = True
        # self.add_widget(actionbar)
        # # runTouchApp(actionbar)    

        def func1(spinner,text):
            variables.DAY=text

        global spinner1
        global spinner2
        dropd1 = AnchorLayout(anchor_x = "left",anchor_y = "top")

        spinner1 = Spinner(
        # default value shown
        text='Select Day',
        # available values
        values=("Mon","Tue","Wed","Thurs","Fri"),
        # just for positioning in our example
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5})


        spinner1.bind(text=func1)
        dropd1.add_widget(spinner1)
        self.add_widget(dropd1)
        
        def func2(spinner,text):
            variables.SLOT=text
            # print(variables.SLOT5)

        
        dropd2 = AnchorLayout(anchor_x = "right",anchor_y = "top")

        spinner2 = Spinner(
        text='Select Slot',
        values=("8-9","9-10","10-11","11-12","12-1","1-2","2-3","3-4","4-5","5-6"),
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5},
        )

        spinner2.bind(text=func2)

        dropd2.add_widget(spinner2)

        self.add_widget(dropd2)
        # print(variables.SLOT)

        Go = FloatLayout() 
        btn3 = Button(text ='Go', 
                     font_size=35, pos_hint={'center_x':0.5,'center_y':0.1}, size_hint=(.13,.13))
        btn3.bind(on_release=self.changeslot)
      
        Go.add_widget(btn3) 
        self.add_widget(Go)


    def changeslot(self,event):
        sm.add_widget(ChangeSlotScreen(name='changeslot'))
        sm.current="changeslot"
        # plyer.notification.notify(title='test', message="Notification using plyer")

class ChangeSlotScreen(Screen):
    
    def __init__(self, **kwargs):
        super(ChangeSlotScreen, self).__init__(**kwargs)
        print(variables.SLOT)
        print(variables.DAY)
        float1= FloatLayout()
        self.label1 = Label(text="Current Value:",size_hint=(0.2,0.2),pos_hint={"center_x":0.3,"center_y":0.8},font_size=30)
        float1.add_widget(self.label1)
       

        self.label3=Label(text="{}".format(cse_1.ReturnLecture(variables.DAY,variables.SLOT)),size_hint=(0.2,0.2),pos_hint={"x":0.45,"center_y":0.8},font_size=35)
        float1.add_widget(self.label3)
       
        
        label2= Label(text="Enter New Value:",size_hint=(0.2,0.2),pos_hint={"center_x":0.27,"center_y":0.6},font_size=30)
        float1.add_widget(label2)

        
        variables.textinput = TextInput(text='Type text here...',multiline=True,size_hint=(0.4,0.1),pos_hint={"x":0.45,"center_y":0.59})
        float1.add_widget(variables.textinput)

        btn1= Button(text="Save Change",pos_hint={"center_x":0.3,"center_y":0.2},size_hint=(0.29,0.2),font_size=30)
        btn1.bind(on_release=self.savechangesbtn)

        btn2= Button(text="Cancel",pos_hint={"center_x":0.7,"center_y":0.2},size_hint=(0.29,0.2),font_size=30)
        float1.add_widget(btn1)
        float1.add_widget(btn2)

        self.add_widget(float1)

    

    def savechangesbtn(self,event):
        cse_1.UpdateRecord(variables.DAY,variables.SLOT,variables.textinput.text)
        print(cse_1.ReturnLecture(variables.DAY,variables.SLOT))
        sm.add_widget(TimeTable(name='timetable1'))
        sm.current="timetable1"
    
    def cancelbtn(self,event):
        sm.add_widget(TimeTable(name='timetable1'))
        sm.current="timetable1"

class StudentLoginPage(Screen):
    def __init__(self, **kwargs):
        super(StudentLoginPage, self).__init__(**kwargs)
    #     super(LoginPage, self).__init__(name='LoginPage')
        self.add_widget(Label(text="Student Login Page"))



class FacultyLoginPage(Screen):
    def __init__(self, **kwargs):
        super(FacultyLoginPage, self).__init__(**kwargs)
    #     super(LoginPage, self).__init__(name='LoginPage')
        self.add_widget(Label(text="Faculty Login Page"))

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
                # globals()['label%s' % j] = Button(id="{},{}".format(i,j+1),text="{}".format(ReturnLecture(days[i],slots[j+1])),background_color =[0.41, 0.42, 0.74, 1])
                variables.label3 = Button(id="{},{}".format(i,j+1),text="{}".format(ReturnLecture(days[i],slots[j+1])),background_color =[0.41, 0.42, 0.74, 1])
                # variables.label3.bind(on_release=self.label3press)
                # globals()['label%s' % j].bind(on_release=self.label3press)
                

                grid.add_widget(variables.label3)
                # grid.add_widget(globals()['label%s'%j])
        # mainbutton = Button(text='Login As', size_hint=(0.5,0.16),font_size=30,background_color=(1,1,1,1))
        space.add_widget(grid)


        self.add_widget(space)

    # def label3press(self,event):
    #     temp = variables.label3.id
    #     if temp[-2]==",":
    #         variables.DAY=days[temp[0]]
    #         variables.SLOT=slots[temp[-1]]
    #     else:
    #         variables.DAY=days[int(temp[0])]
    #         variables.SLOT=slots[int(temp[2:])]
    #     sm.add_widget(ChangeSlotScreen(name="changeslot"))
    #     sm.current="changeslot"


        


sm = ScreenManager() 
sm.add_widget(ChangesScreen(name='changes'))
# sm.add_widget(enterchange.ChangeSlotScreen(name='changeslot'))
sm.add_widget(FacultyLoginPage(name='FacultyLoginPage'))
sm.add_widget(TimeTable(name="timetable1"))
# kv = Builder.load_file("student_admin_login.kv")



class My8App(App):

    def build(self):
        return sm

if __name__ == '__main__':
    My8App().run()
