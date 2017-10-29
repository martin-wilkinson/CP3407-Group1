from kivy.app import App
from random import *
from kivy.app import Widget
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
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
    battery_int = 99
    battery = StringProperty("99%")
    sensor_status = StringProperty("Ok")
    status_strings = ["OK", "OK", "OK", "OK", "OK"]
    pump_status = StringProperty("Ok")
    delivery_status = StringProperty("Ok")
    needle_status = StringProperty("Ok")
    reservoir_status = StringProperty("Ok")
    insulin_status = StringProperty("Ok")

    def status_update(self,*args):
        self.sensor_status = "{}".format(self.status_strings[0])
        self.pump_status = "{}".format(self.status_strings[1])
        self.delivery_status = "{}".format(self.status_strings[2])
        self.needle_status = "{}".format(self.status_strings[3])
        self.reservoir_status = "{}".format(self.status_strings[4])

        self.schedule_status_update()

    def schedule_status_update(self):
        checks = ['TRUE', 'TRUE', 'FALSE', 'TRUE', 'FALSE']
        ids = [self.ids.Sensor, self.ids.Pump, self.ids.Delivery, self.ids.Needle, self.ids.Reservoir]
        states = ["OK", "FAIL"]
        for i in range(0, 5):
            if checks[i] == 'FALSE':
                self.status_strings[i] = states[1]
                ids[i].color = (0.97, 0.27, 0.27, 1)
            else:
                self.status_strings[i] = states[0]
                ids[i].color = (0.28, 0.97, 0.29, 1)
        Clock.schedule_once(self.status_update, 30)

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

    def battery_update(self, *args):

        self.battery = "{}%".format(self.battery_int)

        self.schedule_battery_update()

    def schedule_battery_update(self):
        if self.battery_int > 9:
            self.battery_int = self.battery_int - 10

        if self.battery_int > 50:
            self.ids.Battery.color = (0.28, 0.97, 0.29, 1)
        elif self.battery_int > 15:
            self.ids.Battery.color = (0.95, 0.95, 0.13, 1)
        else:
            self.ids.Battery.color = (0.97, 0.27, 0.27, 1)
        Clock.schedule_once(self.battery_update, 600)

    #def sensor_update(self, *args):


    #def schedule_sensor_update(self):


    #def pump_update(self, *args):

    #def schedule_pump_update(self):

    ##def delivery_update(self, *args):

    #def schedule_delivery_update(self):

    #def needle_update(self, *args):

    #def schedule_needle_update(self):

    #def reservoir_update(self, *args):

    #def schedule_reservoir_update(self):

    #def insulin_update(self, *args):

    #def schedule_insulin_update(self):


class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        container = Container()
        container.update()
        container.battery_update()
        container.status_update()
        return container

if __name__ == "__main__":
    MainApp().run()

