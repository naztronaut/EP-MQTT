# EP MQTT Setup 

<img src="img/PythonMQTT.jpg" alt="Python MQTT Thumbnail" width="700px">


## Install Mosquitto
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

## Install Paho-Mqtt Python Library 
Install paho-mqtt:

```shell
sudo pip3 install paho-mqtt
```

## Set up `mqtt_subscriber.py` as a service

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

## Set up authentication for your Mosquitto broker

#### Method 1: Create a password file manually:

```shell
nano password_file
```

Add your credentials:

```shell
username:password
```

Substitute `username` for your username and `password` for your password.

Encrypt the file:

```shell
sudo mosquitto_passwd -U password_file
```

#### Method 2: Create password file via CLI

Run command:

```shell
sudo mosquitto_passwd -c password_file username
```

Substitute `username` for your username and `password` for your password.


#### Mosquitto Configuration

Move the newly created `password_file` to its proper location:

```shell
sudo mv password_file /etc/mosquitto
```

Edit the configuration file:

```shell
cd /etc/mosquitto 
sudo nano mosquitto.conf
```

Add the two following lines at the end:

```
allow_anonymous false
password_file /etc/mosquitto/password_file
```
Also be sure to look at the [mosquitto.conf](mosquitto.conf) file in this repo for a full example. 

Restart mosquitto service:

```shell
sudo service mosquitto restart
```