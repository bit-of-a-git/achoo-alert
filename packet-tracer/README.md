# Packet Tracer Files

## /iot-devices

This folder contains Python files which are used on Packet Tracer's IoT devices, such as humidity sensors.

### main.py

This is a template file found on Packet Tracer's Humidity Sensor which has been slightly modified. As it returns values in the range of 0 to 255, it has been modified to convert the value to one in the range of 0 to 100 and then round the value. It then passes the value to py_bridge, which sends the value to a UDP server.

### py_bridge.py

This is a file provided in one of our labs. It has been slightly modified to send data to the UDP server via JSON.

## /pi

This folder contains Python files which are used on Packet Tracer's version of a Pi.

### main.py

This is a template called "Real TCP Server - Python" which can be found on Packet Tracer's version of a Pi. It has been slightly modified to pass any data received to a handler function, which is found in device_handlers.py. It returns a JSON object to the client, which can be used to determine the success of any commands sent to the server.

### device_handlers.py

This has been added to the Pi. When the TCP server receives JSON, it is passed to a handler in this file which first checks whether the value for "device" is "ac" or "humidifier". If so, it passes the value for "action" to the respective handler for "ac" or "humidifier". If the value for "action" is "on" or "off", it will turn on or off the device and inform the client by returning data.