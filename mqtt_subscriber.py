import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe([("ep_mqtt/test", 1), ("ep_mqtt/topic2", 1), ("ep_mqtt/topic3", 1)])


def on_message(client, userdata, message):
    print("Message received: " + message.topic + " : " + str(message.payload))
    if message.topic == 'python/topic2':
        with open('/home/pi/mqtt_update.txt', 'a+') as f:
            f.write("received topic2")


broker_address = "localhost"  # Broker address
port = 1883  # Broker port
# user = "yourUser"                    #Connection username
# password = "yourPassword"            #Connection password

client = mqtt.Client()  # create new instance
# client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(broker_address, port=port)  # connect to broker

client.loop_forever()
