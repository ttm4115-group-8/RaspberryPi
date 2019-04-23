from threading import Thread
import paho.mqtt.client as mqtt
from Sensor import Sensor
from time import sleep
import threading
from datetime import datetime, timedelta
import math

class mqtt_rpi:

    tidspunkt = None
    broker = "129.241.208.68"
    port = 1883
    sensor = Sensor()
    client = mqtt.Client()
    
    def __init__(self):
        keep_sending = False
        #self.client.on_message = self.on_message
        self.start()
        self.client.subscribe("timer_response")
    def send_data(self):
        print("sender data")
        try:
            self.keep_sending = True
            while self.keep_sending:
                self.client.publish("temperature", self.sensor.temperature_sensor())
                self.client.publish("humidity", self.sensor.humidity_sensor())
                self.client.publish("movement",self.sensor.motion_sensor())
                self.sensor.sense.clear(0,255,0)
            self.sensor.sense.clear(255,0,0)

        except e:
            print ("dette er feil", e)
            

    def get_timer(self):
        #self.tidspunkt = "kjørrrr"
        self.client.publish("timer_request", "give me timer")

    """
    def on_message(self,client,userdata, msg):
        if msg.topic == "timer_response":
            message = msg.payload.decode()
            message_splitted = message.split(":") # message_splitted[0] is hour, [1] is minute
            hour, minute = int(message_splitted[0]), int(message_splitted[1])

            dtnow = datetime.now()
            print(dtnow)
            future_date = None

            if dtnow.hour < hour:
                future_date = datetime(dtnow.year, dtnow.month, dtnow.day, hour, minute, 0, 0)
                print("Samme dag")
            else:
                print("Neste dag")
                day = timedelta(days=1)
                tomorrow = dtnow + day
                future_date = datetime(tomorrow.year, tomorrow.month, tomorrow.day, hour, minute, 0, 0)

            timestamp = time.mktime(future_date.timetuple())

            print(timestamp)
            
            now = time.time()
            timestamp_difference = timestamp - now
            self.tidspunkt = math.floor(timestamp_difference / 60) 
            
            print(self.tidspunkt)
            self.done = True
            """

    def start(self):
        print('Connecting to {}:{}'.format(self.broker, self.port))
        self.client.connect(self.broker, self.port)
        print("connect")
"""
        client_thread = Thread(target=self.client.loop_start())
        client_thread.start()

mqtt = mqtt_rpi()

mqtt.get_timer()
print("fSDFDSfsdfsd")
"""
