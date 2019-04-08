from threading import Thread
import paho.mqtt.client as mqtt
from Sensor import Sensor
from time import sleep
import threading



class mqtt_rpi:

    

    
    broker = "129.241.208.68"
    port = 1883
        

    def __init__(self):
        sensor = Sensor()
        keep_sending = False
        self.start()
    def send_data(self):
        try:
            self.keep_sending = True
            while self.keep_sending:
                self.client.publish("temperature", self.sensor.temperature_sensor())
                self.client.publish("humidity", self.sensor.humidity_sensor())
                sleep(1)

        except e:
            print ("dette er feil", e)
            

    def start(self):
        self.client = mqtt.Client()
        print('Connecting to {}:{}'.format(self.broker, self.port))
        self.client.connect(self.broker, self.port)
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
#test = mqtt_rpi()
