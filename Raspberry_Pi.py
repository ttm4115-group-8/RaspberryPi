"""this is the RaspBerry_Pi class. This is will hold the functions associated with the state machine
send sensor data, communicate with the server, wake the user and so on
"""

from mqtt_rpi import mqtt_rpi
from sense_hat import SenseHat
import threading
	
class Raspberry_Pi:

	def start_in_idle(self):
		print("idle")
		try:
		threading.start_new_thread(self.button())
		except:
		print("didn't start button thread")
		client = mqtt_rpi()
	

	def start_sensor(self): #begin sending data to the server
		try:
		threading.start_new_thread(self.client.send_data())
		except:
		print("didn't start send data thread")
		
		print("start_sensor")



	def ring_alarm(self):
		self.client.sensor.alarm()


	def alarm_set(self):  #send message to state machine wether alarm is set or not
		print("hardcoded in return true and false, since I can't communicate with the server yet")
		self.stm.send("alarm_not_set")

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

	def start_timer(self): #set timer by looking at alarm time from the website
		print("må fikse dennse")

	def button(self):
		sense = SenseHat()
		sense.clear(200,233,80)
		print("button lytter")
		while True:
			for event in sense.stick.get_events():
				if event.action == "pressed":
					print("pressed")
					sense.clear(0,0,255)
					self.single_button_press()
				elif event.action == "held":
					sense.clear(255,0,255)
					self.hold_button()
	


