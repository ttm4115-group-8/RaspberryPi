import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish
import paho.mqtt.client as client
from sense_hat import SenseHat
import subprocess


class RPI_SENSOR:

	sense = SenseHat()
	sense.clear(200,233,80)
	
	'''def __init__(self):
                print ("hallo")
		#self.broker = "localhost"
		#self.port = 1883'''
	
	#returns motion

	def motion_sensor(self,SENSOR_PIN):  #define which pin the motion sensor is connected to on the breadboard
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(SENSOR_PIN,GPIO.IN)
		return GPIO.input(SENSOR_PIN)

	def humidity_sensor(self):
		return self.sense.get_humidity()

	# returns temperature	
	
	def temperature_sensor(self):
		return self.sense.get_temperature() -13


        def button(self):
                for event in sense.stick.get_events():
                        if sense.direction=="middle":
                                
	
		
	'''def start(self):
		
		temp = self.temperature_sensor()
		#print(self.motion_sensor(16))
		print(temp-13)
		print(self.humidity_sensor())

testing = RPI_SENSOR()
testing.start()'''
	
