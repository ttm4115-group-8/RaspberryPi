"""this is the RaspBerry_Pi class. This is will hold the functions associated with the state machine
send sensor data, communicate with the server, wake the user and so on
"""




class RaspberryPi:

    def start_sensor(self): #begin sending data to the server
        print("fsd")


    def ring_alarm(self):
        print("fdd")


    def alarm_set(self):  #send message to state machine wether alarm is set or not
        print("fdfsd")

    def single_button_press(self):
        self.stm.send('single_button_press')

    def hold_button(self):
        self.stm.send('hold_button')

    def stop_alarm(self):
        print("mekk stopp alarm")

    def store_data(self):
        print("stop sending av data")


