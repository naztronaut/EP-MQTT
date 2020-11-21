# EP MQTT Setup 

Run the following commands to install install mosquitto:

```shell
sudo apt install -y mosquitto mosquitto-clients
```

Make sure mosquitto service is enabled:

```shell
sudo systemctl enable mosquitto.service
```

Check of mosquitto is running:

```shell
ps -ef | grep mosquitto
```

Run mosquitto as a daemon:

```shell
mosquitto -d
```

Install paho-mqtt:

```shell
sudo pip3 install paho-mqtt
```

Get the `mqtt_subscriber.py` script from this repo and place it anywhere on your server. 

Move the MQTT Subscriber service and run it:

```
sudo cp mqtt_subscriber.service /etc/systemd/system
```

Reload systemctl and turn it on:

```shell
sudo systemctl daemon-reload
sudo systemctl enable mqtt_subscriber.service
sudo service mqtt_subscriber start
```

To see if it's running:

```shell
service mqtt_subscriber/status
```

