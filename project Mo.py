# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# import time
# 
# kivy.require('1.9.0')
#  
# # The Label widget is for rendering text.
# from kivy.uix.label import Label
#  
# # The Clock object allows you to sched# this restrict the kivy version i.e 
# # below this kivy version you cannot 
# # use the app or software 
# kivy.require('1.9.0')
#  
# # The Label widget is for rendering text.
# from kivy.uix.label import Label
#  
# # The Clock object allows you to schedule
# # a function call in the future; once or
# # repeatedly at specified intervals.
# from kivy.clock import Clock
  
# The kivy App that extends from the App class

# 
# class Mohamed(App):
#     def build(self):
#         mybutton = Button(text = "Hello World!", size_hint = (1,.5), pos_hint = {"center_x": .5, "center_y": .5})
#         mybutton.bind(on_press = self.displaySomething)
#         return mybutton    
#     
#     def displaySomething(self, instance):
#         print("butoon is pressed")
#       
# Mohamed().run()

from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
import time
import datetime
ref_time = datetime.datetime.now().strftime("%I:%M:%S")
print(ref_time)
# set window size
Window.size = (390, 844)
#red background color
Window.clearcolor = (1, 1, 1, 1)
Builder.load_string("""
<Layout>
    ClockLabel:
        id: clock_label
        size_hint: 1,1.5
        font_size: 80
        color: 'black'
        markup: True
""")
# create layout class
class Layout(BoxLayout):
    pass
# clocklabel class to display
# updated time label
class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
    def update(self, *args):
        current_time =
        sub_time = 
        self.text = f"[u]{time.strftime('%I:%M:%S', sub_time)}[/u]" #strftime(format, time)
# Extend kivy's App class
# with new class  
class DigitalClockApp(App):
    def build(self):
        return Layout()
# create object
clock = DigitalClockApp()
# run app
clock.run()

