import os
import json
from dotenv import load_dotenv

import BlynkLib
from BlynkTimer import BlynkTimer
from handlers import set_up_blynk_handlers, check_humidity_thresholds
from sensor_listener import SensorListener
from humidity_control import check_and_control_humidity
from pollen import fetch_highest_risk

from sense_hat import SenseHat
from sensehat_handlers import SenseHatHandler

import config

import logging
import logging_config


# Load environment variables from .env file
load_dotenv()
BLYNK_AUTH = os.getenv("BLYNK_AUTH_TOKEN")
UDP_PORT = int(os.getenv("UDP_PORT", 5000))

# Initialise Blynk and BlynkTimer instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)
timer = BlynkTimer()

# Set up event handlers for Blynk instance
set_up_blynk_handlers(blynk)


def send_pollen_to_blynk():
    risk = fetch_highest_risk()
    blynk.virtual_write(6, risk)
    if risk in ("High", "Very High"):
        blynk.log_event("pollen_event")


def handle_data(data):
    """
    Process incoming data from the UDP listener.
    """
    logging.info(f"Processing data: {data}")
    try:
        # Convert incoming JSON to a dictionary
        parsed_data = json.loads(data)

        # Checks if the 'parameter' is 'humidity'
        if parsed_data.get("parameter").lower() == "humidity":
            humidity = parsed_data["value"]
            blynk.virtual_write(0, humidity)
            if config.auto_enabled:
                check_and_control_humidity(humidity)
        else:
            logging.warning(
                f"Parameter '{parsed_data.get('parameter')}' is currently not supported."
            )
    except json.JSONDecodeError:
        logging.error("Error: Received data is not valid JSON.")


def main():
    """
    Main execution block to start the Blynk application, UDP listener, and Sense Hat joystick listener.
    """
    logging.info("Blynk application started. Listening for events...")

    # Initialises UDP listener
    listener = SensorListener(port=UDP_PORT)
    listener.callback = handle_data
    listener.start()

    sense = SenseHat()
    sensehat_handler = SenseHatHandler(sense)
    sense.stick.direction_middle = sensehat_handler.button_pressed

    # Every 60 seconds, checks whether min and max humidity levels have been set
    timer.set_timeout(60, lambda: check_humidity_thresholds(blynk))
    timer.set_interval(600, send_pollen_to_blynk)

    try:
        while True:
            blynk.run()  # Process Blynk events
            timer.run()
    except KeyboardInterrupt:
        logging.info("Blynk application stopped.")
    finally:
        listener.stop()
        sense.clear()


if __name__ == "__main__":
    main()
