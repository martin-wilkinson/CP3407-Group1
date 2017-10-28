from kivy.app import App
from random import *
from kivy.app import Widget
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.clock import Clock

import time


from os import listdir
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

colorIterator = 0


class Container(GridLayout):

    time = StringProperty("00:00")

    def buttonPress(self):
        global colorIterator
        if colorIterator == 0:
            self.ids.manualButton.background_color = (0.28, 0.97, 0.29, 1)
            self.ids.manualButton.text = "ON"
            colorIterator = 1
        else:
            self.ids.manualButton.background_color = (0.97, 0.27, 0.27, 1)
            self.ids.manualButton.text = "OFF"
            colorIterator = 0

    def update(self, *args):
        self.time = time.strftime("%H : %M")
        self.schedule_update()

    def schedule_update(self):
        current_time = time.localtime()
        seconds = current_time[5]

        secs_to_next_minute = 60 - seconds

        Clock.schedule_once(self.update, secs_to_next_minute)






class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        container = Container()
        container.update()

        return container

if __name__ == "__main__":
    MainApp().run()

