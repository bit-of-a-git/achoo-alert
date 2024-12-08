import BlynkLib
from BlynkTimer import BlynkTimer
from dotenv import load_dotenv
import os
from sense_hat import SenseHat

# Initialising global variables with "None" as default value
min_humidity = None
max_humidity = None
auto_enabled = True

load_dotenv()

# Blynk authentication token
BLYNK_AUTH = os.getenv("BLYNK_AUTH_TOKEN")

# initialise SenseHAT
sense = SenseHat()
sense.clear()

# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = BlynkTimer()


# Register handler for virtual pin V1 write event
@blynk.on("V1")
def handle_v1_write(value):
    global min_humidity
    button_value = value[0]
    print(f"Min humidity set to {button_value}")
    min_humidity = button_value


# Register handler for virtual pin V2 write event
@blynk.on("V2")
def handle_v2_write(value):
    global max_humidity
    button_value = value[0]
    print(f"Max humidity set to {button_value}")
    max_humidity = button_value


# Register handler for virtual pin V4 write event
@blynk.on("V3")
def handle_v3_write(value):
    global auto_enabled
    auto_enabled = value[0] == "1"


def send_to_blynk(pin, value):
    blynk.virtual_write(pin, value)
    print(f"{value}, Success!")


# Function to check if values are set and log an event if not
def check_humidity_values():
    if min_humidity is None or max_humidity is None:
        blynk.log_event("placeholder", "Min or max humidity not set")
        print("Logged event: Min or max humidity not set")


def check_humidity_values():
    if min_humidity is None or max_humidity is None:
        blynk.log_event("min_max_not_set")
    else:
        print(f"Current thresholds: Min={min_humidity}, Max={max_humidity}")


timer.set_interval(5, lambda: blynk.virtual_write(60, round(sense.humidity, 2)))

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for events...")
    try:
        while True:
            blynk.run()  # Process Blynk events
            timer.run()
    except KeyboardInterrupt:
        print("Blynk application stopped.")
