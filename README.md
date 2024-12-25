# Achoo Alert - Proactive Allergy Management System

### SETU Computer Systems and Networks Assignment 2: IoT Application

## Table of Contents
- [About the project](#about-the-project)
- [Features](#features)
- [Future plans](#future-plans)
- [Getting started](#getting-started)
- [Folder Structure](#folder-structure)
- [Configuration](#configuration)
- [Credits](#credits)

## About the project

Achoo Alert is a prototype Internet of Things (IoT) project for the Raspberry Pi 5, designed to help individuals proactively manage their allergies. Users interface with the system via a Blynk app, where the user can view information from the app, set preferences, receive notifications, and even control other devices.

The system monitors pollen for a given location hourly using the Ambee Pollen API, and alerts the user via a Blynk app if the risk is high. Using a Sense Hat add-on, users may also request ad hoc information on pollen risk level by pressing the joystick. Information about the current risk will scroll across the Sense Hat, colour-coded from green to red in order of risk severity.

As indoor humidity is an important factor in controlling allergy symptoms, the system also provides an automated solution for managing humidity. Currently, it mocks sensors and humidity devices by integrating with Cisco Packet Tracer (PT). The process is started by a humidity sensor monitoring and sends humidity to the Pi, which writes this data to Blynk, a low-code IoT platform. By fetching user preferences from Blynk, the system then determines whether the humidity falls outside of the desired range, and sends control signals to an air conditioner or humidifier to bring the indoor humidity back into the desired range.

## Features

- 
- 
- 

## Future plans:

The next steps in development will be to integrate with the Ambee Air Quality API in addition to air purifiers, which can be triggered to turn on when air quality is poor or the pollen count high.

## Getting started

### Hardware Requirements:

- Raspberry Pi 5: The central IoT device for data collection, processing, and communication.
- Sense HAT: For joystick and LED matrix, for ad-hoc pollen risk information.
- Laptop with [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer) installed, on the same local network as your Raspberry Pi.

### Blynk Configuration:
To run Achoo Alert, users must first configure Blynk. The steps are:
- [Sign up for a Blynk account](https://blynk.cloud/dashboard/login)
- Create a new template, title it "Achoo Alert", and select "Raspberry Pi" and "Wifi".
- Add seven Datastreams [as pictured here](img/datastreams.png).
- Set up a Web Dashboard [as pictured here](img/web-dashboard.png).
- Create [2 Events & Notifications](img/events-notifications.png). Use the following pictures as a reference. [1](img/min-max-not-set-1.png) [2](img/min-max-not-set-2.png) [3](img/pollen-event-1.png) [4](img/pollen-event-2.png)
- Set up a [high pollen count automation](img/high-pollen-count-automation.png).
- Install [and configure](img/blynk-mobile-app.png) Blynk on your mobile phone.

### Packet Tracer Configuration
On your laptop, open the "pi-project.pkt" file found in the packet-tracer directory. Click the Humidity Sensor, then "Advanced", and then the "Programming" tab. Open the ``py_bridge.py`` file and enter the local IP address of your Raspberry Pi for the global variable IP. You may find the IP of your Pi by running ``hostname -I``.

### Ambee API
To fetch data about pollen levels, users must first [sign up for Ambee](https://www.getambee.com/) and get an API key.

### Installation
On your Raspberry Pi, install Achoo Alert's dependencies and clone the repo. 
```bash
apt install git python3-dev gcc g++ libopenjp2-7 python3 python3-pip python3-venv
git clone https://github.com/bit-of-a-git/achoo-alert
git clone https://github.com/RPi-Distro/RTIMULib/
cd RTIMULib/Linux/python
python setup.py build
python setup.py install
cd ../../../achoo-alert
pip install -r requirements.txt
```

The local IP address of your laptop will be needed for this next step. You may find this via ``ipconfig`` on Windows Command Prompt, or ``hostname -I`` on Linux. Next, use the .env.example file to populate a .env file. Add your Blynk template name and auth token. For the control device IP, use the local IP address of your laptop and the default port of 1234 (unless this has been changed on the virtual Pi in Packet Tracer). For pollen configurations, put in your desired location (e.g. "Galway", "Waterford", "Cork", "Dublin") and your API key.

### Running the App
Users may run the app with the following command:
```bash
python achoo-alert/main.py
```

Next, go to Packet Tracer. Click on SBC-PT and open the "Programming" tab. Press "Run" to start a TCP server which will listen for commands from your Raspberry Pi. Next, click on the Humidity Sensor and open the "Programming" tab. Click run to begin sending humidity readings to the Raspberry Pi. 

Next, navigate to the Blynk app on your mobile phone. Here you may set your desired minimum and maximum humidity in addition to enabling or disabling automatic mode. If in manual mode, users may use the bottom two buttons to turn on the humidifier or AC. Users may also view the current pollen risk in addition to visualise the humidity.

## Folder Structure

```bash
.
├── achoo-alert                #
│   ├── config.py              #
│   ├── handlers.py            #
│   ├── humidity_control.py    #
│   ├── main.py                #
│   ├── pollen.py              #
│   ├── sensehat_handlers.py   #
│   ├── sensor_listener.py     #
│   └── tcp_client.py          #
├── .env.example               #
├── .gitignore
├── img                        #
│   └── Screenshot*            #
├── packet-tracer              #
│   ├── iot-devices            #
│   │   ├── main.py            #
│   │   └── py_bridge.py       #
│   ├── pi                     #
│   │   ├── device_handlers.py # putting info here
│   │   └── main.py            #
│   ├── Pi Project.pkt         #
│   └── README.md              #
├── proposal_template.md       #
├── README.md                  #
└── requirements.txt           #
```

## Configuration

General configurable options are stored in achoo-alert/config.py. These include:

```bash
RISK_COLOURS # Sets the colours used for various levels of pollen risk
SCROLL_SPEED # Sets the scroll speed of text
```

Logging configuration options are stored in achoo-alert/logging_config.py.

## Credits