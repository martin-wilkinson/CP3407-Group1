import time
from os import listdir


from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

from InsulinPump import *
from database import *

kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

colorIterator = 0
button_count = 0
current = 0
count = 1
reservoir = int(reservoirLevel())
message_applied_time = time.time()
last_time = 0
daily_dosage = 0
HIGH = 7
LOW = 3
MAX_DAILY_DOSAGE = 10
MAX_DOSAGE = 3
DOSE = 1


class Container(GridLayout):
    manual_mode = StringProperty("FALSE")
    latest_message = StringProperty("No Message")
    time = StringProperty("00:00")
    blood_glucose_level = StringProperty("0")
    last_dose = StringProperty("1")
    battery_int = 99
    battery = StringProperty("99%")
    sensor_status = StringProperty("Ok")
    status_strings = ["OK", "OK", "OK", "OK", "OK"]
    pump_status = StringProperty("Ok")
    delivery_status = StringProperty("Ok")
    needle_status = StringProperty("Ok")
    reservoir_status = StringProperty("Ok")
    insulin_status = StringProperty("Ok")

    def status_update(self, *args):
        self.sensor_status = "{}".format(self.status_strings[0])
        self.pump_status = "{}".format(self.status_strings[1])
        self.delivery_status = "{}".format(self.status_strings[2])
        self.needle_status = "{}".format(self.status_strings[3])
        self.reservoir_status = "{}".format(self.status_strings[4])

        self.schedule_status_update()

    def schedule_status_update(self):
        global count
        checks = get_status_checks(count)
        ids = [self.ids.Sensor, self.ids.Pump, self.ids.Delivery, self.ids.Needle, self.ids.Reservoir]
        states = ["OK", "FAIL"]
        for i in range(0, 5):
            if checks[i] == 'FALSE':
                self.status_strings[i] = states[1]
                ids[i].color = (0.97, 0.27, 0.27, 1)
            else:
                self.status_strings[i] = states[0]
                ids[i].color = (0.28, 0.97, 0.29, 1)
        Clock.schedule_once(self.status_update, 5)

    def buttonPress(self):
        global colorIterator
        global button_count
        global last_time
        if colorIterator == 0:
            self.ids.manualButton.background_color = (0.28, 0.97, 0.29, 1)
            self.ids.manualButton.text = "ON"
            self.ids.doseButton.background_color = (0.28, 0.97, 0.29, 1)
            self.ids.doseButton.text = "DOSE"
            self.manual_mode = "TRUE"
            button_count = 0
            last_time = 0
            colorIterator = 1
        else:
            self.ids.manualButton.background_color = (0.97, 0.27, 0.27, 1)
            self.ids.manualButton.text = "OFF"
            self.manual_mode = "FALSE"
            self.ids.doseButton.text = "DISABLED"
            self.ids.doseButton.background_color = 0.65, 0.60, 0.60, 1
            colorIterator = 0

    def add_dose(self):
        global button_count
        global last_time
        global daily_dosage
        current_time = time.time()
        button_count += 1
        if self.manual_mode == "TRUE":
            if current_time - last_time > 5:
                manualDosage = manualAdminister(button_count, daily_dosage, current_time)
        else:
            pass
        last_time = current_time

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

    # Simulates slow drain of battery
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

    # Print message making sure that messages are not present for less than 5 seconds to ensure readability
    def update_message_box(self, message):
        global message_applied_time
        while (time.time() - message_applied_time) < 5:
            pass
        self.latest_message = message

    # Automatic Functionality
    def auto_mode(self):
        global count  # This iterates through the data in CSV.
        global current
        global daily_dosage
        global reservoir
        previous = current
        current = getSugarLevels(count)
        rate = getRate(current, previous)
        can_administer = canAdminister(rate, current)
        if can_administer[0] is True:
            message = "{}: {}".format(time, canAdminister(rate, current)[1])
            self.update_message_box(message)
            if rate >= MAX_DOSAGE:
                rate = MAX_DOSAGE
            canDose = cumlativeDose(rate, daily_dosage)[0]
            if reservoir >= rate and canDose:
                daily_dosage = cumlativeDose(rate, daily_dosage)[1]
                message3 = "{}: Insulin Delivered.".format(time)
                self.update_message_box(message3)
            elif cumlativeDose(rate, daily_dosage) is False:
                dailyExceedMessage = "{}: Daily Dosage exceeded.".format(time)
                self.update_message_box(dailyExceedMessage)
            elif reservoir < rate:
                emptyReservoirMessage = "{}: Reservoir out of insulin.".format(time)
                self.update_message_box(emptyReservoirMessage)
                self.last_dose = daily_dosage
        else:
            self.update_message_box(can_administer[1])

        if count == 19:
            count = 1
        else:
            count += 1
        self.schedule_amode_update()

    def schedule_amode_update(self):
        Clock.schedule_once(self.auto_mode(), 5)


class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        container = Container()
        container.update()
        container.battery_update()
        container.status_update()
        container.schedule_amode_update()
        return container

create_tables()

if __name__ == "__main__":
    MainApp().run()

