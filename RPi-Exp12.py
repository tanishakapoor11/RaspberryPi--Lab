from time import sleep
from random import randint
import paho.mqtt.client as MQTT
import json host = "demo.thingsboard.io"
access_token = "RoMzT0qvQh5UnpmpWM8i"
sensor_data = {'temperature': 0, 'humidity': 0}
client = MQTT.Client()
client.username_pw_set(access_token)
client.connect(host, 1883, 60)
client.loop_start()
print("Connected to MQTT.")
try:
 while True:
 sensor_data['temperature'] = randint(1,50)
 sensor_data['humidity'] = randint(51,100)
 client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
 print(f"Telemetry sent. Data: {json.dumps(sensor_data)}")
 sleep(5)
except KeyboardInterrupt:
 client.loop_stop()
 client.disconnect()
 print("Disconnecting MQTT. Exiting program...")
