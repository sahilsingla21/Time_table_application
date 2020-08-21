
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

mainbutton=""

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        choose = FloatLayout() 
        label = Label(text ='Choose Your Login Mode', 
                     font_size=45, pos_hint={'center_x':0.5,'center_y':0.85} ) 
      
        choose.add_widget(label) 


        dropd = AnchorLayout(anchor_x = "center",anchor_y = "center",size = self.size, pos=(0,80))

        self.dropdown = DropDown()
        
        notes = ['Student','Faculty']
        for note in notes:
            btn = Button(text='%r' % note, size_hint_y=None, height=60,font_size=18)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        global mainbutton 
        mainbutton = Button(text='Login As', size_hint=(0.5,0.16),font_size=30,background_color=(1,1,1,1))
        mainbutton.bind(on_release=self.dropdown.open)

        self.dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        dropd.add_widget(mainbutton)

        Go = FloatLayout() 
        btn = Button(text ='Go', 
                     font_size=35, pos_hint={'center_x':0.5,'center_y':0.2}, size_hint=(.13,.13))
        btn.bind(on_release=self.callbackTo2)
      
        Go.add_widget(btn) 


        self.add_widget(dropd)

        self.add_widget(choose)

        self.add_widget(Go)

    def callbackTo2(self,event):
    #     sm.current="StudentLoginPage"
        if mainbutton.text == "'Student'":
            variables.user="Student"
            sm.current="StudentLoginPage"
        elif mainbutton.text == "'Faculty'":
            variables.user="admin"
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

sm = ScreenManager() 
sm.add_widget(HomeScreen(name='screen'))
sm.add_widget(StudentLoginPage(name='StudentLoginPage'))
sm.add_widget(FacultyLoginPage(name='FacultyLoginPage'))

# kv = Builder.load_file("student_admin_login.kv")



class My8App(App):

    def build(self):
        return sm

if __name__ == '__main__':
    My8App().run()

# import kivy
# kivy.require('1.7.2')
# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.properties import ObjectProperty
# from kivy.uix.button import Button
# from kivy.uix.dropdown import DropDown
# from kivy.lang import Builder
# from kivy.uix.label import Label


# class CustomDropDown(DropDown):
#     pass

# class HomeScreen(Screen):
#     top_layout = ObjectProperty(None)
    
#     def __init__(self, *args, **kwargs):
#         super(HomeScreen, self).__init__(*args, **kwargs)
#         self.drop_down = CustomDropDown()


#         dropdown = DropDown()
#         notes = ['Student','Faculty']
#         for note in notes:
#             btn = Button(text='%r' % note, size_hint_y=None, height=60,font_size=18)
#             btn.bind(on_release=lambda btn: dropdown.select(btn.text))
#             dropdown.add_widget(btn)

#         mainbutton = Button(text='Choose your login mode', size_hint=(1.2,1),font_size=30,background_color=(1,1,1,1))

#         mainbutton.bind(on_release=dropdown.open)
#         dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

#         self.top_layout.add_widget(mainbutton)
#     def callbackTo2(instance):
#         sm.current="LoginPage"


# class LoginPage(Screen):
#     def __init__(self, *args):
#         super(LoginPage, self).__init__(name='LoginPage')
#         self.add_widget(Label(text="Login Page"))



# sm = ScreenManager()


# class dropdApp(App):
#     def build(self):
#         sm.add_widget(HomeScreen())
#         sm.add_widget(LoginPage())
#         return sm
    
# kv = Builder.load_file("student_admin_login.kv")



# if __name__ == '__main__':
#     dropdApp().run()