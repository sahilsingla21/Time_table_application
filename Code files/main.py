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
# import enterchange
# import timetable
import cse_1
import sqlite3
from kivy.factory import Factory as F
# import change_password
# import loginpage

import announcements_db
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView

import time
import student_logininfo

import admin_logininfo


mainbutton=""


'''
Home Page
Announcements
Time Table
Change Password
Sign Out
'''


class Action_Bar(Screen):

    def __init__(self, **kwargs):
        super(Action_Bar, self).__init__(**kwargs)


        # sm.add_widget(HomeScreen(name='screen'))
        actionbar = F.ActionBar(pos_hint={'top': 1})

        av = F.ActionView()
        av.add_widget(F.ActionPrevious(title='Action Bar', with_previous=False))
        av.add_widget(F.ActionOverflow())
        # av.add_widget(F.ActionButton(text='Btn0',icon='atlas://data/images/defaulttheme/audio-volume-high'))

        # av.add_widget(F.ActionButton(text='HomePage'))
        av.add_widget(F.ActionButton(text='Announcements',on_release=self.announcements))
        av.add_widget(F.ActionButton(text='Time Table',on_release=self.timetable))
        # av.add_widget(F.ActionButton(text='Settings',on_release=self.on_press))
    

        # for i in range(1, 5):
        #     av.add_widget(F.ActionButton(text='Btn{}'.format(i)))

        ag = F.ActionGroup(text='Settings')
        # for i in range(5, 12):
        ag.add_widget(F.ActionButton(text='Change Password',on_release=self.change_password))
        ag.add_widget(F.ActionButton(text='Sign Out',on_release=self.sign_out))

        av.add_widget(ag)

        actionbar.add_widget(av)

        # can't be set in F.ActionView() -- seems like a bug
        av.use_separator = True
        self.add_widget(actionbar)
        # runTouchApp(actionbar)    

    def change_password(self,event):
        sm.add_widget(ChangePassword(name='changepassword'))
        sm.current="changepassword"
        # print("l")
    def sign_out(self,event):
        # ActionBar().run()
        variables.mainbutton.text="Login As"
        # sm.add_widget(HomeScreen(name='screen'))
        sm.add_widget(StudentLoginPage(name='StudentLoginPage'))
        sm.add_widget(FacultyLoginPage(name='FacultyLoginPage'))
        sm.current="screen"

    def announcements(self,event):
        # print("1")
        # print(variables.user+"h")
        if variables.user=="admin":
            # sm.add_widget(Admin_Ann(name='admin_ann'))
            sm.current="admin_ann"
        elif variables.user=="student":
            # print("2")
            sm.add_widget(TestScreen(name="TestScreen"))
            sm.current="TestScreen"
            # print("2")
            # layout = FloatLayout()
            # layout.add_widget(Scroller())
            # testscreen = TestScreen(name='TestScreen')
            # testscreen.add_widget(layout)
            # sm.add_widget(screen=testscreen)
            # # self.manager.transition= SlideTransition(direction="left")
            # sm.current='TestScreen'


    def timetable(self,event):
        if variables.user=="admin":
            sm.add_widget(AdminPage(name='admin_page'))
            sm.current="admin_page"
        elif variables.user=="student":
            # print(variables.ID)
            SID=variables.ID
            if SID[2]=="1":
                if SID[0:2]=="18":
                    variables.student_year="2"
                elif SID[0:2]=="19":
                    variables.student_year="1"
                if SID[3:5]=="03":
                    variables.student_branch="cse"
                elif SID[3:5]:
                    variables.student_branch="ece"
                if SID[5:]<="60":
                    variables.student_group="1"
                elif SID[5:]<="120" and SID[5:] >"60":
                    variables.student_group="2"
            variables.classname="{}{}_{}".format(variables.student_branch,variables.student_year,variables.student_group)
            # global db
            variables.db = sqlite3.connect("{}.db".format(variables.classname))

            sm.add_widget(TimeTable(name="Time table"))
            sm.current="Time table"
            # layout = FloatLayout()
            # layout.add_widget(Scroller())
            # testscreen = TestScreen(name='TestScreen')
            # testscreen.add_widget(layout)
            # self.manager.add_widget(screen=testscreen)
            # # self.manager.transition= SlideTransition(direction="left")
            # self.manager.current='TestScreen'

