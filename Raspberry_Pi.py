"""this is the RaspBerry_Pi class. This is will hold the functions associated with the state machine
send sensor data, communicate with the server, wake the user and so on
"""

from mqtt_rpi import mqtt_rpi
from sense_hat import SenseHat
import threading
	
class Raspberry_Pi:

	def start_in_idle(self):
		button = threading.Thread(target = self.button())
		button.start()
		client = mqtt_rpi()
	

	def start_sensor(self): #begin sending data to the server
		sensor = threading.Thread(target = self.client.send_data())
		sensor.start()
		print("didn't start send data thread")
		print("start_sensor")



	def ring_alarm(self):
		alarm = threading.Thread(target = self.client.sensor.alarm())


	def alarm_set(self):  #send message to state machine wether alarm is set or not
		print("hardcoded in return true and false, since I can't communicate with the server yet")
		self.stm.send("alarm_not_set")

	def single_button_press(self):
		self.stm.send('single_button_press')
		print("single_button_press")

	def hold_button(self):
		self.stm.send('hold_button')

	def stop_alarm(self):
		print("mekk stopp alarm")
		self.client.sensor.play_alarm = False


	def store_data(self):
		print("stop sending av data")
		self.client.keep_sending = False

	def start_timer(self): #set timer by looking at alarm time from the website
		print("må fikse dennse")

	def button(self):
		sense = SenseHat()
		print("button lytter")
		while True:
			for event in sense.stick.get_events():
				if event.action == "pressed" and not event.action == "held":
					print("pressed")
					self.single_button_press()
				elif event.action == "held":
					print("held")
					self.hold_button()
	


