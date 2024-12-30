import logging

import config
import logging_config
from BlynkLib import Blynk
from humidity_control import send_device_command


def set_up_blynk_handlers(blynk):
    # Synchronises device values to server values upon connection
    @blynk.on("connected")
    def blynk_connected():
        logging.info("Updating V1,V2,V3 values from the server...")
        blynk.sync_virtual(1, 2, 3)

    # The below handlers are triggered when the corresponding virtual pin is written to
    @blynk.on("V1")
    def handle_v1_write(value):
        config.min_humidity = int(value[0])
        logging.info(f"Min humidity set to {config.min_humidity}")

    @blynk.on("V2")
    def handle_v2_write(value):
        config.max_humidity = int(value[0])
        logging.info(f"Max humidity set to {config.max_humidity}")

    @blynk.on("V3")
    def handle_v3_write(value):
        config.auto_enabled = value[0] == "1"
        logging.info(
            f"Automatic mode {'enabled' if config.auto_enabled else 'disabled'}"
        )

    # The below handlers run when pins 4 and 5 are written to. These are used to manually control the humidity control devices
    @blynk.on("V4")
    def handle_v4_write(value):
        if not config.auto_enabled:
            if value[0] == "1":
                send_device_command("ac", "on")
            else:
                send_device_command("ac", "off")

    @blynk.on("V5")
    def handle_v5_write(value):
        if not config.auto_enabled:
            if value[0] == "1":
                send_device_command("humidifier", "on")
            else:
                send_device_command("humidifier", "off")


# Alerts the user via the app that the min and max humidity levels have not been set
def check_humidity_thresholds(blynk):
    if config.min_humidity is None or config.max_humidity is None:
        blynk.log_event("min_max_not_set")
        logging.info("Logged event: Min or max humidity thresholds not set")

    else:
        logging.info(
            f"Current thresholds: Min={config.min_humidity}, Max={config.max_humidity}"
        )
