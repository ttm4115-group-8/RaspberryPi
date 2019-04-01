import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
	temperature = sensor.get_temperature(22)
	print("The temperature is %s celsius" %temperature)
	time.sleep(1)
