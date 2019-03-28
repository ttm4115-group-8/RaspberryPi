import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish
import paho.mqtt.client as client
from sense_hat import SenseHat


class RPI_SENSOR:

	broker,port = "fsdfsdfsdfsd", 1184 #set this to correct values for server and port
	sense = SenseHat()
	sense.clear()

	def __init__(self):


	#returns motion

	def motion_sensor(self,SENSOR_PIN):  #define which pin the motion sensor is connected to on the breadboard
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(SENSOR_PIN,GPIO.IN)
		return GPIO.input(SENSOR_PIN)
	
	# returns temperature	

        def temperature_sensor(self):
		return self.sense.get_temperature()

	def start(self):
		print(self.motion_sensor(self,16)
		#print(self.temperature_sensor(self)


testing = RPI_SENSOR()
testing.start()
	
