import time
from typing import Any

import board
import busio
import serial
from adafruit_pm25.i2c import PM25_I2C
from digitalio import DigitalInOut, Direction, Pull

# GPIO connects to a reset pin (TODO: ??)
reset_pin: Any = None
# reset_pin = DigitalInOut(board.G0)
# reset_pin.direction = Direction.OUTPUT
# reset_pin.value = False

uart: serial.Serial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)