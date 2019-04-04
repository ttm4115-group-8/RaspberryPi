"""this is the RaspBerry_Pi class. This is will hold the functions associated with the state machine
send sensor data, communicate with the server, wake the user and so on
"""

from .mqtt_rpi import mqtt_rpi


class RaspberryPi:

    def __init__(self):
        self.client = mqtt_rpi(self)

    def start_sensor(self): #begin sending data to the server
        self.client.send_data()



    def ring_alarm(self):
        self.client.sensor.alarm()


    def alarm_set(self):  #send message to state machine wether alarm is set or not
        print("hardcoded in return true and false, since I can't communicate with the server yet")
        self.stm.send("alarm_set")

    def single_button_press(self):
        self.stm.send('single_button_press')

    def hold_button(self):
        self.stm.send('hold_button')

    def stop_alarm(self):
        print("mekk stopp alarm")
        self.client.sensor.play_alarm = False


    def store_data(self):
        print("stop sending av data")
        self.client.keep_sending = False


