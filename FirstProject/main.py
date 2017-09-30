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

class Container(GridLayout):
    def buttonPress(self):
        insultList = ['Fuck You Brigitte', 'Brigitte is a monster', 'Brigitte the bed hog',
                      'Brigitte is the best... jks']

        self.ids.L1.text = insultList[randint(0, 3)]




class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        return Container()

if __name__ == "__main__":
    MainApp().run()

