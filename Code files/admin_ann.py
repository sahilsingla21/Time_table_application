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
import announcements_db
from kivy.clock import Clock

import time



spinner1=Spinner()
spinner2=Spinner()
spinner3=Spinner()

  


class ChangesScreen(Screen):

    def __init__(self, **kwargs):
        super(ChangesScreen, self).__init__(**kwargs)


        def func1(spinner,text):
            variables.YEAR=text

        global spinner1
        global spinner2
        global spinner3
        dropd1 = AnchorLayout(anchor_x = "left",anchor_y = "top")

        spinner1 = Spinner(
        # default value shown
        text='Select Year',
        # available values
        values=("1","2"),
        # just for positioning in our example
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5})


        spinner1.bind(text=func1)
        dropd1.add_widget(spinner1)
        self.add_widget(dropd1)
        
        def func2(spinner,text):
            variables.BRANCH=text
            # print(variables.SLOT5)

        
        dropd2 = AnchorLayout(anchor_x = "center",anchor_y = "top")

        spinner2 = Spinner(
        text='Select Branch',
        values=("CSE","ECE"),
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5},
        )

        spinner2.bind(text=func2)

        dropd2.add_widget(spinner2)

        self.add_widget(dropd2)
        # print(variables.SLOT)

        def func3(spinner,text):
            variables.GROUP=text
            # print(variables.SLOT5)

        
        dropd3 = AnchorLayout(anchor_x = "right",anchor_y = "top")

        spinner3 = Spinner(
        text='Select Group',
        values=("1","2"),
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5},
        )

        spinner3.bind(text=func3)

        dropd3.add_widget(spinner3)

        self.add_widget(dropd3)
        # print(variables.SLOT)

        variables.textinput2 = TextInput(text='Type new announcement here..',multiline=True,size_hint=(0.4,0.1),pos_hint={"x":0.45,"center_y":0.59})
        self.add_widget(variables.textinput2)


        Go = FloatLayout() 
        btn3 = Button(text ='Go', 
                     font_size=35, pos_hint={'center_x':0.5,'center_y':0.1}, size_hint=(.13,.13))
        btn3.bind(on_release=self.update_ann)
      
        Go.add_widget(btn3) 
        self.add_widget(Go)


    def update_ann(self,event):

        if variables.textinput2.text == "Type new announcement here..":
            pass
        else:
            new_ann="{}    {}".format(time.strftime('%Y-%m-%d', time.localtime()), variables.textinput2.text)
            announcements_db.UpdateRecord(variables.YEAR,variables.BRANCH,variables.GROUP, new_ann)
            announcements_db.ListAdmins()
        # print(announcements_db.ReturnLecture(variables.DAY,variables.SLOT))
        # sm.add_widget(TimeTable(name='timetable1'))
        # sm.current="timetable1"





        


sm = ScreenManager() 
sm.add_widget(ChangesScreen(name='changes'))
# sm.add_widget(enterchange.ChangeSlotScreen(name='changeslot'))
# sm.add_widget(FacultyLoginPage(name='FacultyLoginPage'))
# sm.add_widget(TimeTable(name="timetable1"))
# kv = Builder.load_file("student_admin_login.kv")



class My8App(App):

    def build(self):
        return sm

if __name__ == '__main__':
    My8App().run()
