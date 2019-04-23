# coding=utf-8
from stmpy import Machine, Driver
from mqtt_rpi import mqtt_rpi
from sense_hat import SenseHat
import threading
from time import sleep
import time
	
class Raspberry_Pi:
	client = mqtt_rpi()
	snooze_exist = False
	snooze_alarm = False
	alarm_exist = False
	run_alarm = False
		
	def start_button(self):
		button_thread = threading.Thread(target=self.button)
		button_thread.start()
		

	def start_sensor(self): #begin sending data to the server
		sensor_thread = threading.Thread(target=self.client.send_data)
		sensor_thread.start()



	def ring_alarm(self):
		alarm_thread = threading.Thread(target = self.client.sensor.alarm)
		alarm_thread.start()


	def alarm_set(self):  #send message to state machine wether alarm is set or not
		#hardcoded in return true and false, since I can't communicate with the server yet
		self.client.get_timer()
		if self.client.tidspunkt == None:
						self.stm.send("alarm_not_set")
		else:
			self.stm.send("alarm_is_set")

	def single_button_press(self):
		self.stm.send('single_button_press')

	def hold_button(self):
		self.stm.send('hold_button')

	def stop_alarm(self):
		#mekk stopp alarm
		self.client.sensor.play_alarm = False


	def store_data(self):
		if self.alarm_exist:
			self.run_alarm = False
		if self.snooze_exist:
			self.snooze_alarm = False
		self.client.keep_sending = False

	def initiate_timer(self): #set timer by looking at alarm time from the website
		#må fikse denne
		timer_thread = threading.Thread(target = self.alarm_timer)
		timer_thread.start()

		
	def alarm_timer(self):
			self.run_alarm = True
			self.alarm_exist = True
			mins = 0
			while mins!=6 and self.run_alarm:
					sleep(10)
					mins += 1
			if self.run_alarm:
					self.stm.send("timer")
					self.run_alarm = False
	def snooze(self): 
			snooze_thread = threading.Thread(target = self.snooze_timer)
			snooze_thread.start()
	
	def snooze_timer(self):
			self.snooze_alarm = True
			self.snooze_exist = True
			mins = 0
			while mins!=1 and self.snooze_alarm:
					sleep(10)
					mins += 1
			if self.snooze_alarm:
					self.stm.send("timer")
					self.snooze_alarm = False
	
	def in_idle(self):
		print("in idle")
	def in_choice_state(self):
		print("in choice state")
	def in_record_data(self):
		print("in record data")
	def in_sleeping(self):
				
		print("in sleeping")
	def in_wake(self):
		print("in wake")
			
	def button(self):
		sense = SenseHat()
		while True:
			event = sense.stick.wait_for_event(emptybuffer = True)
			print(event.action)
			if			event.action == "pressed":
								self.single_button_press()
			elif event.action == "held":
								self.hold_button()
			
	




rpi = Raspberry_Pi()

# Initial transition
t0 = {'source': 'initial',
	  'target': 'Idle',
	  'effect':'start_button'}

# react to singe_button_press, go to either Sleeping (if alarm is not set) or Recorddata if alarm is not set
# runs function that returns alarm if alarm is set, and no_alarm if alarm is not set

t1 = {'trigger':'single_button_press', #react to a button press
	  'source':'Idle',
	 'target': 'ChoiceState'} #go to choice state, where choice state decides where to go, Sleeping or RecordData


t2 = {'trigger':'alarm_is_set', #alarm is set, go to sleeping
	  'source':'ChoiceState',
	  'effect':'initiate_timer', #this function starts a timer which fetches alarm time to calculate timer
	  'target':'Sleeping'}

t3 = {'trigger':'alarm_not_set', #alarm isn't set, go to record data
	  'source':'ChoiceState',
	  'target':'RecordData'}

t4 = {'trigger':'timer',  #timer is up, go to wake the user
	  'source':'Sleeping',
	 'target': 'Wake'}

t5 = {'trigger':'on_notify_rpi_alarm',  #the user is active and alarm time is close, wake the user
	  'source':'Sleeping',
	  'target':'Wake'}

t6 = {'trigger':'hold_button',  #user recognized the alarm and turned it off, go to idle
	  'source':'Wake',
	  'effect':'store_data',
	  'target':'Idle'}


t7 = {'trigger':'single_button_press',  #user snoozed, start timer and go back to Sleeping
	  'source':'Wake',
	  'effect':'snooze',
	  'target':'Sleeping'}

t8 = {'trigger':'single_button_press',
	  'source':'RecordData',
	  'effect':'store_data',
	  'target':'Idle'}

t9 = {'trigger': 'hold_button',
	  'source': 'Sleeping',
	  'effect': 'store_data',
	  'target':'Idle'}

# States:

Idle = {'name': 'Idle',
		'entry':'in_idle()'}

ChoiceState = {'name': 'ChoiceState',
		'entry': 'alarm_set();in_choice_state()'} #this function must decide if alarm is set or not

RecordData = {'name': 'RecordData',
		'entry': 'start_sensor();in_record_data()'}

Sleeping = {'name': 'Sleeping',
		'entry': 'start_sensor();in_sleeping()'}

Wake = {'name': 'Wake',
		'entry': 'ring_alarm();in_wake()',
		'exit': 'stop_alarm()'}  #this function wakes the user

#set transitions and states. object is set to Raspberry_Pi, change this if class name is different
machine = Machine(name='rpi', transitions=[t0, t1, t2, t3, t4, t5, t6, t7, t8, t9], obj=rpi, states=[Idle, ChoiceState, RecordData, Sleeping, Wake])
rpi.stm = machine
driver = Driver()
driver.add_machine(machine)
driver.start()
