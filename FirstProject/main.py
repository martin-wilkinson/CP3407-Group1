from kivy.app import App
from random import *
from kivy.app import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

from os import listdir
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

colorIterator = 0


class Container(GridLayout):
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







class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        return Container()

if __name__ == "__main__":
    MainApp().run()

