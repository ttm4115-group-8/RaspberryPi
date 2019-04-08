import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish
import paho.mqtt.client as client
from sense_hat import SenseHat
import subprocess
import pygame as pygame


class Sensor:

	sense = SenseHat()
	sense.clear(0,0,255)
	

	def alarm(self):
		self.play_alarm = True
		pygame.mixer.init()
		pygame.mixer.music.load("alarm.wav")
		pygame.mixer.music.play()
		while self.play_alarm:
			continue
		pygame.mixer.music.stop()				
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


										
	'''def start(self):
		
		temp = self.temperature_sensor()
		#print(self.motion_sensor(16))
		print(temp)
		print(self.humidity_sensor())
		self.button()
	

testing = RPI_SENSOR()

testing.start()
'''
