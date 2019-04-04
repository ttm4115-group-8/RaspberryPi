from threading import Thread
import paho.mqtt.client as mqtt
import Sensor
import Raspberry_Pi
from time import sleep

broker = "129.241.208.68"
port = 1883
	
class MQTT_Client:

    def __init__(self, RPI):
        self.sensor = Sensor.RPI_SENSOR(RPI)
        self.start(broker, port)
        keep_sending = False
        
    def send_data(self):
        try:
            self.keep_sending = True
            while self.keep_sending:
                self.client.publish("temperature", sensor.temperature_sensor())
                self.client.publish("humidity", sensor.humidity_sensor())
                sleep(1)

        except e:
            print ("dette er feil", e)
            

    def start(self, broker, port):
        self.client = mqtt.Client()
        print('Connecting to {}:{}'.format(broker, port))
        self.client.connect(broker, port)
        print("connect")
        
'''
        try:
            thread = Thread(target=self.client.loop_forever())
            thread.start()
        except KeyboardInterrupt:
            print('Interrupted')
            self.client.disconnect()

test = MQTT_Client()
test.start(broker, port)
'''
