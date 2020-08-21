# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.recycleview import RecycleView
# from kivy.uix.recycleview.views import RecycleDataViewBehavior
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.properties import BooleanProperty
# from kivy.uix.recycleboxlayout import RecycleBoxLayout
# from kivy.uix.behaviors import FocusBehavior
# from kivy.uix.recycleview.layout import LayoutSelectionBehavior
# import announcements_db
# import variables

# Builder.load_string('''
# <SelectableLabel>:

#     # Draw a background to indicate selection
#     canvas.before:
#         Color:
#             rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
#         Rectangle:
#             pos: self.pos
#             size: self.size
#     label1_text: 'label 1 text'
#     pos: self.pos
#     size: self.size
    
#     Label:
#         id: id_label1
#         text: root.label1_text

# <RV>:
#     viewclass: 'SelectableLabel'
#     SelectableRecycleBoxLayout:
#         default_size: None, dp(56)
#         default_size_hint: 1, None
#         size_hint_y: None
#         height: self.minimum_height
#         orientation: 'vertical'
#         multiselect: True
#         touch_multiselect: True
# ''')


# # items_1 = {'apple', 'banana', 'pear', 'pineapple'}
# # items_2 = {'dog', 'cat', 'rat', 'bat'}

# # items_2={"i"}
# # items_3={"j"}

# class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
#                                  RecycleBoxLayout):
#     ''' Adds selection and focus behaviour to the view. '''


# class SelectableLabel(RecycleDataViewBehavior, GridLayout):
#     ''' Add selection support to the Label '''
#     index = None
#     selected = BooleanProperty(False)
#     selectable = BooleanProperty(True)
#     cols = 3

#     def refresh_view_attrs(self, rv, index, data):
#         ''' Catch and handle the view changes '''
#         self.index = index
#         self.label1_text = data['label1']['text']
#         # self.label2_text = data['label2']['text']
#         # self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
#         return super(SelectableLabel, self).refresh_view_attrs(
#             rv, index, data)

#     def on_touch_down(self, touch):
#         ''' Add selection on touch down '''
#         if super(SelectableLabel, self).on_touch_down(touch):
#             return True
#         if self.collide_point(*touch.pos) and self.selectable:
#             return self.parent.select_with_touch(self.index, touch)

#     def apply_selection(self, rv, index, is_selected):
#         ''' Respond to the selection of items in the view. '''
#         self.selected = is_selected
#         if is_selected:
#             print("selection changed to {0}".format(rv.data[index]))
#         else:
#             print("selection removed for {0}".format(rv.data[index]))


# class RV(RecycleView):
#     def __init__(self, **kwargs):
#         super(RV, self).__init__(**kwargs)

#         items_1=announcements_db.Return_Announcements(variables.student_year,variables.student_branch,variables.student_group)
#         self.data = []
#         for i1 in items_1:
#             d = {'label1': {'text': i1}}
#             self.data.append(d)
#         # can also be performed in a complicated one liner for those who like it tricky
#         # self.data = [{'label2': {'text': i1}, 'label3': {'text': i2}} for i1, i2 in zip(items_1, items_2)]


# class Next_Page(App):
#     def build(self):
#         return RV()

# if __name__ == '__main__':
#     Next_Page().run()
