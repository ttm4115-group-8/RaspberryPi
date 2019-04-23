import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish
import paho.mqtt.client as client
from sense_hat import SenseHat
import subprocess
import pygame as pygame


class Sensor:

	sense = SenseHat()
	sense.clear(255,0,0)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16,GPIO.IN)
		

		
	def alarm(self):
		self.play_alarm = True
		pygame.mixer.init()
		pygame.mixer.music.load("alarm.wav")
		pygame.mixer.music.play()
		while self.play_alarm:
			continue
		pygame.mixer.music.stop()				
	#returns motion

	def motion_sensor(self):  #define which pin the motion sensor is connected to on the breadboard
		return GPIO.input(16)

	def humidity_sensor(self):
		return self.sense.get_humidity()

	# returns temperature	
	
	def temperature_sensor(self):
		return self.sense.get_temperature() -13


										
	def start(self):
		
		temp = self.temperature_sensor()
		print(self.motion_sensor())
		#print(temp)
		#print(self.humidity_sensor())
		#self.button()
	
"""
testing = Sensor()


while True:
		time.sleep(1)
		testing.start()
"""
