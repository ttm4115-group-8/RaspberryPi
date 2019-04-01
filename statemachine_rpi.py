
from stmpy import Machine, Driver

# Initial transition
t0 = {'source': 'initial',
      'target': 'Idle'}

# react to singe_button_press, go to either Sleeping (if alarm is not set) or Recorddata if alarm is not set
# runs function that returns alarm if alarm is set, and no_alarm if alarm is not set

t1 = {'trigger':single_button_press(), #react to a button press
      'source':'Idle',
     'target': 'ChoiceState'} #go to choice state, where choice state decides where to go, Sleeping or RecordData


t2 = {'trigger':alarm_is_set(), #alarm is set, go to sleeping
      'source':'ChoiceState',
      'function':start_timer(), #this function starts a timer which fetches alarm time to calculate timer
      'target':'Sleeping'}

t3 = {'trigger':alarm_not_set(), #alarm isn't set, go to record data
      'source':'ChoiceState',
      'target':'RecordData'}

t4 = {'trigger':'t',  #timer is up, go to wake the user
      'source':'Sleeping',
     'target': 'Wake'}

t5 = {'trigger':on_notify_rpi_alarm(),  #the user is active and alarm time is close, wake the user
      'source':'Sleeping',
      'target':'Wake'}

t6 = {'trigger':hold_button(),  #user recognized the alarm and turned it off, go to idle
      'source':'Wake',
      'function':store_data(),stop_alarm(),
      'target':'Idle'}


t7 = {'trigger':single_button_press(),  #user snoozed, start timer and go back to Sleeping
      'source':'Wake',
      'function':start_timer(t,60000),snooze_alarm(),
      'target':'Sleeping'}

# States:

ChoiceState = {'name': 'ChoiceState',
        'entry': 'alarm_set()'} #this function must decide if alarm is set or not

RecordData = {'name': 'RecordData',
        'entry': 'start_sensors()'}

Sleeping = {'name': 'Sleeping',
        'entry': 'start_sensors()'}

Wake = {'name': 'Wake',
        'entry': 'ring_alarm()'}  #this function wakes the user

#set transitions and states. object is set to Raspberry_Pi, change this if class name is different
machine = Machine(name='Raspberry_Pi', transitions=[t0, t1, t2, t3, t4, t5, t6, t7], obj=Raspberry_Pi, states=[ChoiceState, RecordData, Sleeping, Wake])
Raspberry_Pi.stm = machine

driver = Driver()
driver.add_machine(machine)
driver.start()
