from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

# from connected import Connected
import student_logininfo
import student_ann
import variables
import announcements_db


class Scroller(ScrollView):
    def __init__(self):
        ScrollView.__init__(self)
        layout = GridLayout(cols=1, size_hint=(1, None),pos_hint={"left_x":0.5,"center_y":0.5})
        self.add_widget(layout)
        # layout.bind(minimum_height=layout.setter('height'))
        ann_list=announcements_db.Return_Announcements(variables.student_year,variables.student_branch,variables.student_group)
        for i in ann_list:
            print(i)
            layout.add_widget(Label(text=i,center_x=True))

class TestScreen(Screen):
    pass

class Login(Screen):
    def check_student_info(self,SID):
        if SID[2]=="1":
            if SID[0:2]=="18":
                variables.student_year="2"
            elif SID[0:2]=="19":
                variables.student_year="1"
            if SID[3:5]=="03":
                variables.student_branch="CSE"
            elif SID[3:5]:
                variables.student_branch="ECE"
            if SID[5:]<="60":
                variables.student_group="1"
            elif SID[5:]<="120" and SID[5:] >"60":
                variables.student_group="2"
    def do_login(self, loginText=" ", passwordText=" "):
        if student_logininfo.check_if_exists(loginText,passwordText)==True:

            self.check_student_info(loginText)
        #     self.manager.transition = SlideTransition(direction="left")
        #     self.manager.current = 'next_page'
        

        # self.clear_widgets()
        # student_ann.Next_Page().run()
            layout = FloatLayout()
            layout.add_widget(Scroller())
            testscreen = TestScreen(name='TestScreen')
            testscreen.add_widget(layout)
            self.manager.add_widget(screen=testscreen)
            # self.manager.transition= SlideTransition(direction="left")
            self.manager.current='TestScreen'
        else:
            self.resetForm()

        # app = App.get_running_app()

        # app.username = loginText
        # app.password = passwordText

        # self.manager.transition = SlideTransition(direction="left")
        # self.manager.current = 'connected'

        # app.config.read(app.get_application_config())
        # app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        # manager.add_widget(Next_Page(name='next_page'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    LoginApp().run()
    # student_ann.Next_Page().run()