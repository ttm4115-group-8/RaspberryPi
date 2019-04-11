from threading import Thread
import paho.mqtt.client as mqtt
from Sensor import Sensor
from time import sleep
import threading



class mqtt_rpi:

    tidspunkt=None
    broker = "129.241.208.68"
    port = 1883
    sensor = Sensor()
    client = mqtt.Client()
    
    def __init__(self):
        keep_sending = False
        self.client.on_message = self.on_message
        self.start()
    def send_data(self):
        print("sender data")
        try:
            self.keep_sending = True
            while self.keep_sending:
                self.client.publish("temperature", self.sensor.temperature_sensor())
                self.client.publish("humidity", self.sensor.humidity_sensor())
                self.sensor.sense.clear(0,255,0)
            self.sensor.sense.clear(255,0,0)

        except e:
            print ("dette er feil", e)
            

    def get_timer(self):
        self.client.publish("timer_request", "give me timer")

    def on_message(self,client,userdata, mag):
        self.tidspunkt=msg.payload
        print(tidspunkt)

    def start(self):
        print('Connecting to {}:{}'.format(self.broker, self.port))
        self.client.connect(self.broker, self.port)
        print("connect")
