from threading import Thread
import paho.mqtt.client as mqtt
import Sensor
from time import sleep

broker = "129.241.208.68"
port = 1883
	
class MQTT_Client:


    def on_connect(self, client, userdata, flags, rc):
        print('on_connect(): {}'.format(mqtt.connack_string(rc)))
        self.client.subscribe("sensor")
        #self.client.subscribe("humidity")
        
    def on_message(self, client, userdata, msg):
        print('on_message(): topic: {}'.format(msg.topic))
        try:
            while True:
                self.client.publish("temperature", a.temperature_sensor())
                self.client.publish("humidity", a.humidity_sensor())
                sleep(1)

        except e:
            print ("dette er feil", e)
       
        
            

    def start(self, broker, port):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        print('Connecting to {}:{}'.format(broker, port))
        self.client.connect(broker, port)
        print("connect")

        
        try:
            thread = Thread(target=self.client.loop_forever())
            thread.start()
        except KeyboardInterrupt:
            print('Interrupted')
            self.client.disconnect()
a = Sensor.RPI_SENSOR()
#print(Sensor.RPI_SENSOR.temperature_sensor(a))
test = MQTT_Client()
test.start(broker, port)
