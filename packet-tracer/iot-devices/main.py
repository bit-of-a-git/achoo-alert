import math
from time import *

import py_bridge
from environment import *
from gpio import *
from physical import *
from pyjs import *

ENVIRONMENT_NAME = "Humidity"
MIN = 0
MAX = 100
ROUNDED_TO = 3


def main():
    while True:
        loop()


def loop():
    global ENVIRONMENT_NAME
    global MIN
    global MAX
    global ROUNDED_TO
    value = Environment.get(ENVIRONMENT_NAME)

    if value < MIN:
        value = MIN
    elif value > MAX:
        value = MAX

    setDeviceProperty(getName(), "level", value)

    value = math.floor(js_map(value, MIN, MAX, 0, 255))
    analogWrite(A0, value)
    roundedValue = round(value / 255 * 100, ROUNDED_TO)
    data = {"parameter": ENVIRONMENT_NAME, "value": roundedValue}
    py_bridge.send(data)
    sleep(60)


if __name__ == "__main__":
    main()
