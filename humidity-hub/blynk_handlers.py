from BlynkLib import Blynk

# Initialize global variables
min_humidity = None
max_humidity = None
auto_enabled = True


# Blynk Handlers
def set_up_blynk_handlers(blynk):

    # Synchronises device values to server values upon connection
    @blynk.on("connected")
    def blynk_connected():
        print("Updating V1,V2,V3 values from the server...")
        blynk.sync_virtual(1, 2, 3)

    @blynk.on("V1")
    def handle_v1_write(value):
        global min_humidity
        min_humidity = int(value[0])
        print(f"Min humidity set to {min_humidity}")

    @blynk.on("V2")
    def handle_v2_write(value):
        global max_humidity
        max_humidity = int(value[0])
        print(f"Max humidity set to {max_humidity}")

    @blynk.on("V3")
    def handle_v3_write(value):
        global auto_enabled
        auto_enabled = value[0] == "1"
        print(f"Automatic mode {'enabled' if auto_enabled else 'disabled'}")
