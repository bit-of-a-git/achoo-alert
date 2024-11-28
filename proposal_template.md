# Achoo Alert - Proactive Allergy and Antihistamine Reminder System
### Student Name: David O' Connor
### Student ID: 08566496

Achoo Alert is an Internet of Things (IoT) project designed to help individuals proactively manage their allergies. The system monitors environmental factors such as humidity using the Sense HAT attached to a Raspberry Pi. It also fetches real-time pollen data from a public API. By combining this data, the system calculates allergy risk levels and notifies users to take preventive measures, such as antihistamines, before symptoms occur.

Data is logged to ThingSpeak for visualisation, and a web app allows users to interact with the system, adjust risk thresholds, and view live sensor readings. The project aims to demonstrate practical IoT integration using networking, cloud platforms, and interactivity.

## Tools, Technologies and Equipment

### Hardware:

- Raspberry Pi 5: The central IoT device for data collection, processing, and communication.
- Sense HAT: Provides onboard sensors (e.g., humidity, temperature, gyroscope) and an 8×8 LED matrix for visual alerts.

### Software/Programming:

#### Programming Language:
- Python (for Sense HAT programming, API integration, and web development).

#### Libraries and Frameworks:
- Sense HAT: To interact with the HAT's sensors and display.
- Flask: To build the web app for interactivity.
- Requests: For HTTP API requests to fetch pollen data.
- ThingSpeak API: For logging and visualising data on the cloud.
- SQLite or simple file-based storage: For local logging of thresholds and settings.

#### IoT Platforms:
- ThingSpeak: For data logging, visualisation, and analysis.
- Operating System: Raspberry Pi OS.

#### Networking/IoT Protocols:
- HTTP: To fetch pollen data from APIs.
- MQTT: For lightweight messaging between the Raspberry Pi and other components.

#### Additional Tools:
- GitHub: For version control and documentation.
- Video Editing Software: To create a demonstration video showcasing the project.
- Bash Scripts: For automating setup and running scripts on the Raspberry Pi.

## Project Repository
Created.