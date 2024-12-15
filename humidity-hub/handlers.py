from BlynkLib import Blynk
import config


def set_up_blynk_handlers(blynk):

    # Synchronises device values to server values upon connection
    @blynk.on("connected")
    def blynk_connected():
        print("Updating V1,V2,V3 values from the server...")
        blynk.sync_virtual(1, 2, 3)

    @blynk.on("V1")
    def handle_v1_write(value):
        config.min_humidity = int(value[0])
        print(f"Min humidity set to {config.min_humidity}")

    @blynk.on("V2")
    def handle_v2_write(value):
        config.max_humidity = int(value[0])
        print(f"Max humidity set to {config.max_humidity}")

    @blynk.on("V3")
    def handle_v3_write(value):
        config.auto_enabled = value[0] == "1"
        print(f"Automatic mode {'enabled' if config.auto_enabled else 'disabled'}")


# Alerts the user via the app that the min and max humidity levels have not been set
def check_humidity_thresholds(blynk):
    if config.min_humidity is None or config.max_humidity is None:
        blynk.log_event("min_max_not_set")
        print("Logged event: Min or max humidity thresholds not set")

    else:
        print(
            f"Current thresholds: Min={config.min_humidity}, Max={config.max_humidity}"
        )
