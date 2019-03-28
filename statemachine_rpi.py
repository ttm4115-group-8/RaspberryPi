
from stmpy import Machine, Driver

# Initial transition
t0 = {'source': 'initial',
      'target': 'idle'}

# react to singe_button_press, go to either Sleeping (if alarm is not set) or Recorddata if alarm is not set
# runs function that returns alarm if alarm is set, and no_alarm if alarm is not set

t1 = {'trigger':single_button_press(),
      'source':'idle',
     'function': alarm_set()}


t2 = {'trigger':'t',
      'source':'waiting_on',
      'target':'lamp_off'}

t3 = {'trigger':'no_hand',
      'source':'waiting_on',
      'target':'lamp_on'}

# Turn off
t4 = {'trigger':'hand',
      'source':'lamp_on',
     'target': 'waiting_off'}

t5 = {'trigger':'t',
      'source':'waiting_off',
      'target':'lamp_on'}

t6 = {'trigger':'no_hand',
      'source':'waiting_off',
      'target':'lamp_off'}

# States:
lamp_off = {'name': 'lamp_off',
            'entry': 'off()'}

lamp_on = {'name': 'lamp_on',
        'entry': 'on()'}

waiting_on = {'name': 'waiting_on',
        'entry': 'start_timer("t", 1000)'}

waiting_off = {'name': 'waiting_off',
        'entry': 'start_timer("t", 1000)'}


machine = Machine(name='head_lamp', transitions=[t0, t1, t2, t3, t4, t5, t6], obj=head_light, states=[lamp_off, lamp_on, waiting_on, waiting_off])
head_light.stm = machine

driver = Driver()
driver.add_machine(machine)
driver.start()
