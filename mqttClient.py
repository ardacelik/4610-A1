import paho.mqtt.client as mqtt
import time

# message callback
def onMessage(client, obj, msg):
	print(str(msg.topic) + str(msg.payload))

mqttC = mqtt.Client()
mqttC.connect("test.mosquitto.org", 1883) # connect to server
mqttC.subscribe("temperature", "humidity") # topic/sensorTag readings(replace with actual data)
mqttC.on_message = onMessage # callback
mqttC.loop_start()

while(1): # get sensorTag data here
    mqttC.publish("temperature", 74.3) # publish temperature(replace with actual data)
	mqttC.publish("humidity", 20.1) # publish humidity(replace with actual data)
	time.sleep(1) # rate of updates