
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


class AdminPage(Screen):
    def __init__(self, **kwargs):
        super(AdminPage, self).__init__(**kwargs)

        fl = FloatLayout()
        btn1= Button(text="Make Changes?",pos_hint={'center_x':0.5,'center_y':0.8}, size_hint=(.4,.2),font_size=30)
        label = Label(text="---OR---",pos_hint={'center_x':0.5,'center_y':0.55},size=(20,20),font_size=25)
        btn2= Button(text="View Time Table",pos_hint={'center_x':0.5,'center_y':0.3}, size_hint=(.4,.2),font_size=30)
        fl.add_widget(btn1)
        fl.add_widget(label)
        fl.add_widget(btn2)
        self.add_widget(fl)

        

    def callbackTo2(self,event):
        if mainbutton.text == "'Student'":
            sm.current="StudentLoginPage"
        elif mainbutton.text == "'Faculty'":
            sm.current="FacultyLoginPage"


class My9App(App):

    def build(self):
        return AdminPage()

if __name__ == '__main__':
	My9App().run()