class AdminPage(Screen):
    def __init__(self, **kwargs):
        super(AdminPage, self).__init__(**kwargs)

        fl = FloatLayout()
        btn1= Button(text="Make Changes?",pos_hint={'center_x':0.5,'center_y':0.8}, size_hint=(.4,.2),font_size=30,on_release=self.make_changes_btn)
        label = Label(text="---OR---",pos_hint={'center_x':0.5,'center_y':0.55},size=(20,20),font_size=25)
        btn2= Button(text="View Time Table",pos_hint={'center_x':0.5,'center_y':0.3}, size_hint=(.4,.2),font_size=30,on_release=self.view_timetable_btn)
        fl.add_widget(btn1)
        fl.add_widget(label)
        fl.add_widget(btn2)
        self.add_widget(fl)

        

    def make_changes_btn(self,event):
        sm.add_widget(Ask_class(name='Ask_class'))
        sm.current="Ask_class"

    def view_timetable_btn(self,event):
        sm.add_widget(Ask_class2(name='Ask_class2'))
        sm.current="Ask_class2"

class Ask_class(Screen):

    def __init__(self, **kwargs):
        super(Ask_class, self).__init__(**kwargs)


        def func1(spinner,text):
            variables.YEAR=text

        global spin1
        global spin2
        global spin3
        dropd1 = AnchorLayout(anchor_x = "left",anchor_y = "top")

        spin1 = Spinner(
        # default value shown
        text='Select Year',
        # available values
        values=("1","2"),
        # just for positioning in our example
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5})


        spin1.bind(text=func1)
        dropd1.add_widget(spin1)
        self.add_widget(dropd1)
        
        def func2(spinner,text):
            variables.BRANCH=text
            # print(variables.SLOT5)

        
        dropd2 = AnchorLayout(anchor_x = "center",anchor_y = "top")

        spin2 = Spinner(
        text='Select Branch',
        values=("cse","ece"),
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5},
        )

        spin2.bind(text=func2)

        dropd2.add_widget(spin2)

        self.add_widget(dropd2)
        # print(variables.SLOT)

        def func3(spinner,text):
            variables.GROUP=text
            # print(variables.SLOT5)

        
        dropd3 = AnchorLayout(anchor_x = "right",anchor_y = "top")

        spin3 = Spinner(
        text='Select Group',
        values=("1","2"),
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5},
        )

        spin3.bind(text=func3)

        dropd3.add_widget(spin3)

        self.add_widget(dropd3)
        # print(variables.SLOT)

        Go = FloatLayout() 
        btn3 = Button(text ='Next', 
                     font_size=35, pos_hint={'center_x':0.5,'center_y':0.1}, size_hint=(.13,.13))
        btn3.bind(on_release=self.next_btn)
      
        Go.add_widget(btn3) 
        self.add_widget(Go)


    def next_btn(self,event):

        sm.add_widget(ChangesScreen(name="changes_screen"))
        sm.current="changes_screen"

class Ask_class2(Screen):

    def __init__(self, **kwargs):
        super(Ask_class2, self).__init__(**kwargs)


        def func1(spinner,text):
            variables.YEAR=text

        global spin1
        global spin2
        global spin3
        dropd1 = AnchorLayout(anchor_x = "left",anchor_y = "top")

        spin1 = Spinner(
        # default value shown
        text='Select Year',
        # available values
        values=("1","2"),
        # just for positioning in our example
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5})


        spin1.bind(text=func1)
        dropd1.add_widget(spin1)
        self.add_widget(dropd1)
        
        def func2(spinner,text):
            variables.BRANCH=text
            # print(variables.SLOT5)

        
        dropd2 = AnchorLayout(anchor_x = "center",anchor_y = "top")

        spin2 = Spinner(
        text='Select Branch',
        values=("cse","ece"),
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5},
        )

        spin2.bind(text=func2)

        dropd2.add_widget(spin2)

        self.add_widget(dropd2)
        # print(variables.SLOT)

        def func3(spinner,text):
            variables.GROUP=text
            # print(variables.SLOT5)

        
        dropd3 = AnchorLayout(anchor_x = "right",anchor_y = "top")

        spin3 = Spinner(
        text='Select Group',
        values=("1","2"),
        size_hint=(None, None),
        size=(100, 44),
        pos_hint={'center_x': .5, 'center_y': .5},
        )

        spin3.bind(text=func3)

        dropd3.add_widget(spin3)

        self.add_widget(dropd3)
        # print(variables.SLOT)

        Go = FloatLayout() 
        btn3 = Button(text ='Next', 
                     font_size=35, pos_hint={'center_x':0.5,'center_y':0.1}, size_hint=(.13,.13))
        btn3.bind(on_release=self.next_btn)
      
        Go.add_widget(btn3) 
        self.add_widget(Go)


    def next_btn(self,event):

        variables.classname="{}{}_{}".format(variables.BRANCH,variables.YEAR,variables.GROUP)
        variables.db = sqlite3.connect("{}.db".format(variables.classname))
        sm.add_widget(TimeTable(name="timetable"))
        sm.current="timetable"




