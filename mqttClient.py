import paho.mqtt.client as mqtt
import time
from bluepy import sensortag

# message callback
def onMessage(client, obj, msg):
	print(str(msg.topic) + str(msg.payload))

mqttC = mqtt.Client()
mqttC.connect("test.mosquitto.org", 1883) # connect to server
mqttC.subscribe("temperature") # topic/sensorTag readings(replace with actual data)
mqttC.subscribe("humidity")
mqttC.on_message = onMessage # callback
mqttC.loop_start()

tag = sensortag.SensorTag('BC:6A:29:AC:53:D1') # sensor address

time.sleep(1.0)
tag.IRtemperature.enable()
tag.waitForNotifications(1.0)

while(1): # get sensorTag data here
	time.sleep(1) # rate of updates
	mqttC.publish("temperature", tag.IRtemperature.read()) # publish temperature(replace with actual data)
	mqttC.publish("humidity", 20.1) # publish humidity(replace with actual data)
