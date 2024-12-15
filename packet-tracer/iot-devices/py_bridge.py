from time import *
from realudp import *
import json

IP = "192.168.1.41"
PORT = 5000
socket = RealUDPSocket()


def send(data):
    socket.send(IP, PORT, json.dumps(data))


if __name__ == "__main__":
    while True:
        send("Tester")
        sleep(1)