class ChangesScreen(Screen):

    def __init__(self, **kwargs):
        super(ChangesScreen, self).__init__(**kwargs)


        def func1(spinner,text):
            variables.DAY=text

        global spinner1
        global spinner2
        dropd1 = AnchorLayout(anchor_x = "left",anchor_y = "top")

        spinner1 = Spinner(
        # default value shown
        text='Select Day',
        # available values*
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

        variables.classname="{}{}_{}".format(variables.BRANCH,variables.YEAR,variables.GROUP)
        variables.db = sqlite3.connect("{}.db".format(variables.classname))
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
       

        self.label3=Label(text="{}".format(ReturnLecture(variables.DAY,variables.SLOT)),size_hint=(0.2,0.2),pos_hint={"x":0.45,"center_y":0.8},font_size=35)
        float1.add_widget(self.label3)
       
        
        label2= Label(text="Enter New Value:",size_hint=(0.2,0.2),pos_hint={"center_x":0.27,"center_y":0.6},font_size=30)
        float1.add_widget(label2)

        
        variables.textinput = TextInput(text='Type text here...',multiline=True,size_hint=(0.4,0.1),pos_hint={"x":0.45,"center_y":0.59})
        float1.add_widget(variables.textinput)

        btn1= Button(text="Save Change",pos_hint={"center_x":0.3,"center_y":0.2},size_hint=(0.29,0.2),font_size=30)
        btn1.bind(on_release=self.savechangesbtn)

        btn2= Button(text="Cancel",pos_hint={"center_x":0.7,"center_y":0.2},size_hint=(0.29,0.2),font_size=30)
        btn2.bind(on_release=self.cancelbtn)
        float1.add_widget(btn1)
        float1.add_widget(btn2)

        self.add_widget(float1)

    

    def savechangesbtn(self,event):
        UpdateRecord(variables.DAY,variables.SLOT,variables.textinput.text)
        # print(ReturnLecture(variables.DAY,variables.SLOT))
        sm.add_widget(TimeTable(name='timetable1'))
        sm.current="timetable1"
    
    def cancelbtn(self,event):
        sm.add_widget(TimeTable(name='timetable1'))
        sm.current="timetable1"



# def createTable():
#     db.row_factory = sqlite3.Row
#     db.execute('create table if not exists cse1(Day text, "8-9" text, "9-10" text, "10-11" text, "11-12" text, "12-1" text,"1-2" text, "2-3" text, "3-4" text, "4-5" text, "5-6" text)')

# def AddRow(Day, Schedule):
#     db.execute("insert into cse1 values(?,?,?,?,?,?,?,?,?,?,?)", (Day, Schedule[0], Schedule[1], Schedule[2], Schedule[3], Schedule[4], Schedule[5], Schedule[6], Schedule[7], Schedule[8], Schedule[9]))
#     db.commit()


def ReturnLecture(day,slot):
    
    variables.db.row_factory=sqlite3.Row
    lecture = variables.db.execute("select * from {}".format(variables.classname))
    for row in lecture:
        if row["Day"] == day:
            return row[slot]

# def DeleteElement(ID):
#     db.row_factory=sqlite3.Row
#     db.execute("delete from cse1 where ID='{}'".format(ID))
#     db.commit()

def UpdateRecord(day,slot,text):
    variables.db.row_factory=sqlite3.Row
    variables.db.execute("update {} set '{}'='{}' where Day='{}'".format(variables.classname,slot,text,day))
    variables.db.commit()



class TimeTable(Screen):
    def __init__(self, **kwargs):
        super(TimeTable, self).__init__(**kwargs)


        # createTable()
        # self.clear_widgets()
        days=["Mon","Tue","Wed","Thurs","Fri"]
        slots=["8-9","9-10","10-11","11-12","12-1","1-2","2-3","3-4","4-5","5-6"]

        space = AnchorLayout(anchor_x = "left",anchor_y = "bottom",size =self.size)

        grid = GridLayout(cols=11)
        grid.add_widget(Button(text="Back",size_hint=(0.8,0.4),pos_hint={"left_x":0.9,"center_y":0.5},on_release=self.homepage_btn))
        # grid.add_widget(layout)

        for i in range(0,10):
            label1 = Label(size_hint=(0.8,0.4),text="{}".format(slots[i]),valign="bottom",font_size=20)
            grid.add_widget(label1)
        for i in range(0,5):
            label2 = Label(size_hint=(0.1,0.05),text="{}".format(days[i]))
            grid.add_widget(label2)
            for j in range(0,10):
                # globals()['label%s' % j] = Button(id="{},{}".format(i,j+1),text="{}".format(ReturnLecture(days[i],slots[j+1])),background_color =[0.41, 0.42, 0.74, 1])
                variables.label3 = Button(id="{},{}".format(i,j),text="{}".format(ReturnLecture(days[i],slots[j])),background_color =[0.41, 0.42, 0.74, 1],font_size=9)
                # variables.label3.bind(on_release=self.label3press)
                # globals()['label%s' % j].bind(on_release=self.label3press)
                

                grid.add_widget(variables.label3)
                # grid.add_widget(globals()['label%s'%j])
        # mainbutton = Button(text='Login As', size_hint=(0.5,0.16),font_size=30,background_color=(1,1,1,1))
        space.add_widget(grid)


        self.add_widget(space)

    def homepage_btn(self,event):
        # print("2222")
        sm.current="action bar"        




class Scroller(ScrollView):
    def __init__(self):
        ScrollView.__init__(self)
        layout = GridLayout(cols=2, size_hint=(1, None),pos_hint={"left_x":4.2,"center_y":0.5})

        layout2 = GridLayout(cols=1, size_hint=(0.5, None),pos_hint={"left_x":4.2,"center_y":0.3})       
        
        layout.add_widget(Button(text=" Home \n Page",size_hint=(0.05,0.005),pos_hint={"left_x":0.9,"center_y":0.5},on_release=self.homepage_btn,font_size=22))
        ann_list=announcements_db.Return_Announcements(variables.student_year,variables.student_branch,variables.student_group)
        for i in ann_list:
            print(i)
            layout2.add_widget(Label(text=i,center_x=True))
        layout.add_widget(layout2)
        self.add_widget(layout)

    def homepage_btn(self,event):
        # self.clear_widgets()
        # print("2222")
        sm.current="action bar"        


class TestScreen(Screen):    

    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        # layout.add_widget(actionbar)
        layout.add_widget(Scroller())
        self.add_widget(layout)




class Admin_Ann(Screen):

    def __init__(self, **kwargs):
        super(Admin_Ann, self).__init__(**kwargs)


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
                     font_size=35, pos_hint={'center_x':0.3,'center_y':0.1}, size_hint=(.13,.13))
        btn3.bind(on_release=self.update_ann)
      
        btn4 = Button(text ='Cancel', 
                     font_size=35, pos_hint={'center_x':0.7,'center_y':0.1}, size_hint=(.16,.13))
        btn4.bind(on_release=self.cancel_btn)
      

        Go.add_widget(btn3) 
        Go.add_widget(btn4)
        self.add_widget(Go)


    def update_ann(self,event):

        if variables.textinput2.text == "Type new announcement here..":
            pass
        else:
            new_ann="{}    {}".format(time.strftime('%Y-%m-%d', time.localtime()), variables.textinput2.text)
            announcements_db.UpdateRecord(variables.YEAR,variables.BRANCH,variables.GROUP, new_ann)
            variables.textinput2.text="Type new announcement here.."
            spinner1.text="Select Year"
            spinner2.text="Select Branch"
            spinner3.text="Select Group"
            # announcements_db.ListAdmins()

            sm.current="action bar"  
        # print(announcements_db.ReturnLecture(variables.DAY,variables.SLOT))
        # sm.add_widget(TimeTable(name='timetable1'))
        # sm.current="timetable1"

    def cancel_btn(self,event):
        variables.textinput2.text="Type new announcement here.."
        spinner1.text="Select Year"
        spinner2.text="Select Branch"
        spinner3.text="Select Group"

        sm.current="action bar"





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

        # global mainbutton 
        variables.mainbutton = Button(text='Login As', size_hint=(0.5,0.16),font_size=30,background_color=(1,1,1,1))
        variables.mainbutton.bind(on_release=self.dropdown.open)

        self.dropdown.bind(on_select=lambda instance, x: setattr(variables.mainbutton, 'text', x))
        dropd.add_widget(variables.mainbutton)

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
        # print(mainbutton.text)

        if variables.mainbutton.text == "'Student'":
            variables.user="student"

            sm.add_widget(StudentLoginPage(name='StudentLoginPage'))
            sm.current="StudentLoginPage"
        elif variables.mainbutton.text == "'Faculty'":
            variables.user="admin"
            sm.add_widget(FacultyLoginPage(name='FacultyLoginPage'))
            sm.current="FacultyLoginPage"


