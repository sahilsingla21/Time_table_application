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
import student_logininfo
import admin_logininfo
import enterchange
import timetable
import cse_1

import sqlite3
from kivy.factory import Factory as F

class ChangePassword(Screen):
    
    def __init__(self, **kwargs):
        super(ChangePassword, self).__init__(**kwargs)
        float1= FloatLayout()
        self.label1 = Label(text="Current Password:",size_hint=(0.2,0.2),pos_hint={"center_x":0.3,"center_y":0.8},font_size=30)
        float1.add_widget(self.label1)
       


        variables.textinput4 = TextInput(text='',multiline=True,size_hint=(0.4,0.1),pos_hint={"x":0.48,"center_y":0.8})
        float1.add_widget(variables.textinput4)       
        
        label2= Label(text="Enter New Password:",size_hint=(0.2,0.2),pos_hint={"center_x":0.27,"center_y":0.65},font_size=30)
        float1.add_widget(label2)

        
        variables.textinput1 = TextInput(text='',multiline=True,size_hint=(0.4,0.1),pos_hint={"x":0.48,"center_y":0.65})
        float1.add_widget(variables.textinput1)

        label3= Label(text="Confirm New Password:",size_hint=(0.2,0.2),pos_hint={"center_x":0.25,"center_y":0.47},font_size=30)
        float1.add_widget(label3)

        
        variables.textinput3 = TextInput(text='',multiline=True,size_hint=(0.4,0.1),pos_hint={"x":0.48,"center_y":0.47})
        float1.add_widget(variables.textinput3)


        btn1= Button(text="Save Change",pos_hint={"center_x":0.3,"center_y":0.2},size_hint=(0.29,0.2),font_size=30)
        btn1.bind(on_release=self.savechangesbtn)

        btn2= Button(text="Cancel",pos_hint={"center_x":0.7,"center_y":0.2},size_hint=(0.29,0.2),font_size=30)
        float1.add_widget(btn1)
        float1.add_widget(btn2)

        self.add_widget(float1)

    def savechangesbtn(self,event):
        if variables.textinput3.text==variables.textinput1.text:
            if variables.user=="admin":
                if admin_logininfo.checkPassword()==True:
                    admin_logininfo.changePassword()
                    self.resetForm()
                else:
                    self.resetForm()

            elif variables.user=="student":
                if student_logininfo.checkPassword()==True:
                    student_logininfo.changePassword()
                    print("done")
                    self.resetForm()
                else:
                    self.resetForm()
        else:
            self.resetForm()

    def resetForm(self):
        # print("reset")
        variables.textinput1.text=""
        variables.textinput3.text=""
        variables.textinput4.text=""
        
    def cancelbtn(self,event):
        pass
        # sm.add_widget(TimeTable(name='timetable1'))
        # sm.current="timetable1"


    
sm = ScreenManager() 
sm.add_widget(ChangePassword(name='changepassword'))



class ChangePassword(App):

    def build(self):
        return sm

if __name__ == '__main__':
    ChangePassword().run()
