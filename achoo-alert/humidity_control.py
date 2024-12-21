from tcp_client import TCPClient
import config
import json
import os
from dotenv import load_dotenv

load_dotenv()

CONTROL_DEVICE_IP = os.getenv("CONTROL_DEVICE_IP")
CONTROL_DEVICE_PORT = int(os.getenv("CONTROL_DEVICE_PORT"))


def check_and_control_humidity(humidity):
    """
    Checks if the current humidity is within the acceptable range.
    If not, sends commands to control the AC or humidifier.
    """
    if humidity < config.min_humidity:
        # As the humidity is too low, this turns on the humidifier and off the AC
        send_device_command("humidifier", "on")
        send_device_command("ac", "off")
    elif humidity > config.max_humidity:
        # As the humidity is too high, this turns on the AC and off the humidifier
        send_device_command("humidifier", "off")
        send_device_command("ac", "on")
    else:
        # As the humidity is within the range, this ensures both devices are off
        send_device_command("humidifier", "off")
        send_device_command("ac", "off")


def send_device_command(device, action):
    """
    Sends a command to the device to either turn it on or off.
    Uses TCPClient to send the command to the server.
    """
    tcp_client = TCPClient(CONTROL_DEVICE_IP, CONTROL_DEVICE_PORT)

    tcp_client.connect()

    if tcp_client.client_socket:
        command = json.dumps({"device": device, "action": action})
        print(f"Sending command to {device}: {command}")
        return_message = tcp_client.send_message(command)
        print(return_message)
        tcp_client.close()