class StudentLoginPage(Screen):
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
            variables.ID=loginText
            variables.password=passwordText
            self.resetForm()
            sm.current="action bar"
            # layout = FloatLayout()
            # layout.add_widget(Scroller())
            # testscreen = TestScreen(name='TestScreen')
            # testscreen.add_widget(layout)
            # self.manager.add_widget(screen=testscreen)
            # # self.manager.transition= SlideTransition(direction="left")
            # self.manager.current='TestScreen'
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


Builder.load_string('''

<StudentLoginPage>:

    BoxLayout
        id: login_layout
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50

        Label:
            text: 'Welcome'
            font_size: 32

        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Id'
                font_size: 18
                halign: 'left'
                text_size: root.width-20, 20

            TextInput:
                id: login
                multiline:False
                font_size: 28
                text: ''

        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Password'
                halign: 'left'
                font_size: 18
                text_size: root.width-20, 20

            TextInput:
                id: password
                multiline:False
                password:True
                font_size: 28
                text:''

        Button:
            text: 'Login'
            font_size: 24

            on_press: root.do_login(login.text, password.text)
 ''')
class FacultyLoginPage(Screen):

    # login=ObjectProperty(None)
    # password=ObjectProperty(None)


    def do_login(self, loginText=" ", passwordText=" "):
        # login.text=""
        if admin_logininfo.check_if_exists(loginText,passwordText)==True:
            # sm.add_widget(admin_announcementpage(name="admin announcement page"))
            variables.ID=loginText
            variables.password=passwordText
            self.resetForm()
            # login.text=""
            # password.text=""
            sm.current="action bar"
        
    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class admin_announcementpage(Screen):
    def __init__(self, **kwargs):
        super(admin_announcementpage, self).__init__(**kwargs)
        self.add_widget(Label(text="Admin Announcements"))

