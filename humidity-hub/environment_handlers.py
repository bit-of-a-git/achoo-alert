from sense_hat import SenseHat

sense = SenseHat()
sense.clear()


def get_humidity():
    """Fetch and return the current humidity."""
    return round(sense.humidity, 2)


def check_humidity_values(blynk, min_humidity, max_humidity):
    """Log event if humidity thresholds are not set."""
    if min_humidity is None or max_humidity is None:
        blynk.log_event("min_max_not_set", "Humidity thresholds are not set.")
        print("Logged event: Min or max humidity not set")
    else:
        print(f"Thresholds set: Min={min_humidity}, Max={max_humidity}")
