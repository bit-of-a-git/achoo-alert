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

Achoo Alert is a prototype Internet of Things (IoT) project for the Raspberry Pi 5, designed to help individuals proactively manage their allergies. Users interact with the system via a Blynk app, where they can view information, set preferences, receive notifications, and control devices.

The system monitors pollen levels for a given location hourly using the Ambee Pollen API and alerts users via the Blynk app if the risk is high. Using a Sense HAT add-on, users can request ad hoc information on pollen risk level by pressing the joystick. Risk information scrolls across the Sense HAT’s LED matrix, color-coded from green to red by severity.

To manage indoor humidity — a key factor for allergy control — the system provides automated monitoring and control. Humidity levels are mocked using Cisco Packet Tracer (PT). The system writes humidity data to Blynk, fetches user preferences, and determines whether to activate an air conditioner or humidifier to maintain desired indoor humidity levels.

## Features

- Hourly pollen risk monitoring using the Ambee Pollen API.
- Color-coded pollen risk display on the Sense HAT LED matrix.
- Real-time humidity monitoring and automatic adjustment.
- Notifications for high pollen levels.
- Automatic or manual control of humidifier and air conditioner via Blynk.
- Cisco Packet Tracer integration for simulating sensor input and device control.

## Future plans:

- Integrate the Ambee Air Quality API to monitor overall air quality in addition to pollen levels.
- Add support for air purifiers, triggered by poor air quality or high pollen counts.

## Getting started

### Prerequisites

Ensure your Raspberry Pi and laptop are connected to the same local network.

### Hardware Requirements:

- Raspberry Pi 5: Central IoT hub.
- Sense HAT: For joystick and LED matrix interactions.
- Laptop with [Cisco Packet Tracer](https://www.netacad.com/cisco-packet-tracer) installed.

### Step 1: Blynk Configuration:
1. [Sign up for a Blynk account](https://blynk.cloud/dashboard/login)
2. Create a new template named Achoo Alert for a Raspberry Pi device.
3. Add seven Datastreams [as pictured here](img/datastreams.png).
4. Set up a Web Dashboard [as pictured here](img/web-dashboard.png).
5. Create [2 Events & Notifications](img/events-notifications.png). Use the following pictures as a reference. [1](img/min-max-not-set-1.png) [2](img/min-max-not-set-2.png) [3](img/pollen-event-1.png) [4](img/pollen-event-2.png)
6. Set up a [high pollen count automation](img/high-pollen-count-automation.png).
7. Install [and configure](img/blynk-mobile-app.png) Blynk on your mobile phone.
8. Copy the example env file with `cp .env.example .env`. Open the new .env file with a text editor of your choice, and enter your Blynk template name and auth token.

### Step 2: Packet Tracer Configuration
1. On your laptop, open the "pi-project.pkt" file found in the packet-tracer directory.
2. Click the Humidity Sensor, then "Advanced", and then the "Programming" tab. Open the ``py_bridge.py`` file and enter the local IP address of your Raspberry Pi for the global variable IP. You may find the IP of your Pi by running ``hostname -I``.
3. Start the required services:
    - On SBC-PT, click "Programming" > "Run" to start the TCP server.
    - On the Humidity Sensor, click "Programming" > "Run" to begin sending data.
4. Find the IP address of your laptop with `ipconfig` or `hostname -I`. Enter this value for CONTROL_DEVICE_IP in your .env file.

### Step 3: Ambee API
- [Sign up at Ambee](https://www.getambee.com/) to obtain an API key.
-  Add your API key and location (e.g. "Galway", "Waterford", "Cork", "Dublin") to your .env file.

### Step 4: Installation
On your Raspberry Pi, install Achoo Alert's dependencies and clone the repositories:
```bash
sudo apt install git python3-dev gcc g++ libopenjp2-7 python3 python3-pip python3-venv
git clone https://github.com/bit-of-a-git/achoo-alert
git clone https://github.com/RPi-Distro/RTIMULib/
cd RTIMULib/Linux/python
python setup.py build
python setup.py install
cd ../../../achoo-alert
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 5: Running the App
Run the application on the Raspberry Pi:
```bash
python achoo-alert/main.py
```
Next, navigate to the Blynk app on your mobile phone to configure settings and monitor data.

## Folder Structure

```bash
.
├── achoo-alert                # Main application directory
│   ├── config.py              # General configuration options
│   ├── handlers.py            # Event handlers for Blynk
│   ├── humidity_control.py    # Logic for managing humidity levels
│   ├── logging_config.py      # Logging setup
│   ├── main.py                # Main entrypoint for the application
│   ├── pollen.py              # Functions for fetching and processing pollen data
│   ├── sensehat_handlers.py   # Joystick and LED handlers for Sense HAT
│   ├── sensor_listener.py     # UDP listener for humidity data
│   └── tcp_client.py          # TCP client for Packet Tracer communication
├── .env.example               # Example file for .env configuration
├── img                        # Images for README and documentation
│   └── Screenshot*            # Blynk configuration screenshots
├── packet-tracer              # Packet Tracer project files and related scripts
│   ├── iot-devices            # IoT device simulation scripts
│   │   ├── main.py            # Fetches humidity from environment
│   │   └── py_bridge.py       # Sends data to your Raspberry Pi.
│   ├── pi                     # Packet Tracer virtual Pi scripts
│   │   ├── device_handlers.py # Parses data and determines whether to turn on or off different devices
│   │   └── main.py            # TCP server which receives data, sends to handlers, and returns responses to client
│   ├── Pi Project.pkt         # Main Packet Tracer project file
│   └── README.md              # Additional README for Packet Tracer files
├── proposal_template.md       # Proposal document for the project
├── README.md                  # This file
└── requirements.txt           # Python dependencies
```

## Configuration

General configuration options are stored in achoo-alert/config.py. These include:

```bash
RISK_COLOURS = {  # Colors for pollen risk levels
    "Low": "green",
    "Moderate": "yellow",
    "High": "orange",
    "Very High": "red"
}
SCROLL_SPEED = 0.1  # Scroll speed for Sense HAT text
```
Logging configuration options are stored in achoo-alert/logging_config.py.

## Credits