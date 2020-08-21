
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
import variables
import cse_1
import makechanges
import timetable

slotbutton=""
daybutton=""




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
        btn1.bind(on_release=makechanges.savechangesbtn)

        btn2= Button(text="Cancel",pos_hint={"center_x":0.7,"center_y":0.2},size_hint=(0.29,0.2),font_size=30)
        float1.add_widget(btn1)
        float1.add_widget(btn2)

        self.add_widget(float1)

    


    def callbackTo2(self,event):
    #     sm.current="StudentLoginPage"
        if mainbutton.text == "'Student'":
            sm.current="StudentLoginPage"
        elif mainbutton.text == "'Faculty'":
            sm.current="FacultyLoginPage"

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

# sm = ScreenManager() 
# sm.add_widget(ChangeSlotScreen(name='changes'))
# sm.add_widget(StudentLoginPage(name='StudentLoginPage'))
# sm.add_widget(FacultyLoginPage(name='FacultyLoginPage'))

# # kv = Builder.load_file("student_admin_login.kv")



# class My8App(App):

#     def build(self):
#         return sm

if __name__ == '__main__':
    My8App().run()