Builder.load_string('''

<FacultyLoginPage>:
    BoxLayout
        id: login_layout
        orientation: 'vertical'
        padding: [10,50,10,50]
        spacing: 50

        Label:
            text: 'Welcome'
            font_size: 32

        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Id'
                font_size: 18
                halign: 'left'
                text_size: root.width-20, 20

            TextInput:
                id: login
                multiline:False
                font_size: 28
                text: ''

        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Password'
                halign: 'left'
                font_size: 18
                text_size: root.width-20, 20

            TextInput:
                id: password
                multiline:False
                password:True
                font_size: 28
                text:''

        Button:
            text: 'Login'
            font_size: 24

            on_press: root.do_login(login.text, password.text)''')

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
        btn2.bind(on_release=self.cancelbtn)
        float1.add_widget(btn1)
        float1.add_widget(btn2)

        self.add_widget(float1)

    def savechangesbtn(self,event):
        if variables.textinput3.text==variables.textinput1.text:
            if variables.user=="admin":
                if admin_logininfo.checkPassword()==True:
                    admin_logininfo.changePassword()
                    sm.current="action bar"
                else:
                    self.resetForm()

            elif variables.user=="student":
                if student_logininfo.checkPassword()==True:
                    student_logininfo.changePassword()
                    self.resetForm()
                    sm.current="action bar"
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
        sm.current="action bar"
        # sm.add_widget(TimeTable(name='timetable1'))
        # sm.current="timetable1"



sm = ScreenManager() 
sm.add_widget(HomeScreen(name='screen'))
sm.add_widget(Action_Bar(name='action bar'))
sm.add_widget(Admin_Ann(name='admin_ann'))



class ActionBar(App):

    def build(self):
        return sm

if __name__ == '__main__':
    ActionBar().run()




